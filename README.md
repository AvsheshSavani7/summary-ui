# Merger Summary Generator

A Streamlit application that generates merger summaries using multiple AI models (OpenAI, Google Gemini, and Anthropic Claude) and can upload them to Google Drive.

## Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
   Create a `.env` file in the project root with your API keys:
   ```
   # AI Model API Keys
   OPENAI_API_KEY=your_openai_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   
   # Configuration Mode: Set to 'true' for local development, 'false' for production (S3)
   USE_LOCAL_CONFIGS=false
   
   # AWS S3 Configuration (only needed when USE_LOCAL_CONFIGS=false)
   AWS_ACCESS_KEY_ID=your_aws_access_key
   AWS_SECRET_ACCESS_KEY=your_aws_secret_key
   AWS_REGION=your_aws_region
   AWS_S3_BUCKET=your_s3_bucket_name
   ```

   **Configuration Modes:**
   - **Local Mode** (`USE_LOCAL_CONFIGS=true`): Reads and writes config files from the local `clause_configs` directory. Use this for development and testing.
   - **Production Mode** (`USE_LOCAL_CONFIGS=false`): Reads and writes config files from AWS S3. Use this for production deployment.

3. Set up Google Drive API (optional):
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Google Drive API
   - Configure the OAuth consent screen
   - Create OAuth 2.0 credentials (Desktop application)
   - Download the credentials and save them as `credentials.json` in the project root directory

4. Run the application:
   - For the main merger summary generator:
   ```bash
   streamlit run streamlit_app.py
   ```
   - For the prompt template editor:
   ```bash
   streamlit run prompt_editor_app.py
   ```

## Features

### AI Model Support
- **OpenAI Models**: GPT-4, GPT-4.1, GPT-4o, GPT-3.5 Turbo
- **Google Gemini Models**: Gemini 2.0 Flash, Gemini 2.5 Flash, Gemini 1.5 Pro
- **Anthropic Claude Models**: 
  - Claude Opus 4.1, Claude Opus 4
  - Claude Sonnet 4, Claude Sonnet 3.7
  - Claude Haiku 3.5

### Main Features
- Generate merger summaries from JSON schema files
- Export summaries to DOCX and PDF formats
- Upload summaries to Google Drive
- View documents directly in the browser
- Download documents locally
- Edit and customize prompt templates
- Drag-and-drop template editing interface

## Usage

### Merger Summary Generator (streamlit_app.py)
1. Upload your JSON schema file using the file uploader
2. Click the 'Generate Summary' button
3. Wait for the processing to complete
4. The summary will be generated in both DOCX and PDF formats
5. You can:
   - Download the files locally
   - Open them directly in Google Drive
   - Preview them in the Document Preview tab

### Prompt Template Editor (prompt_editor_app.py)
1. Select your preferred AI model provider and model
2. Upload or select a JSON source file
3. Choose a configuration file from S3
4. Select a template to edit
5. Customize the prompt template using the drag-and-drop interface
6. Generate summaries with your customized templates

## Testing

Run the integration test to verify all components are working:
```bash
python test_anthropic_integration.py
```

## Note

When you first run the application with Google Drive integration, it will open a browser window asking you to authenticate with your Google account. This is a one-time process, and the credentials will be saved for future use. 