import enum
import pytest
from billtracker.views.point import _Renderer, _Route, _Request, Point, _Status

pytestmark = pytest.mark.unit


@pytest.fixture(scope="module")
def point() -> Point:
    return Point()


def test_rendered(point: Point) -> None:
    assert isinstance(point.renderer, _Renderer)


def test_route(point: Point) -> None:
    assert isinstance(point.route, _Route)


def test_request(point: Point) -> None:
    assert isinstance(point.request, _Request)


def test_status(point: Point) -> None:
    assert isinstance(point.status, enum.EnumMeta)


def test_status_code_not_found() -> None:
    assert _Status.NOT_FOUND.code == 404
