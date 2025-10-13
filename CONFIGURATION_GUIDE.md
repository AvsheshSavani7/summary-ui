# Configuration Mode Guide

## Overview

The application now supports two configuration modes:
- **Local Mode**: For development - reads/writes config files from local `clause_configs` directory
- **Production Mode**: For deployment - reads/writes config files from AWS S3

## Environment Variable

Add this to your `.env` file:

```env
USE_LOCAL_CONFIGS=true   # For local development
# OR
USE_LOCAL_CONFIGS=false  # For production (S3)
```

**Default**: If not set, defaults to `false` (production/S3 mode)

## How It Works

### Local Mode (`USE_LOCAL_CONFIGS=true`)
- ✅ Reads config files from `./clause_configs/` directory
- ✅ Writes changes directly to local files
- ✅ No AWS credentials required
- ✅ Perfect for development and testing

### Production Mode (`USE_LOCAL_CONFIGS=false`)
- ✅ Reads config files from AWS S3
- ✅ Writes changes to S3 bucket
- ✅ Requires AWS credentials in `.env` file
- ✅ Used for production deployment

## Functions Updated

The following functions now automatically switch based on the `USE_LOCAL_CONFIGS` flag:

1. **`get_config_files()`** - Lists config files from local or S3
2. **`read_config(config_name)`** - Reads config from local or S3
3. **`save_config_changes(config_name, edited_templates)`** - Saves to local or S3

## Example .env File

### For Local Development:
```env
# Configuration Mode
USE_LOCAL_CONFIGS=true

# AI Model API Keys
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# AWS S3 not needed for local mode
```

### For Production:
```env
# Configuration Mode
USE_LOCAL_CONFIGS=false

# AI Model API Keys
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# AWS S3 Configuration
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=us-east-1
AWS_S3_BUCKET=your_bucket_name
```

## Code Changes Summary

### New Functions Added:
- `read_config_from_local(config_name)` - Read from local directory
- `get_config_files_from_local()` - List local config files
- `save_config_changes_to_local(config_name, edited_templates)` - Save to local files

### Wrapper Functions:
- `read_config(config_name)` - Auto-selects local or S3
- `get_config_files()` - Auto-selects local or S3
- `save_config_changes(config_name, edited_templates)` - Auto-selects local or S3

### Modified Code:
- AWS S3 client initialization now conditional
- All config read/write operations now use wrapper functions
- Seamless switching between local and S3 based on environment variable

## Testing

1. **Test Local Mode:**
   ```bash
   echo "USE_LOCAL_CONFIGS=true" > .env
   streamlit run prompt_editor_app.py
   ```

2. **Test Production Mode:**
   ```bash
   echo "USE_LOCAL_CONFIGS=false" > .env
   # Add AWS credentials to .env
   streamlit run prompt_editor_app.py
   ```

## Benefits

✨ **No Code Changes Needed** - Switch between local and production by changing one environment variable

🔧 **Easy Development** - Test locally without AWS credentials

🚀 **Production Ready** - Same code works in production with S3

🔒 **Safe** - S3 client only initialized when needed

