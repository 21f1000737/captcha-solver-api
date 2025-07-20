#!/usr/bin/env python3
"""
Deploy to Render using their API
"""

import requests
import json
import os

def deploy_to_render():
    """Deploy the application to Render"""
    
    # Render service configuration
    service_config = {
        "type": "web_service",
        "name": "captcha-solver-api",
        "repo": "https://github.com/21f1000737/captcha-solver-api",
        "branch": "master",
        "buildCommand": "pip install -r requirements.txt",
        "startCommand": "uvicorn main:app --host 0.0.0.0 --port $PORT",
        "envVars": [
            {
                "key": "PYTHON_VERSION",
                "value": "3.11.0"
            }
        ],
        "serviceDetails": {
            "env": "python",
            "region": "oregon",
            "plan": "free"
        }
    }
    
    print("Repository created: https://github.com/21f1000737/captcha-solver-api")
    print("\nTo deploy on Render:")
    print("1. Go to https://render.com")
    print("2. Sign up/Login with GitHub")
    print("3. Click 'New Web Service'")
    print("4. Connect the repository: https://github.com/21f1000737/captcha-solver-api")
    print("5. Use these settings:")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT")
    print("   - Environment: Python 3")
    print("6. Deploy!")
    print("\nYour API will be available at: https://captcha-solver-api.onrender.com/captcha")

if __name__ == "__main__":
    deploy_to_render()