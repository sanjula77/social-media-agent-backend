import ollama
from app.models.post import Post
from app.utils.logger import logger

async def generate_post(transcript: str, platform: str) -> list[Post]:
    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "system", "content": "You are a social media agent..."},
                {"role": "user", "content": f"Create a creative post for {platform} based on:\n{transcript}"}
            ]
        )
        return [Post(platform=platform, content=response["message"]["content"])]
    except Exception as e:
        logger.error(f"LLM generation failed: {e}")
        return []
