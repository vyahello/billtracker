"""Module to contain not found views."""
from typing import Dict, Union, List
from pyramid.view import view_config


@view_config(route_name="home", renderer="../templates/home/default.pt")
def home(_) -> Dict[str, Union[str, List[str]]]:
    """Returns home page for `Bills Tracker` tool."""
    return {"project": "Bills Tracker", "items": ["item1", "item2", "item3", "item4"]}
