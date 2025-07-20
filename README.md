# CAPTCHA Solver API

A FastAPI application that solves multiplication problems from CAPTCHA images.

## Features

- Accepts POST requests with image files containing multiplication problems
- Uses OCR (Tesseract) to extract text from images
- Calculates multiplication results
- Returns JSON response with answer and email

## API Endpoint

**POST** `/captcha`

**Request:** Multipart form data with image file
**Response:** 
```json
{
  "answer": 123456789012345678,
  "email": "21f1000737@ds.study.iitm.ac.in"
}
```

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Tesseract OCR:
```bash
# macOS
brew install tesseract

# Ubuntu/Debian
sudo apt-get install tesseract-ocr

# Windows
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
```

3. Run the server:
```bash
python main.py
```

## Deployment

### Railway
1. Push to GitHub
2. Connect to Railway
3. Deploy using Dockerfile

### Render
1. Push to GitHub
2. Connect to Render
3. Use Docker environment

### Vercel
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`

## Testing

Run the test script:
```bash
python test_api.py [URL]
```

Default URL: http://localhost:8000