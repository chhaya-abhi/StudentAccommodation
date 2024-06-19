from django.test import TestCase
from .models import *
from django.urls import reverse, resolve
from studapp.views import *


# Create your tests here.
class TestUrls(TestCase):
    def setUp(self):
        print('setUp Called !')

    def test_list_url_is_resolved(self):
        url = reverse('studapp')
        print(resolve(url))
        self.assertEqual(resolve(url).func,index)