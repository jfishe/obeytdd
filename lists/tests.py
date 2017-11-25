from django.test import TestCase

class HomePageTest(TestCase):

    """Docstring for HomePageTest. """

    def test_uses_home_template(self):
        """test_uses_home_template"""
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')
