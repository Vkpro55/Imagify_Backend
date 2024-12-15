from pydantic import BaseModel

class ImageMetadataBase(BaseModel):
    image_path: str
    uploaded_at: str

class ImageMetadataCreate(ImageMetadataBase):
    pass

class ImageMetadata(ImageMetadataBase):
    id: str  # MongoDB's ObjectId will be a string when converted to JSON

    class Config:
        orm_mode = True
