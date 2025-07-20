#!/usr/bin/env python3
"""
Deploy script for CAPTCHA solver API
"""

import subprocess
import sys
import os

def run_locally():
    """Run the FastAPI application locally for testing"""
    print("Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    
    print("Starting FastAPI server locally on http://localhost:8000")
    print("API endpoint: http://localhost:8000/captcha")
    print("Documentation: http://localhost:8000/docs")
    
    subprocess.run([sys.executable, "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])

def deploy_to_render():
    """Instructions for deploying to Render"""
    print("""
To deploy to Render:
1. Push this code to a GitHub repository
2. Go to https://render.com and sign up/login
3. Click 'New Web Service'
4. Connect your GitHub repository
5. Use these settings:
   - Build Command: pip install -r requirements.txt
   - Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
   - Environment: Python 3
   - Instance Type: Free
6. Add environment variable: TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata
7. Deploy

Your API will be available at: https://your-service-name.onrender.com/captcha
""")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "local":
        run_locally()
    else:
        deploy_to_render()
        print("\nFor local testing, run: python deploy.py local")