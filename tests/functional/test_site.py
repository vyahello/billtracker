import unittest
from webtest import TestApp, TestResponse
from billtracker import main
from billtracker.views import view
from billtracker.data.repository import user_by_id


class SiteTests(unittest.TestCase):
    def setUp(self) -> None:
        self._app: TestApp = TestApp(main({}))

    def test_root(self) -> None:
        response: TestResponse = self._app.get("/", status=view.status.SUCCESS.code)
        assert "Mitchael Aggiss" in response.text
        assert "Unpaid bills" in response.text

    def test_sitemap(self) -> None:
        for url in ("/", *(f"/bill/{bill.id}" for bill in user_by_id(user_id=10).bills)):  # type: str
            self._app.get(url, status=view.status.SUCCESS.code)
