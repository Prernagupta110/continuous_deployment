from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_book():
    response = client.post("/book", json={
        "id": "1", "name": "Sample Book", "author": "Author Name", "isbn": "1234567890123", "rating": 4, "publish_date": "2023-01-01T00:00:00"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Book created", "id": "1"}

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200

def test_get_book():
    response = client.get("/book/1")
    assert response.status_code == 200
    assert response.json()["id"] == "1"
