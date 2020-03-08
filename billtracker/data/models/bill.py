"""Module contains a set of methods to operate bills."""
import datetime
from sqlalchemy import Column, Float, Integer, DateTime, String, ForeignKey
from sqlalchemy import orm
from billtracker.data.model import SqlAlchemyBase


class Bill(SqlAlchemyBase):
    """Represents bill data model type."""

    __tablename__: str = "bills"
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    created_date: Column = Column(DateTime, default=datetime.datetime.now, index=True)
    description: Column = Column(String, nullable=False)
    paid: Column = Column(Float, default=0, index=True)
    total: Column = Column(Float, default=0, index=True)
    user_id: Column = Column(Integer, ForeignKey("users.id"))
    user = orm.relation("User", back_populates="bills")

    @property
    def is_paid(self) -> bool:
        """Check is bill is paid or not."""
        return self.total <= self.paid
