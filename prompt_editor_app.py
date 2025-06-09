import streamlit as st
import os
import json
import importlib
import re
import hashlib
import sys
import boto3
from io import StringIO
import tempfile
from dotenv import load_dotenv
from summary_engine import process_clause_config, write_docx_summary

# Load environment variables
load_dotenv()

# Configure AWS S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)
S3_BUCKET = os.getenv('AWS_S3_BUCKET')

# Configure the page
st.set_page_config(
    page_title="Prompt Template Editor",
    page_icon="✏️",
    layout="wide"
)

# Initialize session state for storing edited templates and selected template
if 'edited_templates' not in st.session_state:
    st.session_state.edited_templates = {}

if 'selected_template' not in st.session_state:
    st.session_state.selected_template = None

if 'template_lines' not in st.session_state:
    st.session_state.template_lines = {}

if 'line_order' not in st.session_state:
    st.session_state.line_order = {}

# Initialize session state for saving changes
if 'pending_save' not in st.session_state:
    st.session_state.pending_save = None
if 'save_clicked' not in st.session_state:
    st.session_state.save_clicked = False
if 'save_status' not in st.session_state:
    st.session_state.save_status = None
if 'save_data' not in st.session_state:
    st.session_state.save_data = None

# Add custom CSS for drag and drop functionality
st.markdown("""
<style>
.draggable-line {
    cursor: move;
    padding: 5px;
    margin: 2px 0;
    background-color: #f0f2f6;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
}
.draggable-line:hover {
    background-color: #e6e9ef;
}
.line-controls {
    display: flex;
    align-items: center;
    gap: 5px;
}
.line-number {
    color: #666;
    font-size: 12px;
    width: 30px;
}
</style>
""", unsafe_allow_html=True)


def initialize_template_lines(template_name, lines):
    """Initialize or update template lines in session state"""
    if template_name not in st.session_state.template_lines:
        st.session_state.template_lines[template_name] = lines
        st.session_state.line_order[template_name] = list(range(len(lines)))


def add_new_line(template_name, index):
    """Add a new line after the specified index"""
    lines = st.session_state.template_lines[template_name]
    order = st.session_state.line_order[template_name]

    # Insert new line
    lines.insert(index + 1, "")
    # Update order
    new_order = list(range(len(lines)))
    st.session_state.line_order[template_name] = new_order


def delete_line(template_name, index):
    """Delete line at specified index"""
    lines = st.session_state.template_lines[template_name]
    order = st.session_state.line_order[template_name]

    if len(lines) > 1:  # Prevent deleting the last line
        del lines[index]
        # Update order
        new_order = list(range(len(lines)))
        st.session_state.line_order[template_name] = new_order


def move_line(template_name, old_index, new_index):
    """Move line from old_index to new_index"""
    lines = st.session_state.template_lines[template_name]
    order = st.session_state.line_order[template_name]

    # Ensure indices are within bounds
    new_index = max(0, min(new_index, len(lines) - 1))

    # Move the line
    line = lines.pop(old_index)
    lines.insert(new_index, line)

    # Update order
    new_order = list(range(len(lines)))
    st.session_state.line_order[template_name] = new_order


def render_editable_groups(template_name, groups, dynamic_values):
    """Render all groups with the ability to move them, while maintaining editability status"""

    # Initialize session state for all groups if not exists
    if f"{template_name}_groups" not in st.session_state:
        st.session_state[f"{template_name}_groups"] = []
        # Track editability
        st.session_state[f"{template_name}_groups_editable"] = []
        # Track deleted groups
        st.session_state[f"{template_name}_deleted_groups"] = set()
        for group in groups:
            st.session_state[f"{template_name}_groups"].append(group["lines"])
            st.session_state[f"{template_name}_groups_editable"].append(
                group["editable"])

    # Container for all groups
    groups_container = st.container()

    with groups_container:
        edited_lines = []
        groups_to_remove = set()  # Track indices of groups to remove

        # Process each group
        for group_index in range(len(st.session_state[f"{template_name}_groups"])):
            # Skip if group was previously deleted
            if group_index in st.session_state[f"{template_name}_deleted_groups"]:
                continue

            current_group = st.session_state[f"{template_name}_groups"][group_index]
            is_editable = st.session_state[f"{template_name}_groups_editable"][group_index]

            # Skip empty non-editable groups
            if not is_editable and not current_group:
                groups_to_remove.add(group_index)
                continue

            # Create columns for group controls and content
            move_col, content_col = st.columns([0.1, 0.9])

            with move_col:
                # Move up button
                if group_index > 0:
                    if st.button("↑", key=f"group_up_{group_index}", help="Move group up"):
                        # Find next valid index up
                        next_index = group_index - 1
                        while next_index in st.session_state[f"{template_name}_deleted_groups"] and next_index > 0:
                            next_index -= 1

                        if next_index >= 0 and next_index not in st.session_state[f"{template_name}_deleted_groups"]:
                            # Swap groups
                            st.session_state[f"{template_name}_groups"][group_index], \
                                st.session_state[f"{template_name}_groups"][next_index] = \
                                st.session_state[f"{template_name}_groups"][next_index], \
                                st.session_state[f"{template_name}_groups"][group_index]

                            # Swap editability flags
                            st.session_state[f"{template_name}_groups_editable"][group_index], \
                                st.session_state[f"{template_name}_groups_editable"][next_index] = \
                                st.session_state[f"{template_name}_groups_editable"][next_index], \
                                st.session_state[f"{template_name}_groups_editable"][group_index]
                            st.experimental_rerun()

                # Move down button
                if group_index < len(st.session_state[f"{template_name}_groups"]) - 1:
                    if st.button("↓", key=f"group_down_{group_index}", help="Move group down"):
                        # Find next valid index down
                        next_index = group_index + 1
                        while next_index in st.session_state[f"{template_name}_deleted_groups"] and next_index < len(st.session_state[f"{template_name}_groups"]) - 1:
                            next_index += 1

                        if next_index < len(st.session_state[f"{template_name}_groups"]) and next_index not in st.session_state[f"{template_name}_deleted_groups"]:
                            # Swap groups
                            st.session_state[f"{template_name}_groups"][group_index], \
                                st.session_state[f"{template_name}_groups"][next_index] = \
                                st.session_state[f"{template_name}_groups"][next_index], \
                                st.session_state[f"{template_name}_groups"][group_index]

                            # Swap editability flags
                            st.session_state[f"{template_name}_groups_editable"][group_index], \
                                st.session_state[f"{template_name}_groups_editable"][next_index] = \
                                st.session_state[f"{template_name}_groups_editable"][next_index], \
                                st.session_state[f"{template_name}_groups_editable"][group_index]
                            st.experimental_rerun()

            with content_col:
                if is_editable:
                    st.markdown(
                        f"**Editable Group {sum(1 for x in st.session_state[f'{template_name}_groups_editable'][:group_index] if x) + 1}:**")

                    # If group is empty, show add line button
                    if not current_group:
                        if st.button("+ Add New Line", key=f"add_line_{group_index}"):
                            st.session_state[f"{template_name}_groups"][group_index] = [
                                "New line"]
                            st.experimental_rerun()
                    else:
                        # Show grouped text area for editable content
                        group_text = "\n".join(current_group)
                        edited_text = st.text_area(
                            label=f"Edit group {group_index + 1}",
                            value=group_text,
                            key=f"{template_name}_group_{group_index}",
                            height=len(current_group) * 30 + 10,
                            label_visibility="collapsed"
                        )

                        # Update group if text changed
                        if edited_text != group_text:
                            new_lines = [line for line in edited_text.split(
                                "\n") if line.strip()]  # Remove empty lines
                            if new_lines:  # If there are non-empty lines
                                st.session_state[f"{template_name}_groups"][group_index] = new_lines
                            else:  # If all lines were deleted
                                st.session_state[f"{template_name}_groups"][group_index] = [
                                ]
                                st.experimental_rerun()

                        # Add delete button for the group
                        if st.button("🗑 Delete Group", key=f"delete_group_{group_index}", help="Delete entire group"):
                            st.session_state[f"{template_name}_groups"][group_index] = [
                            ]
                            st.experimental_rerun()
                else:
                    # Handle non-editable line as a parent element
                    if current_group:  # Only process if group is not empty
                        content_col, delete_col = st.columns([0.9, 0.1])

                        with content_col:
                            # Show the line with any dynamic content highlighted
                            # Since each non-editable line is now its own group
                            line = current_group[0]
                            dynamic_found = any(
                                dyn in line for dyn in dynamic_values)

                            if dynamic_found:
                                st.code(line, language="python")
                            else:
                                st.text(line)

                        with delete_col:
                            # Delete button for the line
                            if st.button("🗑", key=f"delete_line_{group_index}", help="Delete line"):
                                groups_to_remove.add(group_index)
                                st.session_state[f"{template_name}_deleted_groups"].add(
                                    group_index)
                                st.experimental_rerun()

            # Add lines from current group if not marked for removal
            if group_index not in groups_to_remove and group_index not in st.session_state[f"{template_name}_deleted_groups"]:
                edited_lines.extend(current_group)
            st.markdown("---")

        # Update the complete template
        if edited_lines:
            st.session_state.edited_templates[template_name] = "\n".join(
                edited_lines)

    return edited_lines


def generate_unique_key(key, line, index):
    """Generate a unique key for each text input widget"""
    # Combine all components and hash them to ensure uniqueness
    combined = f"{key}_{index}_{line}"
    return hashlib.md5(combined.encode()).hexdigest()


def load_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading JSON file: {str(e)}")
        return None


def get_json_files():
    json_dir = "simplifyJson"
    json_files = []
    try:
        for file in os.listdir(json_dir):
            if file.endswith(".json"):
                json_files.append(file)
        return sorted(json_files)
    except Exception as e:
        st.error(f"Error accessing simplifyJson directory: {str(e)}")
        return []


def read_config_from_s3(config_name):
    """Read a config file from S3"""
    try:
        # Get the object from S3
        response = s3_client.get_object(
            Bucket=S3_BUCKET,
            # Changed extension to .json
            Key=f"clause_configs/{config_name}.json"
        )
        content = response['Body'].read().decode('utf-8')

        # Parse JSON content directly
        json_data = json.loads(content)

        # Get the first key from the JSON object (e.g., "BOARD_APPROVAL_CLAUSES")
        config_dict = next(iter(json_data.values()))

        return config_dict
    except Exception as e:
        st.error(f"Error reading config from S3: {str(e)}")
        return {}


def get_config_files_from_s3():
    """List all config files in S3"""
    try:
        response = s3_client.list_objects_v2(
            Bucket=S3_BUCKET,
            Prefix='clause_configs/'
        )

        config_files = []
        for obj in response.get('Contents', []):
            filename = os.path.basename(obj['Key'])
            if filename.endswith('_config.json') and not filename.startswith('__'):
                config_files.append(filename[:-5])  # Remove .json extension
        return sorted(config_files)
    except Exception as e:
        st.error(f"Error listing configs from S3: {str(e)}")
        return []


def split_prompt_template(template):
    # Split by newlines while preserving them
    lines = template.split('\n')
    # Find dynamic content (anything between {})
    dynamic_parts = re.finditer(r'{[^}]+}', template)
    dynamic_values = [match.group() for match in dynamic_parts]
    return lines, dynamic_values


def get_config_files():
    config_dir = "clause_configs"
    config_files = []
    for file in os.listdir(config_dir):
        if file.endswith("_config.json") and not file.startswith("__"):
            config_files.append(file[:-5])  # Remove .json extension
    return sorted(config_files)


def init_save(config_name, template_name, template_content):
    """Initialize save operation by storing data in session state"""
    print(f"Initializing save for template: {template_name}")
    st.session_state.save_data = {
        'config_name': config_name,
        'template_name': template_name,
        'template_content': template_content,
        'initialized': True
    }


def save_callback():
    """Execute save operation using data from session state"""
    print("Save callback triggered")
    if st.session_state.save_data and st.session_state.save_data.get('initialized'):
        data = st.session_state.save_data
        print(f"Processing save for template: {data['template_name']}")

        try:
            if save_config_changes_to_s3(data['config_name'],
                                         {data['template_name']: data['template_content']}):
                print(f"Save successful for {data['template_name']}")
                if data['template_name'] in st.session_state.edited_templates:
                    del st.session_state.edited_templates[data['template_name']]
                st.session_state.save_status = "success"
            else:
                print(f"Save failed for {data['template_name']}")
                st.session_state.save_status = "error"
        except Exception as e:
            print(f"Error in save callback: {str(e)}")
            st.session_state.save_status = "error"

        # Clear save data after processing
        st.session_state.save_data = None
    else:
        print("No save data found in session state")


def save_config_changes_to_s3(config_name, edited_templates):
    """Save changes back to S3 using JSON format"""
    try:
        print(f"Attempting to save changes to S3 for {config_name}")
        print(f"Edited templates: {edited_templates}")

        # First read the existing file from S3
        response = s3_client.get_object(
            Bucket=S3_BUCKET,
            Key=f"clause_configs/{config_name}.json"
        )
        content = response['Body'].read().decode('utf-8')
        json_data = json.loads(content)

        # Get the wrapper key (e.g., "BOARD_APPROVAL_CLAUSES")
        wrapper_key = next(iter(json_data.keys()))
        config_dict = json_data[wrapper_key]

        # Update only the prompt_template in the dictionary while preserving all other fields
        for key, new_template in edited_templates.items():
            if key in config_dict:
                config_dict[key]['prompt_template'] = new_template
                print(f"Updated template for {key}")
            else:
                print(f"Warning: Key {key} not found in config")
                return False

        # Reconstruct the JSON with the wrapper
        json_data[wrapper_key] = config_dict
        final_content = json.dumps(json_data, indent=2)

        # Upload the modified content back to S3
        print(f"Uploading modified content to S3")
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=f"clause_configs/{config_name}.json",
            Body=final_content.encode('utf-8')
        )

        print(f"Save completed successfully")
        return True

    except Exception as e:
        print(f"Error saving changes to S3: {str(e)}")
        st.error(f"Error saving changes to S3: {str(e)}")
        return False


def run_summary_generation(json_data, config_dict, selected_template=None):
    try:
        summary_outputs = []
        prompt_logs = []  # Store prompts for logging

        # If selected_template is provided, only process that template
        if selected_template:
            templates_to_process = {
                selected_template: config_dict[selected_template]}
        else:
            templates_to_process = config_dict

        for clause_name, clause_config in templates_to_process.items():
            # If we have edited this template, use the edited version
            if clause_name in st.session_state.edited_templates:
                clause_config = clause_config.copy()
                clause_config['prompt_template'] = st.session_state.edited_templates[clause_name]

            result = process_clause_config(clause_config, json_data)
            if result["output"] and result["output"] != "No output generated.":
                if (result.get("summary_type", "").lower() == "concise" and
                        clause_config.get("view_prompt", True) is False):
                    continue

                # Store the prompt and result for logging
                prompt_logs.append({
                    "clause_name": clause_name,
                    "template": clause_config['prompt_template'],
                    "final_prompt": result.get("used_prompt", "Prompt not available"),
                    "output": result["output"]
                })

                summary_outputs.append({
                    "clause_name": clause_name,
                    **result
                })

        # Generate the summary document
        write_docx_summary(summary_outputs)
        return True, prompt_logs
    except Exception as e:
        st.error(f"Error generating summary: {str(e)}")
        return False, []


def group_lines_by_editability(lines, dynamic_values):
    """Group lines into editable and non-editable sections"""
    groups = []
    current_group = {"editable": True, "lines": [], "indices": []}

    for i, line in enumerate(lines):
        has_dynamic = any(dyn in line for dyn in dynamic_values)
        is_editable = not has_dynamic

        if is_editable:
            # If current group is editable, add to it
            if current_group["editable"]:
                current_group["lines"].append(line)
                current_group["indices"].append(i)
            else:
                # If current group is not editable, save it and start new editable group
                if current_group["lines"]:
                    groups.append(current_group)
                current_group = {"editable": True,
                                 "lines": [line], "indices": [i]}
        else:
            # For non-editable lines, create a separate group for each line
            if current_group["lines"]:
                groups.append(current_group)
            # Create a new group for this single non-editable line
            groups.append({"editable": False, "lines": [line], "indices": [i]})
            # Start a new editable group
            current_group = {"editable": True, "lines": [], "indices": []}

    # Add the last group if it has any lines
    if current_group["lines"]:
        groups.append(current_group)

    return groups


def show_template_diff(original_template, edited_template):
    """Show differences between original and edited templates"""
    import difflib

    original_lines = original_template.splitlines()
    edited_lines = edited_template.splitlines()

    differ = difflib.Differ()
    diff = list(differ.compare(original_lines, edited_lines))

    removed_lines = []
    added_lines = []

    for line in diff:
        if line.startswith('- '):
            removed_lines.append(line[2:])
        elif line.startswith('+ '):
            added_lines.append(line[2:])

    return removed_lines, added_lines


def handle_save_confirmation(template_name, edited_template):
    """Handle the save confirmation and update session state"""
    st.session_state.pending_save = {
        'template_name': template_name,
        'edited_template': edited_template
    }


# Custom CSS for smaller headers
st.markdown("""
    <style>
    .small-font {
        font-size: 18px !important;
        margin-bottom: 0px !important;
    }
    .large-font {
        font-size: 28px !important;
        margin-bottom: 0px !important;
        font-weight: bold;
    }
    .smaller-font {
        font-size: 16px !important;
        margin-bottom: 0px !important;
        font-weight: bold;
    }
    .smallest-font {
        font-size: 14px !important;
        margin-bottom: 0px !important;
    }
    /* Reduce padding in Streamlit elements */
    .st-emotion-cache-z5fcl4 {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    .st-emotion-cache-16idsys p {
        margin-bottom: 0.5rem !important;
    }
    .st-emotion-cache-16idsys {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }
    /* Reduce padding in expander */
    .streamlit-expanderHeader {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }
    /* Reduce padding in text areas */
    .stTextArea {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }
    /* Reduce margins between elements */
    div.stButton > button {
        margin-top: 0.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="large-font">Prompt Template Editor</p>',
            unsafe_allow_html=True)

# Create two columns for steps 1 and 2
col1, col2 = st.columns(2)

with col1:
    # JSON File Selection (Step 1)
    st.markdown('<p class="smaller-font">1. Select JSON Source</p>',
                unsafe_allow_html=True)
    json_source = st.radio("Choose JSON source:", [
                           "Upload JSON", "Select Existing JSON"])

    json_data = None
    if json_source == "Upload JSON":
        uploaded_file = st.file_uploader("Upload JSON file", type=['json'])
        if uploaded_file:
            json_data = json.load(uploaded_file)
            st.success("✅ JSON file loaded successfully!")
    else:
        # Show dropdown for existing JSON files
        json_files = get_json_files()
        if json_files:
            selected_json = st.selectbox("Choose a JSON file:", json_files)
            if selected_json:
                json_path = os.path.join("simplifyJson", selected_json)
                json_data = load_json_file(json_path)
                if json_data:
                    st.success("✅ JSON file loaded successfully!")
        else:
            st.warning("No JSON files found in simplifyJson directory")

with col2:
    # Config File Selection (Step 2)
    st.markdown('<p class="smaller-font">2. Select Config File</p>',
                unsafe_allow_html=True)
    config_files = get_config_files_from_s3()
    selected_config = st.selectbox("Choose a config file:", config_files)

# Template Selection (Step 3)
if selected_config and json_data:
    config_dict = read_config_from_s3(selected_config)
    st.markdown('<p class="smaller-font">3. Select Template to Edit</p>',
                unsafe_allow_html=True)
    template_options = list(config_dict.keys())
    st.session_state.selected_template = st.selectbox(
        "Choose a template to edit:", template_options)

    # Full width section for Step 4 (Editing)
    if st.session_state.selected_template:
        st.markdown('<p class="smaller-font">4. Edit Selected Template</p>',
                    unsafe_allow_html=True)

        value = config_dict[st.session_state.selected_template]
        if isinstance(value, dict) and "prompt_template" in value:
            prompt_template = value["prompt_template"]

            # Split the template into lines and find dynamic content
            lines, dynamic_values = split_prompt_template(prompt_template)

            # Group lines by editability
            groups = group_lines_by_editability(lines, dynamic_values)

            # Use the new render_editable_groups function
            edited_lines = render_editable_groups(
                st.session_state.selected_template, groups, dynamic_values)

            # Show the complete edited template
            st.markdown(
                '<p class="smallest-font">Complete Template:</p>', unsafe_allow_html=True)
            st.code("\n".join(edited_lines))

            # Add run button
            if st.button("Run Summary"):
                if json_data and selected_config:
                    with st.spinner(f"Generating summary for {st.session_state.selected_template}..."):
                        success, prompt_logs = run_summary_generation(
                            json_data, config_dict, st.session_state.selected_template)
                        if success:
                            st.success(
                                f"✅ Summary generated successfully for {st.session_state.selected_template}!")

                            # Create tabs for Results and Changes
                            results_tab, changes_tab = st.tabs(
                                ["Summary Results", "Template Changes"])

                            with results_tab:
                                # Add download button for the generated summary
                                with open("clause_summary_output.docx", "rb") as file:
                                    st.download_button(
                                        label="Download Summary",
                                        data=file,
                                        file_name=f"clause_summary_{st.session_state.selected_template}.docx",
                                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                                    )

                                # Show prompts used in generation
                                if prompt_logs:
                                    st.markdown(
                                        '<p class="smaller-font">📋 Prompt Used in Generation</p>', unsafe_allow_html=True)
                                    # There should be only one log since we're processing one template
                                    log = prompt_logs[0]
                                    with st.expander(f"**{log['clause_name']}**"):
                                        st.markdown(
                                            '<p class="smallest-font">Template with Dynamic Keys</p>', unsafe_allow_html=True)
                                        st.code(log['template'])

                                        st.markdown(
                                            '<p class="smallest-font">Final Prompt (with values filled in)</p>', unsafe_allow_html=True)
                                        st.code(log['final_prompt'])

                                        st.markdown(
                                            '<p class="smallest-font">Generated Output</p>', unsafe_allow_html=True)
                                        st.code(log['output'])

                            with changes_tab:
                                if st.session_state.selected_template in st.session_state.edited_templates:
                                    st.markdown(
                                        '<p class="smaller-font">🔄 Template Changes</p>', unsafe_allow_html=True)

                                    edited_template = st.session_state.edited_templates[
                                        st.session_state.selected_template]
                                    original_template = config_dict[st.session_state.selected_template]['prompt_template']

                                    # Show the differences
                                    removed_lines, added_lines = show_template_diff(
                                        original_template, edited_template)

                                    if removed_lines:
                                        st.markdown("**Removed Lines:**")
                                        st.code('\n'.join(removed_lines),
                                                language='diff')

                                    if added_lines:
                                        st.markdown("**Added Lines:**")
                                        st.code('\n'.join(added_lines),
                                                language='diff')

                                    # Initialize save data before button click
                                    init_save(selected_config,
                                              st.session_state.selected_template,
                                              edited_template)

                                    # Add confirm button that triggers callback
                                    st.button(
                                        f"Confirm Changes for {st.session_state.selected_template}",
                                        on_click=save_callback,
                                        key=f"save_button_{st.session_state.selected_template}"
                                    )

                                    # Show save status if available
                                    if st.session_state.save_status == "success":
                                        st.success(
                                            f"✅ Changes saved successfully to S3!")
                                        st.session_state.save_status = None
                                    elif st.session_state.save_status == "error":
                                        st.error(
                                            "Failed to save changes. Please try again.")
                                        st.session_state.save_status = None
                                else:
                                    st.info(
                                        "No changes to review for this template.")
                else:
                    st.warning(
                        "Please select both a JSON file and a config file before running the summary.")
        else:
            st.warning(
                "No prompt template found in this configuration.")
elif not json_data:
    st.info("Please select a JSON file first")
elif not selected_config:
    st.info("Please select a config file")
