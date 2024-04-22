from django.test import TestCase
from shop.models import *
class TestModels(TestCase):
    def test_category(self):
        category1= Category.objects.create(name="Home and Living", slug="home", desc="demo")
        self.assertEqual(str(category1), "Homeiving")
        self.assertTrue(isinstance(category1, Category))



