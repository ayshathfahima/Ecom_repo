from django.test import TestCase
from django.urls import reverse, resolve
from shop import views
from  shop.views import *

# class TestUrl(TestCase):
#     def test_home(self):
#         response=self.client.get('/')
#         print(response)
#         self.assertEquals(response.status_code, 200)

class TestUrl(TestCase):
    def test_home(self):
        myurl=reverse('home')

        print("url is",myurl)
        self.assertEqual(resolve(myurl).func, home)
        print(resolve(myurl))
