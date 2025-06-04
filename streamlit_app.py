import streamlit as st
import sys
import os
import json
from summary_engine import process_clause_config, write_docx_summary
from clause_configs.ordinary_course_config import ORDINARY_COURSE_CLAUSES
from clause_configs.best_efforts_config import BEST_EFFORTS_CLAUSES
import base64
from docx import Document
import subprocess

# Configure the page
st.set_page_config(
    page_title="Merger Summary Generator",
    page_icon="📄",
    layout="wide"
)

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
                    
                    # Convert DOCX to PDF
                    docx_path = "clause_summary_output.docx"
                    pdf_path = "clause_summary_output.pdf"
                    
                    # Display download button for DOCX
                    if os.path.exists(docx_path):
                        with open(docx_path, "rb") as file:
                            st.download_button(
                                label="Download DOCX",
                                data=file,
                                file_name="clause_summary_output.docx",
                                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                            )
                    
                    # Try to convert to PDF and show PDF download button
                    if convert_docx_to_pdf(docx_path, pdf_path):
                        if os.path.exists(pdf_path):
                            with open(pdf_path, "rb") as file:
                                st.download_button(
                                    label="Download PDF",
                                    data=file,
                                    file_name="clause_summary_output.pdf",
                                    mime="application/pdf"
                                )
                    
                    st.success("✅ Summary generated successfully!")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.session_state.doc_generated = False
    else:
        st.info("Please upload a JSON schema file to generate the summary.")

with tab2:
    st.subheader("Document Preview")
    if st.session_state.doc_generated:
        if os.path.exists("clause_summary_output.pdf"):
            display_pdf("clause_summary_output.pdf")
        elif os.path.exists("clause_summary_output.docx"):
            st.subheader("📄 DOCX Text Preview")
            doc_text = read_docx_text("clause_summary_output.docx")
            st.text_area("Raw Text Preview", doc_text, height=500)
        else:
            st.info("Document preview is not available. Please generate a summary first.")
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
5. Download the document in DOCX or PDF format
""")