#!/usr/bin/env python3
"""
Run the CAPTCHA solver server with ngrok for public access
"""

import subprocess
import sys
import threading
import time
import json
import requests

def start_fastapi():
    """Start the FastAPI server"""
    subprocess.run([
        sys.executable, "-m", "uvicorn", 
        "main:app", 
        "--host", "0.0.0.0", 
        "--port", "8000"
    ])

def start_ngrok():
    """Start ngrok tunnel"""
    try:
        subprocess.run(["ngrok", "http", "8000"], check=True)
    except FileNotFoundError:
        print("ngrok not found. Install it from https://ngrok.com/download")
        print("Or deploy manually to a cloud platform")

if __name__ == "__main__":
    print("Starting CAPTCHA solver server...")
    
    # Start FastAPI in a separate thread
    fastapi_thread = threading.Thread(target=start_fastapi, daemon=True)
    fastapi_thread.start()
    
    # Wait for server to start
    time.sleep(3)
    
    print("Server started on http://localhost:8000")
    print("API endpoint: http://localhost:8000/captcha")
    print("Documentation: http://localhost:8000/docs")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--ngrok":
        print("Starting ngrok tunnel...")
        start_ngrok()
    else:
        print("Run with --ngrok flag to create public tunnel")
        print("Server running locally. Press Ctrl+C to stop.")
        try:
            fastapi_thread.join()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            sys.exit(0)