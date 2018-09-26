from django.test import Client
from django.urls import resolve
from django.test import TestCase

from ..models import Item
from ..views import home_page


class HomePageTest(TestCase):

    def setUp(self):
        self.csrf_client = Client()

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.csrf_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_can_save_POST_request(self):
        self.csrf_client.post('/', data={'new_item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_home_page_redirect_after_POST_request(self):
        response = self.csrf_client.post('/', data={'new_item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_home_page_only_saves_item_when_necessary(self):
        self.csrf_client.post('/', data={'new_item_text': ''})
        self.assertEqual(Item.objects.count(), 0)


class ListViewTest(TestCase):

    def test_home_page_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')
