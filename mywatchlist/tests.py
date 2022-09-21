from django.test import TestCase
from django.test import Client

# Create your tests here.
class MyWatchlistTestCase(TestCase):
    def test_base(self):
        response = Client().get('/mywatchlist/')
        self.assertEqual(response.status_code,200)

    def test_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    def test_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
