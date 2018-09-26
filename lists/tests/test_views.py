from django.test import Client
from django.urls import resolve
from django.test import TestCase

from ..models import Item
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

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_only_saves_item_when_necessary(self):
        csrf_client = Client()
        csrf_client.post('/', data={'new_item_text': ''})
        self.assertEqual(Item.objects.count(), 0)
