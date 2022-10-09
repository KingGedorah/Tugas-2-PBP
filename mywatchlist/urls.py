from django.urls import path
from mywatchlist.views import show_html, show_json, show_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('html/',show_html, name='show_html'),
    path('json/',show_json, name='show_json'),
    path('xml/',show_xml, name='show_xml')
]