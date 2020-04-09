from pytest import fixture, mark
from billtracker.bin.loader import _LoaderFile

pytestmark = mark.unit


@fixture(scope="module")
def file() -> _LoaderFile:
    return _LoaderFile()


def test_file_users(file: _LoaderFile) -> None:
    assert file.users == "USERS.json"


def test_file_payment(file: _LoaderFile) -> None:
    assert file.payment == "PAYMENTS.json"
