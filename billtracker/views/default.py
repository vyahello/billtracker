"""Module to contain not found views."""
from typing import Dict, Optional, Union, Any
from pyramid.httpexceptions import HTTPFound
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config
from billtracker.data.models.users import User
from billtracker.views import view
from billtracker.models.default.index import IndexViewModel
from billtracker.models.default.details import BillDetailsViewModel
from billtracker.data.repository import add_payment

_DetailsType = Union[Response, Dict[str, Any]]


@view_config(route_name=view.route.home, renderer=view.renderer.default, request_method=view.request.get)
def home(request: Request) -> Dict[str, Optional[User]]:
    """Returns home page content.

    Args:
        request (Request): user request
    """
    return IndexViewModel(request, user_id=10).to_dict()


@view_config(route_name=view.route.details, renderer=view.renderer.details, request_method=view.request.get)
def bill_details(request: Request) -> _DetailsType:
    """Returns bill details.

    Args:
        request (Request): user request
    """
    model: BillDetailsViewModel = BillDetailsViewModel(request, user_id=10)
    if not model.bill:
        return Response(status=view.status.NOT_FOUND.code)
    return model.to_dict()


@view_config(route_name=view.route.details, renderer=view.renderer.details, request_method=view.request.post)
def pay_bills(request: Request) -> _DetailsType:
    """Make payments.

    Args:
        request (Request): user request

    Raises:
        `HTTPFound` if specific bill was not found
    """
    model: BillDetailsViewModel = BillDetailsViewModel(request, user_id=10)
    if not model.bill:
        return Response(status=view.status.NOT_FOUND.code)
    model.validate()
    if model.error:
        return model.to_dict()
    add_payment(model.amount, model.bill_id)
    return HTTPFound(location=f"/bill/{model.bill_id}")
