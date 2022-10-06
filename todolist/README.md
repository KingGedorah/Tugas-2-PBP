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

#

# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

Link Aplikasi Heroku : [Tugas5PBP-todolist](https://web-tugas2pbp-palinggg.herokuapp.com/todolist/)

## Perbedaan Inline, Internal, dan External CSS
- Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Contoh penggunaannya seperti :
    ```html
    <h1 style=" color: red">
        heading
    </h2>
    ```
- Internal CSS adalah kode CSS yang ditulis dalam `tag<style>` dan kode HTML yang ditulis di bagian header file HTML. Contoh penggunaannya seperti :
    ```html
    <h1>
        Heading
    </h1>
    <style>
        h1 {
            color : red
        }
    </style>
    ```
- External CSS adalah kode CSS yang ditulis terpisah dari kode HTML. External CSS di tulis di sebuah file dengan eksistensi `.css`. File CSS yang digunakan sebagai _styling_ biasanya diletakkan setelah bagian `<head>` di halaman. Contoh penggunaannya :
    ```html
    <link href="external.css" rel="styleshee">

    <h1>
        Heading
    </h1>
    ```

**Inline CSS**

**Kelebihan**
- Proses request HTTP yang kecil membuat proses loading website jadi lebih cepat. 

**Kekurangan**
- Tidak efisien karena hanya bisa diterapkan pada satu elemen saja

**Internal CSS**

**Kelebihan**
- Class dan ID bisa digunakan oleh internal stylesheet
- Tidak perlu mengupload file tambahan karena HTML dan CSS berada pada file yang sama

**Kekurangan**
- Performa web menjad lambat, karena CSS yang berbeda-beda dapat mengakibatkan loading ulang setiap berganti halaman website

**External CSS**

**Kelebihan**
- Ukuran halaman jadi lebih kecil dan Struktur HTML menjadi lebih rapi
- Loading website menjadi lebih cepat.

**Kekurangan**
- Ketika file CSS gagal dipanggil, tampilan webiste akan terlihat berantakan

## Tag pada HTML
- `<title>` : Untuk membuat suatu halaman
- `<h1>` to `<h6>` : Untuk membuat heading
- `<p>` : Untuk membuat paragraf
- `<div>` : Untuk membuat bagian dalam dokumen
- `<button>` : Untuk membuat button
- `<a>` : Untuk membuat hyperlink

## Tipe - tipe CSS Selector 
- Selektor Tag, memilih elemen berdasarkan tag.
- Selektor Class, memilih elemen berdasarkan nama class yang diberikan.
- Selektor ID,  memilih elemen berdasarkan ID. ID mirip dengan class tetapi ID bersifat unik.
- Selektor Atribut, memilih elemen berdasarkan atribut.
- Selektor Universal,  menyeleksi semua elemen pada jangkaua (scope) tertentu
- Selektor Pseudo, memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya.

## Implementasi
1. Menginclude bootstrap pada `base.html`
2. Menerapkan styling pada halama project todolist
3. Membuat navbar dan menerapkan card