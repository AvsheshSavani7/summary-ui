# =========================
# Setup and Imports
# =========================
import sys
import os
import json
import streamlit as st
from docx import Document
import pandas as pd

sys.path.append(os.path.dirname(__file__))

from summary_engine import process_clause_config, write_docx_summary
from clause_configs.ordinary_course_config import ORDINARY_COURSE_CLAUSES
from clause_configs.best_efforts_config import BEST_EFFORTS_CLAUSES
from clause_configs.termination_config import TERMINATION_CLAUSES
from clause_configs.non_solicitation_config import NON_SOLICITATION_CLAUSES
from clause_configs.condition_to_closing_config import CONDITION_TO_CLOSING_CLAUSES
from clause_configs.financing_summary_config import FINANCING_SUMMARY_CLAUSES
from clause_configs.closing_mechanics_config  import CLOSING_MECHANICS_CLAUSES
from clause_configs.proxy_shareholder_config  import PROXY_SHAREHOLDER_CLAUSES
from clause_configs.specific_performance_config  import SPECIFIC_PERFORMANCE_CLAUSES
from clause_configs.law_jurisdiction_config  import LAW_JURISDICTION_CLAUSES
from clause_configs.party_details_config  import PARTY_DETAILS_CLAUSES
from clause_configs.timeline_config  import TIMELINE_CLAUSES
from clause_configs.outside_date_config  import OUTSIDE_DATE_CLAUSES

# =========================
# Load Config and Schema
# =========================
CLAUSE_CONFIG = {
    **ORDINARY_COURSE_CLAUSES,
    **BEST_EFFORTS_CLAUSES,
    #**TERMINATION_CLAUSES,
    #**NON_SOLICITATION_CLAUSES,
    #**FINANCING_SUMMARY_CLAUSES,
    #**CLOSING_MECHANICS_CLAUSES,
    #**CONDITION_TO_CLOSING_CLAUSES,
    #**PROXY_SHAREHOLDER_CLAUSES,
    #**SPECIFIC_PERFORMANCE_CLAUSES,
    #**LAW_JURISDICTION_CLAUSES,
    #**PARTY_DETAILS_CLAUSES,
    #**TIMELINE_CLAUSES
    # **OUTSIDE_DATE_CLAUSES
}

    # =========================
# Accept JSON filename Hardcoded 
# =========================
# with open("schema.json") as f:
#     EXAMPLE_SCHEMA_DATA = json.load(f)
    
    # =========================
# Accept JSON filename from terminal
# =========================
if len(sys.argv) < 2:
    print("❌ Please provide a JSON file name as an argument.\nUsage: python summary_main.py <filename.json>")
    sys.exit(1)

json_filename = sys.argv[1]

if not os.path.exists(json_filename):
    print(f"❌ File not found: {json_filename}")
    sys.exit(1)

with open(json_filename, "r", encoding="utf-8") as f:
    EXAMPLE_SCHEMA_DATA = json.load(f)
    
    

print("Loaded clause configs:", list(CLAUSE_CONFIG.keys()))

# =========================
# Run Clause Evaluations
# =========================
summary_outputs = []

for clause_name, clause_config in CLAUSE_CONFIG.items():
    print(f"\n→ Evaluating: {clause_name}")
    result = process_clause_config(clause_config, EXAMPLE_SCHEMA_DATA)

    if result["output"] and result["output"] != "No output generated.":
        # Skip concise summaries where view_prompt is False
        if (
            result.get("summary_type", "").lower() == "concise"
            and clause_config.get("view_prompt", True) is False
        ):
            print(f"Skipping {clause_name} (concise, view_prompt=False)")
            continue

        summary_outputs.append({
            "clause_name": clause_name,
           
            **result
        })

        print("=== CLAUSE SUMMARY OUTPUT ===")
        print(f"Clause: {clause_name}")
        if result.get("used_prompt"):
            print("Used Prompt:\n" + result["used_prompt"])
        print("Summary:\n" + result["output"])
        if result.get("references"):
            print("References:")
            for r in result["references"]:
                print("- " + r)
        else:
            print("References: [None found or resolved]")

# =========================
# Write to DOCX
# =========================
summary_outputs_sorted = sorted(summary_outputs, key=lambda x: x['summary_rank'])

write_docx_summary(summary_outputs_sorted)
print("\n✅ DOCX summary written.")

# Configure the page
st.set_page_config(
    page_title="Merger Summary Generator",
    page_icon="📄",
    layout="wide"
)

def read_docx_content(file_path):
    """Read and return the content of a DOCX file"""
    doc = Document(file_path)
    content = []
    for para in doc.paragraphs:
        if para.text.strip():  # Only add non-empty paragraphs
            content.append(para.text)
    return content

# Add a title
st.title("Merger Summary Generator")

# Create file uploader for JSON
uploaded_file = st.file_uploader("Upload your JSON schema file", type=['json'])

def generate_summary(json_data):
    summary_outputs = []
    
    for clause_name, clause_config in CLAUSE_CONFIG.items():
        with st.spinner(f'Processing: {clause_name}...'):
            result = process_clause_config(clause_config, json_data)
            
            if result["output"] and result["output"] != "No output generated.":
                if (
                    result.get("summary_type", "").lower() == "concise"
                    and clause_config.get("view_prompt", True) is False
                ):
                    continue
                
                summary_outputs.append({
                    "clause_name": clause_name,
                    **result
                })
    
    summary_outputs_sorted = sorted(summary_outputs, key=lambda x: x['summary_rank'])
    return summary_outputs_sorted

# Create tabs for different views
tab1, tab2 = st.tabs(["Generate Summary", "View Document"])

with tab1:
    # Add a generate button
    if uploaded_file is not None:
        if st.button("Generate Summary"):
            try:
                # Load JSON data
                json_data = json.load(uploaded_file)
                
                # Generate summary
                with st.spinner('Generating summary...'):
                    summary_outputs = generate_summary(json_data)
                    
                    # Write to DOCX
                    write_docx_summary(summary_outputs)
                    
                    # Display success message
                    st.success("✅ Summary generated successfully!")
                    
                    # Display download button for the generated DOCX
                    with open("clause_summary_output.docx", "rb") as file:
                        st.download_button(
                            label="Download Summary Document",
                            data=file,
                            file_name="clause_summary_output.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        )
                    
                    # Display summary in the UI
                    st.subheader("Summary Preview")
                    for summary in summary_outputs:
                        with st.expander(f"📑 {summary['clause_name']}"):
                            st.write(summary['output'])
                            if summary.get('references'):
                                st.write("**References:**")
                                for ref in summary['references']:
                                    st.write(f"- {ref}")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.info("Please upload a JSON schema file to generate the summary.")

with tab2:
    st.subheader("Document Viewer")
    
    # Check if the document exists
    if os.path.exists("clause_summary_output.docx"):
        # Read the document content
        doc_content = read_docx_content("clause_summary_output.docx")
        
        # Display document content in a clean format
        for paragraph in doc_content:
            # Check if the paragraph looks like a heading (you might want to adjust this logic)
            if paragraph.isupper() or len(paragraph) < 50:
                st.markdown(f"### {paragraph}")
            else:
                st.write(paragraph)
                st.markdown("---")  # Add a separator between paragraphs
                
        # Add download button here as well
        with open("clause_summary_output.docx", "rb") as file:
            st.download_button(
                label="Download Document",
                data=file,
                file_name="clause_summary_output.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    else:
        st.info("No document has been generated yet. Please generate a summary first.")

# Add some helpful instructions
st.sidebar.markdown("""
## How to use:
1. Upload your JSON schema file using the file uploader
2. Click the 'Generate Summary' button
3. Wait for the processing to complete
4. View the generated summary in the UI
5. Switch to the 'View Document' tab to see the full document
6. Download the DOCX file if needed
""")
