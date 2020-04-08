"""Module contains API to operate details route view model."""
from typing import Optional
from pyramid.request import Request
from billtracker.data.repository import bill_by_id, user_by_id
from billtracker.data.models.bill import Bill
from billtracker.data.models.users import User
from billtracker.views.models.base import ViewModel


class BillDetailsViewModel(ViewModel):
    """Represent details view model route."""

    def __init__(self, request: Request, user_id: int) -> None:
        super().__init__(request)
        self.bill_id: int = int(request.matchdict.get("bill_id"))
        self.bill: Optional[Bill] = bill_by_id(self.bill_id)
        self.user_id: int = user_id
        self.user: Optional[User] = user_by_id(user_id)
        self.amount: Optional[int] = None

    def validate(self) -> None:
        """Validation from form template."""
        try:
            self.amount = self.__amount
            if self.amount < 0 or self.amount > self.bill.total - self.bill.paid:  # type: ignore
                self.error = "Your amount must be more the zero and less than what you owe."
        except ValueError:
            self.error = "Amount must be an integer."

    @property
    def __amount(self) -> int:
        """Returns bill amount."""
        return int(self.request.POST.get("amount", -1))
