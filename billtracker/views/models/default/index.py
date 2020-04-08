"""Module contains API to operate index route view model."""
from typing import Optional
from pyramid.request import Request
from billtracker.data import repository
from billtracker.views.models.base import ViewModelBase


class IndexViewModel(ViewModelBase):
    """Represent index view model route."""

    def __init__(self, request: Request, user_id: int) -> None:
        super().__init__(request)
        self._user_id: int = user_id
        self.user: Optional[str] = repository.user_by_id(user_id)
        if not self.user:
            self.error = f"No user with ID {user_id}"

    @property
    def user_id(self) -> int:
        return self._user_id
