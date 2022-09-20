from django.urls import path
from mywatchlist.views import show_html, show_json, show_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('mywatchlist/html/',show_html, name='show_html'),
    path('mywatchlist/json/',show_json, name='show_json'),
    path('mywatchlist/xml/',show_xml, name='show_xml')
]