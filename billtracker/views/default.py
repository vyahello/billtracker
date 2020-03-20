"""Module to contain not found views."""
from typing import Dict, Optional, Union, Any
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config
from billtracker.data.repository import user_by_id
from billtracker.data.models.users import User
from data import repository


@view_config(route_name="home", renderer="../templates/home/default.pt")
def home(_: Request) -> Dict[str, Optional[User]]:
    """Returns index page content."""
    return {
        "user": user_by_id(user_id=1),
    }


@view_config(route_name="details", renderer="../templates/home/details.pt", request_method="GET")
def get_details(request: Request) -> Union[Response, Dict[str, Any]]:
    """Returns bill details."""
    bill = repository.bill_by_id(bill_id=int(request.matchdict.get("bill_id")))
    return Response(status=404) if not bill else {"user": user_by_id(user_id=1), "bill": bill, "error": None}
