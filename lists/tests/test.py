from django.test import Client
from django.urls import resolve
from django.test import TestCase

from ..views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        csrf_client = Client()
        response = csrf_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_can_save_POST_request(self):
        csrf_client = Client()
        response = csrf_client.post('/', data={'new_item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
