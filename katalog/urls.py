# TODO: Implement Routings Here
from django.urls import path
from katalog.views import show_catalog

app_name = 'katalog'

urlpatterns = [
    path('katalog/', show_catalog, name='show_catalog')
]