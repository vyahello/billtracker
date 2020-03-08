"""Module contains a set of methods to operate loaders."""
import json
import os
import random
from typing import List, Dict, Any, IO
import dateutil.parser
from sqlalchemy.orm import Session
from billtracker.data.session import DatabaseSession
from billtracker.data.models.bill import Bill
from billtracker.data.models.users import User

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


def _users_from_session(session: Session) -> List[User]:
    """Returns a list of users from a session."""
    users: List[User] = []
    for record in _load_from_json("USERS.json"):  # type: Dict[str, Any]
        user: User = User()
        users.append(user)
        user.email = record["email"]
        user.name = record["name"]
        user.created_date = dateutil.parser.parse(record["created_date"])
        user.last_login = dateutil.parser.parse(record["last_login"])
        user.last_login = dateutil.parser.parse(record["last_login"])
        user.hashed_password = record["hashed_password"]
        session.add(user)
    return users


def _include_bills(users: List[User]) -> None:
    """Adds users bills."""
    for record in _load_from_json("PAYMENTS.json"):  # type: Dict[str, Any]
        user: User = random.choice(users)
        bill: Bill = Bill()
        bill.created_date = dateutil.parser.parse(record["created_date"])
        bill.description = record["description"]
        bill.total = int(record["total"])
        bill.paid = min(bill.total, int(record["paid"]))
        user.bills.append(bill)
