"""Module to contain not found view."""
from typing import Dict, Any
from pyramid.request import Request
from pyramid.view import notfound_view_config
from views import view


@notfound_view_config(renderer="../templates/errors/404.pt")
def notfound_view(request: Request) -> Dict[Any, Any]:
    """Returns `NOT FOUND` view content."""
    request.response.status = view.status.NOT_FOUND.code
    return {}
