from django.test import TestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_html, show_xml, show_json


# Create your tests here.
class TestingUrl(TestCase):
    def setUp(self):
        self.urlViewHtml = reverse('mywatchlist:show_html')
        self.urlViewJson = reverse('mywatchlist:show_json')
        self.urlViewXml = reverse('mywatchlist:show_xml')
    
    def test_mywatchlist_resolve(self):
        self.assertEqual(resolve(self.urlViewHtml).func, show_html)
    
    def test_mywatchlist_json_resolve(self):
        self.assertEqual(resolve(self.urlViewJson).func, show_json)
    
    def test_mywatchlist_xml_resolve(self):
        self.assertEqual(resolve(self.urlViewXml).func, show_xml)