from bson import ObjectId
from . import schemas
from .config import db

async def create_image_metadata(original_image_path: str):
    # Create a new document in the 'image_metadata' collection
    image_metadata = {
        "original_image_path": original_image_path,
    }
    # Insert the document into the collection
    result = db.image_metadata.insert_one(image_metadata)
    return result.inserted_id
