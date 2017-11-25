from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    """Docstring for HomePageTest. """
    def test_root_url_resolves_to_home_page_view(self):
        """TODO: Docstring for test_root_url_resolves_to_home_page_view.
        Returns
        -------
        TODO

        """
        found = resolve('/')
        self.assertEqual(found.func, home_page)
