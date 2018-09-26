from unittest import TestCase

from ..models import Item


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The second item'
        second_item.save()

        saved_items  = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_item = saved_items[0]
        self.assertEqual(first_item.text, 'The first item')
        second_item = saved_items[1]
        self.assertEqual(second_item.text, 'The second item')
