from pydantic import BaseModel

class Post(BaseModel):
    platform: str
    content: str

class GenerateRequest(BaseModel):
    video_id: str
    platforms: list[str]
