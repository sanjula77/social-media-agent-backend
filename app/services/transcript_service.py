from youtube_transcript_api import YouTubeTranscriptApi
from app.utils.logger import logger

def fetch_transcript(video_id: str) -> str | None:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item["text"] for item in transcript])
    except Exception as e:
        logger.error(f"Transcript fetch failed: {e}")
        return None
