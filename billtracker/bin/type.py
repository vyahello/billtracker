"""Module contains data entry types."""
from attr import dataclass


@dataclass
class Payment:
    """Represents payment data item."""

    id_: int
    created_date: str
    description: str
    paid: int
    total: int


@dataclass
class User:
    """Represents user data item."""

    id_: int
    name: str
    email: str
    hashed_password: str
    created_date: str
    last_login: str
