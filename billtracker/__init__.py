"""Describes API for bill tracker package."""
from typing import Dict, Any
from pyramid.config import Configurator
from pyramid.router import Router


def main(_, **settings: Dict[Any, Any]) -> Router:
    """Returns a Pyramid WSGI application."""
    with Configurator(settings=settings) as config:  # type: Configurator
        config.include("pyramid_chameleon")
        config.include(".routes")
        config.scan()
    return config.make_wsgi_app()
