from fastapi.testclient import TestClient
from src.core.api import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

# Note: More complex tests involving LLM calls would typically be mocked
# in a production environment to avoid API costs and latency during CI.
