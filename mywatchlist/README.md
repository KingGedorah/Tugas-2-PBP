# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

## Perbedaan antara JSON, XML, dan HTML
JSON merupakan singkatan dari Javascript Object Notation. JSON merupakan format data yang ringan dan berdasarkan oleh bahasa pemrograman JavScript. Format data yang dalam bentuk JSON lebih mudah dapat dibaca. Ekstensi file JSON adalah .json

XML merupakan sebuah _markup language_ yang dirancang untuk menyimpan data bukan untuk menampilkan data. XML adalah sebuah bahasa yang mendefinisikan aturan - aturan dalam penulisan dokumen dalam format bahasa yang dapat dibaca oleh manusia dan juga mesin. 

HTML atau singkatan dari HyperText Markup Language merupakan sebuah _markup language_ yang digunakan untuk mendesain halaman web. HTML merupakan kombinasi dari Hypertext dan juga _markup language_. Hypertext digunakan untuk pendefinisian _link_ antara halaman web dan _markup language_ digunakan untuk pendefinisian dokumen teks dalam tag yang digunakan pada struktur halaman web

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery berguna sebagai respon yang telah diminta oleh user terhadap platform yang kita buat. Jika tidak melakukan data delivery maka _user_ tidak dapat melihat data yang telah kita buat walaupun data tersebut sudah kita simpan dalam _database_ yang kita punya.


## Implementasi
1. Membuat sebuah project django baru bernama ```mywatchlist```
2. Menambahkan aplikasi ```mywatchlist``` pada variabel ```INSTALLED_APPS``` pada file ```settings.py``` yang berada di folder ```project_django```. Contohnya :
```python 
INSTALLED_APPS = [
      ...,
      'mywatchlist',
]
```
3. Kemudian pada file models.py yang ada pada folder ```mywatchlist``` tambahkan kode sebagai berikut :
```python
from django.db import models

class WatchListItem(models.Model):
    status = models.CharField(max_length=20)
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.CharField(max_length=20)
    review = models.TextField()
```
4. Kemudian lakukan perintah ```python manage.py makemigrations``` persiapan migrasi skema model ke _database_ Django lokal dan juga ```python manage.py migrate``` untuk migrasi sekma model ke _database_ Django lokal.
5. Buat folder ```fixtures``` di folder ```mywatchlist``` dan buat sebuah file yang bernama ```initial_mywatchlist_data```. Kemudian tambahkan kode sebagai berikut :
```javascript
[
    {
        "model": "mywatchlist.watchlistitem",
        "pk": 1,
        "fields": {
            "status": "Watched",
            "title": "Ready Player One",
            "rating": "8",
            "release_date": "28/03/2018",
            "review": "One of the best movies"
        }
    },
    {
        "model": "mywatchlist.watchlistitem",
        "pk": 2,
        "fields": {
            "status": "Watched",
            "title": "Everything Everywhere All At Once",
            "rating": "8",
            "release_date": "22/06/2022",
            "review": "Amazing movie about multiverse"
        }
    },
    {
        "model": "mywatchlist.watchlistitem",
        "pk": 3,
        "fields": {
            "status": "Watched",
            "title": "Your Name",
            "rating": "9",
            "release_date": "07/12/2016",
            "review": "Makoto shinkai's masterpiece"
        }
    },
    {
        "model": "mywatchlist.watchlistitem",
        "pk": 4,
        "fields": {
            "status": "Watched",
            "title": "Avatar",
            "rating": "9",
            "release_date": "17/12/2009",
            "review": "One of the best movies"
        }
    },
    {
        "model": "mywatchlist.watchlistitem",
        "pk": 5,
        "fields": {
            "status": "Watched",
            "title": "Maquia: When The Promised Flower Blooms",
            "rating": "8",
            "release_date": "24/08/2018",
            "review": "Highly recommend to watch"
        }
    },
    {
        "model": "mywatchlist.watchlistitem",
        "pk": 6,
        "fields": {
            "status": "Watched",
            "title": "Interstellar",
            "rating": "8",
            "release_date": "06/11/2014",
            "review": "One of the best movies about sci-fi"
        }
    },
    {
        "model": "mywatchlist.watchlistitem",
        "pk": 7,
        "fields": {
            "status": "Watched",
            "title": "The Dark Knight",
            "rating": "9",
            "release_date": "18/07/2008",
            "review": "Great Film"
        }
    },
    {
        "model": "mywatchlist.watchlistitem",
        "pk": 8,
        "fields": {
            "status": "Watched",
            "title": "Deadpool",
            "rating": "8",
            "release_date": "10/02/2016",
            "review": "Great Film"
        }
    },
    {
        "model": "mywatchlist.watchlistitem",
        "pk": 9,
        "fields": {
            "status": "Watched",
            "title": "Deadpool 2" ,
            "rating": "8",
            "release_date": "15/05/2018",
            "review": "Great Film"
        }
    },
    {
        "model": "mywatchlist.watchlistitem",
        "pk": 10,
        "fields": {
            "status": "Not Watched",
            "title": "The Batman",
            "rating": "8",
            "release_date": "02/03/2022",
            "review": "Haven't watched it yet"
        }
    }
]
```
6. Jalankan perintah ```python manage.py loaddata initial_mywatchlist_data.json``` untuk memasukkan data ke dalam _database_ Django lokal.
7. Pada file ```views.py``` di folder ```mywatchlist``` tambahkan potongan kode sebagai berikut ini:
```python
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchListItem

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
```
8. Buat sebuaah file bernama ```mywatchlist.html``` pada folder ```template``` di ```mywatchlist``` dan tambahkan potong kode di bawah ini:
```
{% extends 'base.html' %}

 {% block content %}

  <h1>Tugas 3 PBP/PBD</h1>

  <h5>Name: </h5>
  <p>{{nama}}</p>

  <h5>Student ID: </h5>
  <p>{{student_id}}</p>

  <table>
    <tr>
      <th>Status</th>
      <th>Title</th>
      <th>Rating</th>
      <th>Release Date</th>
      <th>Review</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for item in list_watchlist %}
    <tr>
      <th>{{item.status}}</th>
      <th>{{item.title}}</th>
      <th>{{item.rating}}</th>
      <th>{{item.release_date}}</th>
      <th>{{item.review}}</th>
    </tr>
    {% endfor %}
  </table>

  {% if check_status %}
    <h1>Selamat, kamu sudah banyak menonton!</h1>
  {% else %}
    <h1>Wah, kamu masih sedikit menonton!</h1>
  {% endif %}

 {% endblock content %}
```
9. Pada file ```urls.py``` yang ada pada folder ```mywatchlist``` tambahkan kode berikut yang bertujuan untuk melakukan _routing_ terhadap fungsi ```views```yang telah dibuat tadi sehingga halama HTML dapat ditampilkan oleh browser :
```python
from django.urls import path
from mywatchlist.views import show_html, show_json, show_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('mywatchlist/html/',show_html, name='show_html'),
    path('mywatchlist/json/',show_json, name='show_json'),
    path('mywatchlist/xml/',show_xml, name='show_xml')
]
```
10. Daftarkan aplikasi ```mywatchlist``` ke dalam ```urls.py``` yang ada pada folder ```project_django``` dengan menambahkan potongan kode sebagai berikut di dalam variabel ```urlpatterns``` :
```python
...
path('mywatchlist/', include('mywatchlist.urls')),
...
```
11. Jalankan projek Django yang telah dibuat tadi dengan perintah ```python manage.py runserver``` dan bukalah http://localhost:8000/mywatchlist/html di browser untuk melihat halaman yang sudah dibuat tadi

## Postman
- HTML

![postman_html](https://user-images.githubusercontent.com/88818694/191653054-ffc4a4cc-78ac-4948-b469-61036507f675.jpg)

- JSON

![postman_json](https://user-images.githubusercontent.com/88818694/191653173-4f378d97-5cf8-47d6-bb52-a370324d9947.jpg)

- XML

![postman_xml](https://user-images.githubusercontent.com/88818694/191653250-e14ba6e8-4e10-4040-855d-8a6abc083190.jpg)

Link Heroku :

[Tugas3PBP-HTML](https://web-tugas2pbp-palinggg.herokuapp.com/mywatchlist/html/)

[Tugas3PBP-JSON](https://web-tugas2pbp-palinggg.herokuapp.com/mywatchlist/json/)

[Tugas3PBP-XML](https://web-tugas2pbp-palinggg.herokuapp.com/mywatchlist/xml/)
