import json
import os
import random
from typing import List, Dict, Any
import dateutil.parser
from sqlalchemy.orm import Session
from billtracker.data.session import DatabaseSession
from billtracker.data.models.bill import Bill
from billtracker.data.models.users import User


def load_starter() -> None:
    """Loads initial base data source."""
    print("Loading starter data...")
    session: Session = DatabaseSession.create_session()
    if session.query(Bill).count() > 0:
        session.close()
        print("Data already loaded...")
        return

    session.expire_on_commit = False
    users: List[User] = add_users(session)
    add_bills(users)
    session.commit()
    session.close()


def add_users(session: Session) -> List[User]:
    """Adds a list of users."""
    users: List[User] = []
    with open(os.path.join(DatabaseSession.folder, "USERS.json"), "r", encoding="utf-8") as stream:
        data: List[Dict[str, Any]] = json.load(stream)

    for record in data:  # type: Dict[str, Any]
        user = User()
        users.append(user)
        user.email = record.get("email")
        user.name = record.get("name")
        user.created_date = dateutil.parser.parse(record.get("created_date"))
        user.last_login = dateutil.parser.parse(record.get("last_login"))
        user.last_login = dateutil.parser.parse(record.get("last_login"))
        user.hashed_password = record.get("hashed_password")
        session.add(user)

    return users


def add_bills(users: List[User]) -> None:
    """Adds users bills."""
    with open(os.path.join(DatabaseSession.folder, "PAYMENTS.json"), encoding="utf-8") as stream:
        data: List[Dict[str, Any]] = json.load(stream)

    for record in data:  # type: Dict[str, Any]
        user = random.choice(users)
        bill = Bill()
        bill.created_date = dateutil.parser.parse(record.get("created_date"))
        bill.description = record.get("description")
        bill.total = int(record.get("total"))
        bill.paid = min(bill.total, int(record.get("paid")))
        user.bills.append(bill)
