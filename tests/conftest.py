import pytest

from starlette.config import environ
from starlette.testclient import TestClient

ENV_VARS = {
    'ENV': 'test',
    'SECRET_KEY': 'averyrandomsecretkey',
    'VERSION': '1.0.0'
}


@pytest.fixture()
def client():
    """
    Make a 'client' fixture available to test cases.
    """
    # Our fixture is created within a context manager. This ensures that
    # application startup and shutdown run for every test case.

    # add our env var overrides
    environ.update(ENV_VARS)

    from app.main import app

    with TestClient(app) as test_client:
        yield test_client
