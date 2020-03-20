"""Module contains method to access entrypoints."""
from dataclasses import dataclass
from enum import Enum
from typing import Type


@dataclass(frozen=True)
class _Renderer:
    """Represents renderer entry."""

    default: str = "../templates/home/default.pt"
    details: str = "../templates/home/details.pt"


@dataclass(frozen=True)
class _Route:
    """Represents route entry."""

    home: str = "home"
    details: str = "details"


@dataclass(frozen=True)
class _Request:
    """Represents request entry."""

    get: str = "GET"
    post: str = "POST"


class _Status(Enum):
    """Represents status entry."""

    NOT_FOUND: int = 404

    @property
    def code(self) -> int:
        return self.value


@dataclass(frozen=True)
class Point:
    """Represents point entry."""

    renderer: _Renderer = _Renderer()
    route: _Route = _Route()
    request: _Request = _Request()
    status: Type[_Status] = _Status
