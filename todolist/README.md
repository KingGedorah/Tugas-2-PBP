# Tugas 4 : Pengimplementasian Form dan Autentikasi Menggunakan Django

Link Aplikasi Heroku : [Tugas4PBP-todolist](https://web-tugas2pbp-palinggg.herokuapp.com/todolist/)

## Kegunaan `{% csrf_token %}` pada elemen `<form>`
CSRF (Cross-Site Request Forgery) token pada elemen `<form>` berguna untuk mencegah terjadinya serangan CSRF. Token ini dibuat dan dikirim oleh server side dalam permintaan HTTP berikutnya oleh client. Setelah request dibuat, server side akan membandingkan dua token yang ditemukan pada _user session_ dan pada request yang telah dibuat. Jikan token tersebut tidak sesuai dengan value yang ada pada user session, request yang telah dibuat tadi akan ditolak, user session akan dihapus dan kejadian tersebut ditandai sebagai kemungkinan `CSFR attack`.

## Apakah dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?
Bisa, dengan cara membuat elemen `<form>` dengan field yang sesuai dengan keinginan kita. Kita juga perlu menambahkan sebuah fungsi yang akan menerima data yang disubmit dengan POST request.

## Proses Alur Data dari Submisi yang dilakukan melalui HTML form
Ketika _user_ menekan tombol yang tipenya adalah submit maka browser akan merespons dan mengirimkan method POST request ke server. Method POST nantinya akan melakukan perubahan pada server / _database_ dan perubahan tersebut akan disimpan. Setelah dijalankan, user akan diarahkan kembali ke views yang sesuai dengan data yang sudah diupdate.

## Implementasi
1. Membuat project django baru dengna nama `todolist` dengan perintah `python manage.py startapp todolist`.
2. Menambahkan aplikasi `todolist` pada variabel `INSTALLED_APPS` yang berada di file `settings.py` pada folder `project_django`.
3. Membuat model pada file `models.py` dengan menambahkan potongan kode dibawah :
```python
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True,)
    date = models.DateField(auto_now=True)
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```
4. Melakukan perintah `python manage.py makemigrations` dan `python manage.py migrate`
5. Buat folder `fixtures` di dalam `todolist` dan buat file bernama `todolist.html` yang akan menjadi template home dari aplikasi `todolist` yang kita buat
6. Pada file `views.py` tambahkan function seperti dibawah ini :
```python
@login_required(login_url='/todolist/login/')
def show_todolist(request):
...

def register(request):
...

def login_user(request):
...

def logout_user(request):
...

@login_required(login_url='/todolist/login/')
def create_task(request):
...

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
...

@login_required(login_url='/todolist/login/')
def update_task(request, id):
...
```
7. Kemudian membuat file `login.html`, `register.html` dan `create_task.html` pada folder `fixtures` yang telah dibuat tadi untuk menjadi template html function yang ada di `views.py`
8. Buat file `urls.py` pada `todolist` dan tambahkan potongan kode di bawah untuk melakukan routing terhadap _function_ yang telah dibuat sebelumnya di file `views.py` :
```python
from django.urls import path
from todolist.views import update_task,delete_task, show_todolist, register, login_user, logout_user, create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist , name='show_todolist'),
    path('register/', register , name='register'),
    path('login/', login_user ,name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('create_task/', create_task, name='create_task'),
    path('delete/<int:id>/', delete_task , name='delete_task'),
    path('update/<int:id>/', update_task , name='update_task'),
]
```
9. Tambahkan aplikasi `todolist` pada `urls.py` yang ada pada folder `project_django` pada variabel `urlpatterns` seperti di bawah :
```
...
path('todolist/', include('todolist.urls')),
...
```
10. Lakukan perintah `add`, `commit`, dan `push` untuk melakukan deploy ke `Heroku`
