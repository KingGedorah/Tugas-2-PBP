from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchListItem

# Create your views here.
def show_html(request):
    watchlist_item = WatchListItem.objects.all()

    watched_film = WatchListItem.objects.filter(status="Watched")
    notwatched_film = WatchListItem.objects.filter(status="Not Watched")

    watched_status = watched_film.count() >= notwatched_film.count()

    context = {
        'list_watchlist' : watchlist_item,
        'nama' : 'Naufal Zhafari Zahran',
        'student_id' : '2106752104',
        'check_status' : watched_status,
    }
    return render(request,'mywatchlist.html',context)

def show_json(request):
    watchlist_item = WatchListItem.objects.all()

    return HttpResponse(serializers.serialize("json", watchlist_item), content_type="application/json")

def show_xml(request):
    watchlist_item = WatchListItem.objects.all()

    return HttpResponse(serializers.serialize("xml", watchlist_item), content_type="application/xml")