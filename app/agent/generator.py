from app.services.transcript_service import fetch_transcript
from app.services.ollama_service import generate_post
from app.models.post import Post
from app.core.config import settings

class SocialMediaAgent:
    async def run(self, video_id: str, platforms: list[str]) -> list[Post]:
        transcript = fetch_transcript(video_id)
        if not transcript:
            return []
        
        all_posts = []
        for platform in platforms:
            posts = await generate_post(transcript[:settings.MAX_CHARS], platform)
            all_posts.extend(posts)
        return all_posts
