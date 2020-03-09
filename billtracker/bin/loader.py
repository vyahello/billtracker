"""Module contains a set of methods to operate loaders."""
import json
import os
import random
from typing import List, Dict, Any, IO, Iterable
import dateutil.parser
from attr import dataclass
from sqlalchemy.orm import Session
from billtracker.data.session import DatabaseSession
from billtracker.data.models.bill import Bill
from billtracker.data.models.users import User
from billtracker.bin import type

_JsonType = List[Dict[Any, Any]]


def load_starter() -> None:
    """Loads initial base data source."""
    print("Loading starter data...")
    session: Session = DatabaseSession.create_session()
    if session.query(Bill).count() > 0:
        session.close()
        print("Data already loaded...")
        return

    session.expire_on_commit = False
    _include_bills(_users_from_session(session))
    session.commit()
    session.close()


def _load_from_json(name: str) -> _JsonType:
    """Converts json file content into dictionary format."""
    with open(os.path.join(DatabaseSession.folder, name), encoding="utf-8") as stream:  # type: IO[str]
        return json.load(stream)


@dataclass
class _LoaderFile:
    """Represents data files holder."""

    users: str = "USERS.json"
    payment: str = "PAYMENT.json"


class _Loader:
    """Represents loader object item."""

    def __init__(self) -> None:
        self._file: _LoaderFile = _LoaderFile()

    def users(self) -> Iterable[type.User]:
        """Returns loaded iterable of users."""
        return map(lambda record: type.User(**record), _load_from_json(self._file.users))

    def payments(self) -> Iterable[type.Payment]:
        """Returns loaded iterable of payments."""
        return map(lambda record: type.Payment(**record), _load_from_json(self._file.payment))


def _users_from_session(session: Session) -> List[User]:
    """Returns a list of users from a session."""
    users: List[User] = []
    for user_record in _Loader().users():  # type: type.User
        user: User = User()
        users.append(user)
        user.email = user_record.email
        user.name = user_record.name
        user.created_date = dateutil.parser.parse(user_record.created_date)
        user.last_login = dateutil.parser.parse(user_record.last_login)
        user.last_login = dateutil.parser.parse(user_record.last_login)
        user.hashed_password = user_record.hashed_password
        session.add(user)
    return users


def _include_bills(users: List[User]) -> None:
    """Adds users bills."""
    for payment in _Loader().payments():  # type: type.Payment
        user: User = random.choice(users)
        bill: Bill = Bill()
        bill.created_date = dateutil.parser.parse(payment.created_date)
        bill.description = payment.description
        bill.total = int(payment.total)
        bill.paid = min(bill.total, int(payment.paid))
        user.bills.append(bill)
