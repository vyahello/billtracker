"""Module contains a set of methods to operate repository."""
from typing import Optional
from sqlalchemy.orm import subqueryload, Session
from billtracker.data.session import DatabaseSession
from billtracker.data.models.users import User
from billtracker.data.models.bill import Bill


def user_by_id(user_id: int, include_bills: bool = True) -> Optional[User]:
    """Returns user by it's ID."""
    session: Session = DatabaseSession.create_session()
    try:
        if not include_bills:
            return session.query(User).filter(User.id == user_id).first()
        return session.query(User).options(subqueryload(User.bills)).filter(User.id == user_id).first()
    finally:
        session.close()


def bill_by_id(bill_id: int) -> Optional[Bill]:
    """Returns bill by it's ID."""
    session: Session = DatabaseSession.create_session()
    try:
        return session.query(Bill).filter(Bill.id == bill_id).first()
    finally:
        session.close()


def add_payment(amount: float, bill_id: int) -> Optional[Bill]:
    """Adds payment to a user account."""
    session: Session = DatabaseSession.create_session()
    session.expire_on_commit = False

    try:
        bill = session.query(Bill).filter(Bill.id == bill_id).first()

        if not bill:
            return None

        bill.paid += amount
        session.commit()
        return bill
    finally:
        session.close()
