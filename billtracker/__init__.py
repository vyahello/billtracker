"""Describes API for bill tracker package."""
from pyramid.config import Configurator


def main(_, **settings):
    """This function returns a Pyramid WSGI application."""
    with Configurator(settings=settings) as config:
        config.include("pyramid_chameleon")
        config.include(".routes")
        config.scan()
    return config.make_wsgi_app()
