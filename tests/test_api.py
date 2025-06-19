from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_invalid_video():
    response = client.post("/generate", json={"video_id": "xyz", "platforms": ["Twitter"]})
    assert response.status_code in [400, 404]
