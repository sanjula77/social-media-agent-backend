from fastapi import APIRouter, HTTPException
from app.models.post import GenerateRequest, Post
from app.agent.generator import SocialMediaAgent

router = APIRouter()
agent = SocialMediaAgent()

@router.post("/generate", response_model=list[Post])
async def generate_posts(request: GenerateRequest):
    result = await agent.run(request.video_id, request.platforms)
    if not result:
        raise HTTPException(status_code=404, detail="Could not generate posts.")
    return result
