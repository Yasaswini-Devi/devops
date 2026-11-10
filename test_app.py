import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"healthy" in rv.data

def test_get_data(client):
    rv = client.get('/api/v1/data')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["name"] == "DevOps Lab"
