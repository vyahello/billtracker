"""Module to contain not found views."""
from typing import Dict, Optional, Union, Any
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config
from billtracker.data.repository import user_by_id, bill_by_id
from billtracker.data.models.users import User
from billtracker.data.models.bill import Bill
from billtracker.views import view


@view_config(route_name=view.route.home, renderer=view.renderer.default, request_method=view.request.get)
def home(_: Request) -> Dict[str, Optional[User]]:
    """Returns index page content."""
    return {
        "user": user_by_id(user_id=1),
    }


@view_config(route_name=view.route.details, renderer=view.renderer.details, request_method=view.request.get)
def get_details(request: Request) -> Union[Response, Dict[str, Any]]:
    """Returns bill details."""
    bill: Bill = bill_by_id(bill_id=int(request.matchdict.get("bill_id")))
    return (
        Response(status=view.status.NOT_FOUND.code)
        if not bill
        else {"user": user_by_id(user_id=1), "bill": bill, "error": None}
    )
