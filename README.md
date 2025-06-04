# Merger Summary Generator

A Streamlit application that generates merger summaries and can upload them to Google Drive.

## Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Set up Google Drive API:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Google Drive API
   - Configure the OAuth consent screen
   - Create OAuth 2.0 credentials (Desktop application)
   - Download the credentials and save them as `credentials.json` in the project root directory

3. Run the application:
```bash
streamlit run streamlit_app.py
```

## Features

- Generate merger summaries from JSON schema files
- Export summaries to DOCX and PDF formats
- Upload summaries to Google Drive
- View documents directly in the browser
- Download documents locally

## Usage

1. Upload your JSON schema file using the file uploader
2. Click the 'Generate Summary' button
3. Wait for the processing to complete
4. The summary will be generated in both DOCX and PDF formats
5. You can:
   - Download the files locally
   - Open them directly in Google Drive
   - Preview them in the Document Preview tab

## Note

When you first run the application with Google Drive integration, it will open a browser window asking you to authenticate with your Google account. This is a one-time process, and the credentials will be saved for future use. 