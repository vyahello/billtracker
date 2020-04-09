import pytest
from pyramid.testing import DummyRequest
from pytest_mock import MockFixture
from billtracker.data.models.bill import Bill
from billtracker.data.models.users import User
from billtracker.models.default.index import IndexViewModel

pytestmark = pytest.mark.unit


@pytest.fixture(scope="module")
def user() -> User:
    user: User = User()
    user.id = 10
    user.bills = [Bill() for _ in range(3)]
    yield user


def test_index_model(user: User, mocker: MockFixture, dummy_request: DummyRequest) -> None:
    mocker.patch("billtracker.data.repository.user_by_id", return_value=user)
    model: IndexViewModel = IndexViewModel(dummy_request, user_id=user.id)
    assert not model.error
    assert model.user
