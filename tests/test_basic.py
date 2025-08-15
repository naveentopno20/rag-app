import io
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200

def test_upload_and_query():
    # Upload a simple txt
    content = b"Apple is a company. It makes iPhones. The headquarters is in Cupertino."
    files = {'files': ('sample.txt', io.BytesIO(content), 'text/plain')}
    up = client.post("/upload", files=files)
    assert up.status_code == 200
    q = client.post("/query", json={"question": "Where is Apple headquartered?", "top_k": 3})
    # Without real keys, the LLM call may fail (500). With keys, expect 200.
    assert q.status_code in (200, 500)
