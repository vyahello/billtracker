from pytest import fixture, mark
from billtracker.bin.type import Payment, User

pytestmark = mark.unit


@fixture(scope="module")
def payment() -> Payment:
    return Payment(id_=1, created_date="6/30/2019", description="Games", paid=300, total=500)


@fixture(scope="module")
def user() -> User:
    return User(
        id_=1,
        name="Dannie",
        email="som0@gmail.com",
        hashed_password="86rV3X82LC6VFF",
        created_date="2019-12-23T13:31:30Z",
        last_login="2018-04-09T05:04:37Z",
    )


def test_payment_id(payment: Payment) -> None:
    assert payment.id_ == 1


def test_payment_created_date(payment: Payment) -> None:
    assert payment.created_date == "6/30/2019"


def test_payment_description(payment: Payment) -> None:
    assert payment.description == "Games"


def test_payment_paid(payment: Payment) -> None:
    assert payment.paid == 300


def test_payment_total(payment: Payment) -> None:
    assert payment.total == 500


def test_user_id(user: User) -> None:
    assert user.id_ == 1


def test_user_name(user: User) -> None:
    assert user.name == "Dannie"


def test_user_email(user: User) -> None:
    assert user.email == "som0@gmail.com"


def test_user_hashed_password(user: User) -> None:
    assert user.hashed_password == "86rV3X82LC6VFF"


def test_user_created_date(user: User) -> None:
    assert user.created_date == "2019-12-23T13:31:30Z"


def test_user_last_login(user: User) -> None:
    assert user.last_login == "2018-04-09T05:04:37Z"
