from django.test import TestCase


# Create your tests here.
class SmoteTest(TestCase):

    def test_bad(self):
        self.assertEqual(1 + 1, 3)
