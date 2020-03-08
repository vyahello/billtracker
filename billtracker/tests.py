"""Module contains a list of functional tests."""
import unittest
from pyramid import testing
from pyramid.config import Configurator
from .views.default import home
from billtracker import main
from webtest import TestApp


class ViewTests(unittest.TestCase):
    """Represents testcases on views."""

    def setUp(self):
        self.config: Configurator = testing.setUp()

    def tearDown(self) -> None:
        testing.tearDown()

    def test_my_view(self) -> None:
        self.assertEqual(home(testing.DummyRequest())["project"], "Bills Tracker")


class FunctionalTests(unittest.TestCase):
    """Represents functional testcases."""

    def setUp(self):
        self.app: TestApp = TestApp(main({}))

    def test_root(self):
        self.assertTrue(b"Pyramid" in self.app.get("/", status=200).body)
