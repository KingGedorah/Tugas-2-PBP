# **Tugas 2 PBP : Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django**

 > ###### Link menuju Heroku : https://web-tugas2pbp-palinggg.herokuapp.com/katalog/

## **Bagan _request client_ ke Web Berbasis Django**

<p align="center">
  <img src= "https://1.bp.blogspot.com/-u-n0WYPhc3o/X9nFtvNZB-I/AAAAAAAADrE/kD5gMaz4kNQIZyaUcaJJFVpDxdKrfoOwgCLcBGAsYHQ/s602/3.%2BPython%2BDjango%2B-%2BModul%2B2_Page2_Image5.jpg"/>
</p>

##### Pertama - tama client membuat request. Request tersebut akan diproses oleh `urls.py` yang kemudian _request_ tersebut akan memanggil fungsi yang sesuai yang ada pada di berkas `views.py`. Kemudian `views.py` menerima _request_ tersebut yang kemudian akan melakukan permintaan pada `models.py` jika terdapat suatu aktivitas yang membutuhkan database. Kemudian database tersebut diproses dan akan dikembalikan kepada `views.py`. `views.py` kemudian akan memilih `html` yang sesuai dari `template` dan kemudian membalikkan _request_ dari client dalam bentuk tampilan aplikasi web.

### **Kenapa menggunakan _virtual environment?_**
#### _Virtual environment_ merupakan sebuah _environment_ yang berguna untuk mengisolasi proyek django. _Virtual environment_ ibarat sebuah library khusus untuk proyek kita yang mana proyek django kita dapat berjalan tanpa mengganggu proyek lain yang ada di komputer kita. Namun, kita tetap dapat membuat proyek django tanpa menggunakan _virtual environment_ tetapi hal ini tidak disarankan.

### **Implementasi**
#### 
1.Membuat sebuah fungsi pada `views.py` sesuai dengan yang kita inginkan sebagai contoh :
```
def show_catalog(request):
  catalog_items = CatalogItem.objects.all()
  context = {
  'list_catalog' : catalog_items,
  'nama' : 'Naufal Zhafari Zahran',
  'student_id' : '2106752104'
  }
  return render(request, 'katalog.html', context)
```
2. Kemudian melakukan routing pada berkas `urls.py` pada katalog dan juga pada folder project_django
  - Menambahkan path pada urlspattern pada urls.py pada folder katalog sebagai contoh:
   ```
   path('katalog/', show_catalog, name='show_catalog')
   ```
  - Menambahkan path pada urlspattern pada urls.py pada folder project_django sebagai contoh:
   ```
   path('', include('katalog.urls'))
   ```
3. Kemudian melakukan _mapping_ ke file `html` dengan cara memanfaatkan variabel `context` yang ada pada _function_ `show_catalog`.

4. Kemudian lakukan `add`, `commit`, dan `push` terhadap file yang sudah dimodifikasi tadi
 
5. Membuat _repository secret_ dengan API key dari Heroku yang kita miliki dan juga nama aplikasi Heroku untuk melakukan _deploy_ 
