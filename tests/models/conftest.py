import pytest
from pyramid.testing import setUp, tearDown, DummyRequest


@pytest.fixture(scope="session", autouse=True)
def connect_environment() -> None:
    setUp()
    yield
    tearDown()


@pytest.fixture()
def dummy_request() -> DummyRequest:
    return DummyRequest()
