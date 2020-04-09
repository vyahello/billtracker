import pytest
from pyramid.testing import DummyRequest
from pytest_mock import MockFixture
from billtracker.data.models.bill import Bill
from billtracker.data.models.users import User
from billtracker.views.default import DetailsType, home, bill_details

pytestmark = pytest.mark.unit


@pytest.fixture()
def user() -> User:
    user: User = User()
    user.id = 72
    user.bills = [Bill(), Bill(), Bill()]
    yield user


def test_home(user: User, mocker: MockFixture, dummy_request: DummyRequest) -> None:
    mocker.patch("billtracker.data.repository.user_by_id", return_value=user)
    assert home(dummy_request)["user"]


def test_bill_details(user: User, mocker: MockFixture, dummy_request: DummyRequest) -> None:
    dummy_request.matchdict["bill_id"] = 700

    for bill in user.bills:  # type: Bill
        bill.user_id = user.id

    mocker.patch("billtracker.data.repository.user_by_id", return_value=user)
    mocker.patch("billtracker.data.repository.bill_by_id", return_value=user.bills[0])
    details: DetailsType = bill_details(dummy_request)

    assert details["user"]
    assert len(details["user"].bills) > 0
