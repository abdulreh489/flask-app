import pytest
from app import app   


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Flask!' in response.data


def test_about_route(client):
    response = client.get('/about')
    assert response.status_code == 200
    # Check that some keyword from about.html exists
    assert b'About' in response.data
