import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'Hello' in res.data


def test_about(client):
    res = client.get('/about')
    assert res.status_code == 200
    assert b'About' in res.data
