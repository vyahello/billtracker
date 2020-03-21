"""Module to contain not found views."""
from typing import Dict, Optional, Union, Any
from pyramid.httpexceptions import HTTPFound
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config
from billtracker.data.repository import user_by_id, bill_by_id, add_payment
from billtracker.data.models.users import User
from billtracker.data.models.bill import Bill
from billtracker.views import view

_DetailsType = Union[Response, Dict[str, Any]]


@view_config(route_name=view.route.home, renderer=view.renderer.default, request_method=view.request.get)
def home(_: Request) -> Dict[str, Optional[User]]:
    """Returns home page content.

    Args:
        _ (Request): user request, it is omitted as it is not used
    """
    return {
        "user": user_by_id(user_id=10),
    }


@view_config(route_name=view.route.details, renderer=view.renderer.details, request_method=view.request.get)
def bill_details(request: Request) -> _DetailsType:
    """Returns bill details.

    Args:
        request (Request): user request
    """
    bill: Optional[Bill] = bill_by_id(bill_id=int(request.matchdict.get("bill_id")))
    if not bill:
        return Response(status=view.status.NOT_FOUND.code)
    return {"user": user_by_id(user_id=10), "bill": bill, "error": None}


@view_config(route_name=view.route.details, renderer=view.renderer.details, request_method=view.request.post)
def pay_bills(request: Request) -> _DetailsType:
    """Make payments.

    Args:
        request (Request): user request

    Raises:
        `HTTPFound` if specific bill was not found
    """
    bill_id: int = int(request.matchdict.get("bill_id"))
    bill: Optional[Bill] = bill_by_id(bill_id)
    if not bill:
        return Response(status=view.status.NOT_FOUND.code)
    amount: int = int(request.POST.get("amount", -1))
    if amount < 0 or amount > bill.total - bill.paid:
        return {
            "user": user_by_id(user_id=10),
            "bill": bill,
            "error": "Your amount must be more than zero and less than what you owe.",
            "amount": amount,
        }
    add_payment(amount, bill_id)
    raise HTTPFound(location=f"/bill/{bill_id}")
