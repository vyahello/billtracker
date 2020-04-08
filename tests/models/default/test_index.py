import pytest
from pyramid import testing
from pyramid.config import Configurator
from pytest_mock import MockFixture
from billtracker.data.models.bill import Bill
from billtracker.data.models.users import User
from billtracker.models.default.index import IndexViewModel

pytestmark = pytest.mark.unit


@pytest.fixture(scope="module")
def config() -> Configurator:
    config: Configurator = testing.setUp()
    yield config
    testing.tearDown()


@pytest.fixture(scope="module")
def user(config: Configurator) -> User:
    user: User = User()
    user.id = 10
    user.bills = [Bill(), Bill(), Bill()]
    yield user


def test_index_model(user: User, mocker: MockFixture) -> None:
    mocker.patch("billtracker.data.repository.user_by_id", return_value=user)
    model: IndexViewModel = IndexViewModel(request=testing.DummyRequest(), user_id=user.id)
    assert not model.error
    assert model.user
