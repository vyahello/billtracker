from pytest import fixture
from billtracker.bin.loader import _LoaderFile
from tests import unittest


@fixture(scope="module")
def file() -> _LoaderFile:
    return _LoaderFile()


@unittest
def test_file_users(file: _LoaderFile) -> None:
    assert file.users == "USERS.json"


@unittest
def test_file_payment(file: _LoaderFile) -> None:
    assert file.payment == "PAYMENTS.json"
