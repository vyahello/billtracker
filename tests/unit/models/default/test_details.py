import pytest
from pyramid.testing import DummyRequest
from pytest_mock import MockFixture
from billtracker.data.models.bill import Bill
from billtracker.data.models.users import User
from billtracker.models.default.details import BillDetailsViewModel

pytestmark = pytest.mark.unit


@pytest.fixture()
def user() -> User:
    user: User = User()
    user.id = 74
    yield user


def test_valid_model(user: User, mocker: MockFixture, dummy_request: DummyRequest) -> None:
    bill: Bill = Bill()
    bill.id = 700
    bill.user_id = user.id
    dummy_request.matchdict["bill_id"] = bill.id
    user.bills = [bill]

    mocker.patch("billtracker.data.repository.user_by_id", return_value=user)
    mocker.patch("billtracker.data.repository.bill_by_id", return_value=bill)

    model: BillDetailsViewModel = BillDetailsViewModel(dummy_request, user.id)
    assert not model.error
    assert model.user
    assert model.bill
    assert model.bill.id == bill.id


def test_no_user(mocker: MockFixture, dummy_request: DummyRequest) -> None:
    mocker.patch("billtracker.data.repository.user_by_id", return_value=None)
    mocker.patch("billtracker.data.repository.bill_by_id", return_value=None)

    user_id: int = 10
    model: BillDetailsViewModel = BillDetailsViewModel(dummy_request, user_id)
    assert model.error
    assert f"No user with ID {user_id}" in model.error


def test_no_bill(user: User, mocker: MockFixture, dummy_request: DummyRequest) -> None:
    bill_id: int = 200
    dummy_request.matchdict["bill_id"] = bill_id
    user.bills = [Bill()]

    mocker.patch("billtracker.data.repository.user_by_id", return_value=user)
    mocker.patch("billtracker.data.repository.bill_by_id", return_value=None)

    model: BillDetailsViewModel = BillDetailsViewModel(dummy_request, user.id)
    assert model.error
    assert f"The bill with ID {bill_id} was not found" in model.error


def test_bill_not_from_user(user: User, mocker: MockFixture, dummy_request: DummyRequest) -> None:
    bill: Bill = Bill()
    bill.id = 700
    bill.user_id = user.id + 1
    dummy_request.matchdict["bill_id"] = bill.id
    user.bills = [bill]

    mocker.patch("billtracker.data.repository.user_by_id", return_value=user)
    mocker.patch("billtracker.data.repository.bill_by_id", return_value=bill)

    model: BillDetailsViewModel = BillDetailsViewModel(dummy_request, user.id)
    assert model.error
    assert not model.bill
    assert "does not belong to user" in model.error
