from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
import io
import re
import uvicorn

app = FastAPI(title="CAPTCHA Solver", description="Solves multiplication problems from CAPTCHA images")

@app.post("/captcha")
async def solve_captcha(file: UploadFile = File(...)):
    try:
        # Validate file type
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Read the uploaded image
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Extract text using OCR
        extracted_text = pytesseract.image_to_string(image, config='--psm 6')
        
        # Find multiplication pattern (8-digit number × 8-digit number)
        pattern = r'(\d{8})\s*[×x*]\s*(\d{8})'
        match = re.search(pattern, extracted_text)
        
        if not match:
            # Try alternative patterns
            pattern = r'(\d{8})\s*(\d{8})'
            numbers = re.findall(r'\d{8}', extracted_text)
            if len(numbers) >= 2:
                num1, num2 = int(numbers[0]), int(numbers[1])
            else:
                raise HTTPException(status_code=400, detail="Could not extract multiplication problem from image")
        else:
            num1, num2 = int(match.group(1)), int(match.group(2))
        
        # Calculate the result
        answer = num1 * num2
        
        # Return the response
        return JSONResponse(content={
            "answer": answer,
            "email": "21f1000737@ds.study.iitm.ac.in"
        })
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

@app.get("/")
async def root():
    return {"message": "CAPTCHA Solver API - Send POST request to /captcha with image file"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)