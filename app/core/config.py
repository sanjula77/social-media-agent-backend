from pydantic import BaseSettings

class Settings(BaseSettings):
    FRONTEND_URL: str = "http://localhost:3000"
    MAX_CHARS: int = 2000

    class Config:
        env_file = ".env"

settings = Settings()
