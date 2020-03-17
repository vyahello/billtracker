"""Module to contain not found views."""
from typing import Dict, Optional
from pyramid.request import Request
from pyramid.view import view_config
from billtracker.data.repository import user_by_id
from billtracker.data.models.users import User


@view_config(route_name="home", renderer="../templates/home/default.pt")
def home(_: Request) -> Dict[str, Optional[User]]:
    """Returns index page content."""
    return {
        "user": user_by_id(1),
    }
