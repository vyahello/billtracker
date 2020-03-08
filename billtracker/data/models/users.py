"""Module contains a set of methods to operate users."""
import datetime
from typing import List
from sqlalchemy import orm, Column, Integer, String, DateTime
from billtracker.data.model import SqlAlchemyBase
from billtracker.data.models.bill import Bill


class User(SqlAlchemyBase):
    """Represents user data model type."""

    __tablename__: str = "users"
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    name: Column = Column(String, nullable=True)
    email: Column = Column(String, index=True, nullable=True)
    hashed_password: Column = Column(String, nullable=True, index=True)
    created_date: Column = Column(DateTime, default=datetime.datetime.now, index=True)
    last_login: Column = Column(DateTime, default=datetime.datetime.now, index=True)
    bills: List[Bill] = orm.relation("Bill", order_by=Bill.created_date.desc(), back_populates="user")

    @property
    def paid_bills(self) -> List[Bill]:
        return list(filter(lambda bill: bill.paid >= bill.total, self.bills))

    @property
    def open_bills(self) -> List[Bill]:
        return list(filter(lambda bill: bill.paid < bill.total, self.bills))

    @property
    def total_owed(self) -> float:
        return sum(bill.total - bill.paid for bill in self.open_bills)

    @property
    def total_paid_off(self) -> float:
        return sum(bill.total for bill in self.paid_bills)
