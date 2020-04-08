"""Module contains API to operate view models."""
from typing import Dict, Any, Optional
from pyramid.request import Request


class ViewModelBase:
    """Represents a base class for view model."""

    def __init__(self, request: Request) -> None:
        self._request: Request = request
        self._error: Optional[str] = None

    @property
    def request(self) -> Request:
        """Returns a request."""
        return self._request

    @property
    def error(self) -> Optional[str]:
        """Returns an error."""
        return self._error

    @error.setter
    def error(self, value: str) -> None:
        """Sets an error to a value."""
        if not isinstance(value, str):
            raise TypeError(f"'{value}' value is not as 'str' data type.")
        self._error = value

    def to_dict(self) -> Dict[str, Any]:
        """Returns view model as a dictionary."""
        return self.__dict__
