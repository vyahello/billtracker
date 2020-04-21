"""Describes API for bill tracker package.

Startup of an application.
"""
import os
from typing import Dict, Any
from pyramid.config import Configurator
from pyramid.router import Router
from billtracker.bin import loader
from billtracker.data.session import DatabaseSession

__author__: str = "Volodymyr Yahello"
__email__: str = "vyahello@gmail.com"
__version__: str = "0.1.3"


def init_database() -> None:
    """Initialize database model."""
    DatabaseSession.initialize(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "storage", "bill_tracker.sqlite")
    )
    loader.load_starter()


def main(_, **settings: Dict[Any, Any]) -> Router:
    """Returns a Pyramid WSGI application."""
    with Configurator(settings=settings) as config:  # type: Configurator
        config.include("pyramid_chameleon")
        config.include(".routes")
        config.scan()
    init_database()
    return config.make_wsgi_app()
