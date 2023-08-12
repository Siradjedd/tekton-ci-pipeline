import pytest
from routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_routes_integration(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Tiger Home Page' in response.data

    response = client.get('/symbol.html')
    assert response.status_code == 200
    assert b'Tiger As Symbol' in response.data

    response = client.get('/myth.html')
    assert response.status_code == 200
    assert b'Tiger in Myth and Legend' in response.data

if __name__ == '__main__':
    pytest.main()
