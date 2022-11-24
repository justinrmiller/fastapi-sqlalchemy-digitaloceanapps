from fastapi.testclient import TestClient


def test_healthcheck(client: TestClient):
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {'status': 'OK'}


def test_details(client: TestClient):
    response = client.get("/details")
    assert response.status_code == 200
    assert response.json() == {
        'env': 'test',
        'version': '1.0.0'
    }
