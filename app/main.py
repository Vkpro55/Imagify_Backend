



import os
import time
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .crud import create_image_metadata

# Instantiate the FastAPI app
app = FastAPI()


# CORS setup for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

port = os.getenv("PORT", 8000)

# Create 'static' directory if it doesn't exist
if not os.path.exists("static"):
    os.makedirs("static")

# Endpoint to upload the original image
@app.post("/upload-image")
async def upload_image(image: UploadFile = File(...)):
    try:
        # Save the original image to disk in the 'static/' directory
        file_location = f"static/{image.filename}"
        with open(file_location, "wb") as f:
            f.write(await image.read())
        
        # Store original image metadata in MongoDB
        image_metadata_id = create_image_metadata(file_location)
        
        return JSONResponse(status_code=200, content={"message": "Image uploaded successfully", "image_id": str(image_metadata_id)})

    except Exception as e:
        print(e)  # Print the exception to debug
        return JSONResponse(status_code=500, content={"message": f"Failed to upload image: {str(e)}"})

# Endpoint to upload the mask image
@app.post("/upload-mask")
async def upload_mask(mask: UploadFile = File(...)):
    try:
        # Save the mask image to disk in the 'static/' directory with a unique filename
        mask_file_location = f"static/mask_{int(time.time())}.png"
        with open(mask_file_location, "wb") as f:
            f.write(await mask.read())
        
        # Store mask image metadata in MongoDB (linking it to the original image if necessary)
        mask_metadata_id = create_image_metadata(mask_file_location)
        
        return JSONResponse(status_code=200, content={"message": "Mask uploaded successfully", "mask_id": str(mask_metadata_id)})

    except Exception as e:
        print(e)  # Print the exception to debug
        return JSONResponse(status_code=500, content={"message": f"Failed to upload mask: {str(e)}"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(port))