import streamlit as st
import sys
import os
import json
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
import base64
from docx import Document
import subprocess
import boto3
from botocore.exceptions import NoCredentialsError
import urllib.parse

# Configure the page
st.set_page_config(
    page_title="Merger Summary Generator",
    page_icon="📄",
    layout="wide"
)

# Initialize AWS credentials from Streamlit secrets
if 'aws' not in st.secrets:
    st.error("AWS credentials not found. Please configure AWS credentials in Streamlit secrets.")
    st.stop()

# Initialize AWS S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=st.secrets["aws"]["access_key_id"],
    aws_secret_access_key=st.secrets["aws"]["secret_access_key"],
    region_name=st.secrets["aws"]["region"]
)
S3_BUCKET = st.secrets["aws"]["bucket_name"]

def upload_to_s3(local_file, s3_file):
    try:
        s3_client.upload_file(local_file, S3_BUCKET, s3_file)
        # Generate a public URL (if bucket is public)
        url = f"https://{S3_BUCKET}.s3.amazonaws.com/{urllib.parse.quote(s3_file)}"
        return url
    except NoCredentialsError:
        st.error("AWS credentials not available")
        return None
    except Exception as e:
        st.error(f"Error uploading to S3: {str(e)}")
        return None

# Add a title
st.title("Merger Summary Generator")

# Initialize session state for tracking document generation
if 'doc_generated' not in st.session_state:
    st.session_state.doc_generated = False

# Create file uploader for JSON
uploaded_file = st.file_uploader("Upload your JSON schema file", type=['json'])

# Initialize CLAUSE_CONFIG
CLAUSE_CONFIG = {
    **ORDINARY_COURSE_CLAUSES,
    **BEST_EFFORTS_CLAUSES,
    **TERMINATION_CLAUSES,
    **NON_SOLICITATION_CLAUSES,
    **FINANCING_SUMMARY_CLAUSES,
    **CLOSING_MECHANICS_CLAUSES,
    **CONDITION_TO_CLOSING_CLAUSES,
    **PROXY_SHAREHOLDER_CLAUSES,
    **SPECIFIC_PERFORMANCE_CLAUSES,
    **LAW_JURISDICTION_CLAUSES,
    **PARTY_DETAILS_CLAUSES,
    **TIMELINE_CLAUSES,
    **OUTSIDE_DATE_CLAUSES
}

def read_docx_text(path):
    doc = Document(path)
    return "\n\n".join([p.text for p in doc.paragraphs if p.text.strip()])

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

def convert_docx_to_pdf(docx_path, pdf_path):
    try:
        # Using LibreOffice for conversion
        cmd = [
            'soffice',
            '--headless',
            '--convert-to', 'pdf',
            '--outdir', os.path.dirname(pdf_path),
            docx_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # LibreOffice creates the PDF with the same name as docx
            # but with .pdf extension, so we need to rename it if necessary
            generated_pdf = docx_path.replace('.docx', '.pdf')
            if generated_pdf != pdf_path and os.path.exists(generated_pdf):
                os.rename(generated_pdf, pdf_path)
            return True
        else:
            st.error(f"PDF conversion failed: {result.stderr}")
            st.info("Please install LibreOffice: brew install libreoffice")
            return False
            
    except Exception as e:
        st.error(f"Error converting DOCX to PDF: {str(e)}")
        if "FileNotFoundError" in str(e):
            st.warning("Please install LibreOffice: brew install libreoffice")
        return False

def display_pdf(pdf_path):
    try:
        # Opening file and encoding
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        
        # Embedding PDF in HTML
        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        
        # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error displaying PDF: {str(e)}")
        st.info("Please use the download button to view the document.")

def display_office_viewer(docx_url):
    viewer_url = f"https://view.officeapps.live.com/op/embed.aspx?src={urllib.parse.quote(docx_url)}"
    st.markdown(f'<iframe src="{viewer_url}" width="100%" height="600px" frameborder="0"></iframe>', unsafe_allow_html=True)

# Create tabs for different views
tab1, tab2 = st.tabs(["Generator", "Document Preview"])

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
                    st.session_state.doc_generated = True
                    
                    # Upload to S3
                    docx_path = "clause_summary_output.docx"
                    if os.path.exists(docx_path):
                        with st.spinner('Uploading document to S3...'):
                            s3_file_name = f"summaries/{os.path.basename(docx_path)}"
                            docx_url = upload_to_s3(docx_path, s3_file_name)
                            if docx_url:
                                st.session_state.docx_url = docx_url
                                st.success("✅ Document uploaded successfully!")
                            
                            # Display download button for DOCX
                            with open(docx_path, "rb") as file:
                                st.download_button(
                                    label="Download DOCX",
                                    data=file,
                                    file_name="clause_summary_output.docx",
                                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                                )
                    
                    st.success("✅ Summary generated successfully!")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.session_state.doc_generated = False
    else:
        st.info("Please upload a JSON schema file to generate the summary.")

with tab2:
    st.subheader("Document Preview")
    if st.session_state.doc_generated and hasattr(st.session_state, 'docx_url'):
        display_office_viewer(st.session_state.docx_url)
    else:
        st.info("No document has been generated yet. Please generate a summary first.")

# Add some helpful instructions
st.sidebar.markdown("""
## How to use:
1. Upload your JSON schema file using the file uploader
2. Click the 'Generate Summary' button
3. Wait for the processing to complete
4. Switch between tabs to view:
   - Generator: Create and download summaries
   - Document Preview: View the generated document
5. Download the document in DOCX
""")