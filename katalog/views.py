from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    catalog_items = CatalogItem.objects.all()
    context = {
        'list_catalog' : catalog_items,
        'nama' : 'Naufal Zhafari Zahran',
        'student_id' : '2106752104'
    }
    return render(request, 'katalog.html', context)