"""Module contains API to operate view models."""
from typing import Dict, Any, Optional
from pyramid.request import Request


class ViewModel:
    """Represents a base class for view model."""

    def __init__(self, request: Request) -> None:
        self.request: Request = request
        self.error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Returns view model as a dictionary."""
        return self.__dict__
