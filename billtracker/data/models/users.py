import datetime
from typing import List
import sqlalchemy
from sqlalchemy import orm
from billtracker.data.model import SqlAlchemyBase
from billtracker.data.models.bill import Bill


class User(SqlAlchemyBase):
    __tablename__: str = "users"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    last_login = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)

    # noinspection PyUnresolvedReferences
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
