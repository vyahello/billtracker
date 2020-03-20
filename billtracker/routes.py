"""Module contains a list of routes."""
from pyramid.config import ViewsConfiguratorMixin


def includeme(config: ViewsConfiguratorMixin) -> None:
    """Returns content of includeme route."""
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("home", "/")
    config.add_route("details", "/bill/{bill_id}")
