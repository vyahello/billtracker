"""Module to contain not found views."""
from pyramid.request import Request
from pyramid.view import view_config
from data.repository import user_by_id


@view_config(route_name='home', renderer='../templates/home/default.pt')
def home(_: Request):
    return {
        'user': user_by_id(1),
    }
