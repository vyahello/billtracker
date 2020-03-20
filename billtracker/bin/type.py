"""Module contains data entry types."""
from abc import ABC
from attr import dataclass


@dataclass
class Record(ABC):
    """The class represents record data abstraction."""

    id_: int
    created_date: str


@dataclass
class Payment(Record):
    """Represents payment data item."""

    id_: int
    created_date: str
    description: str
    paid: int
    total: int


@dataclass
class User(Record):
    """Represents user data item."""

    id_: int
    created_date: str
    name: str
    email: str
    hashed_password: str
    last_login: str
