#!/usr/bin/env python3
"""
Test script for the CAPTCHA solver API
"""

import requests
import io
from PIL import Image, ImageDraw, ImageFont

def create_test_image():
    """Create a test image with multiplication problem"""
    # Create a white image
    img = Image.new('RGB', (400, 100), color='white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    # Draw multiplication problem
    text = "12345678 × 87654321"
    draw.text((50, 30), text, fill='black', font=font)
    
    return img

def test_api(url="http://localhost:8000"):
    """Test the CAPTCHA API"""
    # Create test image
    test_img = create_test_image()
    
    # Convert to bytes
    img_bytes = io.BytesIO()
    test_img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    # Test API
    try:
        response = requests.post(
            f"{url}/captcha",
            files={"file": ("test.png", img_bytes, "image/png")}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"Success! Answer: {result['answer']}")
            print(f"Email: {result['email']}")
            
            # Verify calculation
            expected = 12345678 * 87654321
            if result['answer'] == expected:
                print("✓ Calculation is correct!")
            else:
                print(f"✗ Calculation error. Expected: {expected}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"Error testing API: {e}")

if __name__ == "__main__":
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    test_api(url)