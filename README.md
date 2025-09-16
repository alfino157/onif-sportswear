# Tugas 2
Alfino Ahmad Feriza - 2406405304 - PBP C

URL PWS : https://alfino-ahmad-footballshop.pbp.cs.ui.ac.id/

## 1. Cara implementasi checklist tugas secara step by step
1. Membuat folder baru bernama onif-sportswear.
2. Membuat dan menjalankan virtual environment pada terminal directory tersebut dengan _**python -m venv env dan env\Scripts\activate**_.
3. Menambahkan beberapa dependencies yang diperlukan, seperti library, package, dan framework tertentu dengan membuat file requirements.txt dan mengisi dependencies yang dibutuhkan.
4. Menginstall dependencies tersebut dengan menjalankan _**pip install -r requirements.txt**_ pada terminal.
5. Membuat proyek django baru dengan menjalankan _**django-admin startproject onif_sportswear .**_ pada terminal.
6. Membuat file .env dan env.prod.  untuk konfigurasi deployment local (menggunakan database SQLite simple untuk testing) atau production deployment (menggunakan database PostgreSQL).
7. Memodifikasi file settings.py untuk menggunakan environment variables dari  .env yang telah dibuat.
8. Menambahkan "localhost" dan "127.0.0.1" pada list ALLOWED_HOST dalam settings.py untuk domain tempat kode dijalankan.
9. Menambahkan konfigurasi PRODUCTION dan memodifikasi kode DATABASES pada settings.py agar dapat switch antara menggunakan SQLite biasa ataupun production menggunakan PostgreSQL.
10. Menjalankan server dengan migrasi database models dengan perintah python manage.py migrate terlebih dahulu. Lalu, jalankan _**python manage.py runserver**_ untuk menjalankan server Django.
11. Membuat git repository baru dengan nama onif-sportswear, membuat file .gitignore untuk berkas-berkas yang perlu diabaikan oleh git, dan menghubungkannya dengan directory lokal yang sudah dibuat.
12. Membuat branch utama master lalu melakukan commit dan push pada github.
13. Membuat project baru pada website PWS dan mengganti environs pada project tersebut sesuai dengan .env.prod yang sudah dibuat pada directory lokal.
14. Menambahkan "alfino-ahmad-footballshop.pbp.cs.ui.ac.id" pada ALLOWED_HOST di settings.py untuk URL deployment website PWS.
15. Melakukan add, commit, dan push kepada git untuk menyimpan perubahan tersebut.
16. Menjalankan perintah pada informasi Project Command (_**git remote add PWS, git branch -M master, dan git push PWS master**_) untuk deployment website PWS.
17. Menjalankan _**git credential-cache exit**_ karena sempat gagal authentication untuk memunculkan popup window.
18. Menjalankan kembali perintah pada informasi Project Command dan memasukkan credentials username dan password dari website.
19. Membuat aplikasi baru bernama main dengan menjalankan perintah _**python manage.py startapp main**_ pada terminal.
20. Menambahkan aplikasi main tersebut pada proyek onif-sportswear dengan menambahkan elemen ‘main’ pada list INSTALLED_APPS di konfigrasui settings.py.
21. Membuat directory templates pada directory app main yang dibuat dan membuat berkas main.html dalam templates tersebut.
22. Mengisi file html tersebut dengan nama football shop, nama pribadi, NPM, dan kelas PBP.
23. Mengubah models.py dalam directory aplikasi main dengan membuat class Product beserta attributes-attributes seperti name(CharField), brand(CharField), description(TextField), category(CharField), Thumbnail(URLField), price(PositiveIntegerField), stock(PositiveIntegerField), dan is_featured(BooleanField).
24. Melakukan migration models atas perubahan model basis data yang dilakukan di atas dengan _**perintah python manage.py makemigrations**_ dan _**python manage.py migrate**_.
25. Menghubungkan views.py dan templates.py dengan mengimport fungsi render terlebih dahulu agar dapat memunculkan tampilan HTML (from django.shortcuts import render). Lalu, menambahkan fungsi show_main dengan parameter request. Fungsi tersebut juga dimofikasi dengan dictionary yang berisi NPM, nama, dan kelas serta akan mereturn render(request, "main.html", context) untuk rendering tampilan main.html sesuai dengan context dan request yang ada.
26. Memodifikasi nama, NPM, dan kelas pada templates.py dengan {{ npm }}, {{ name }}, dan {{ class }} untuk menampilkan sesuai dengan context yang dibuat pada views.
27. Mengkonfigurasi routing URL aplikasi dengan membuat urls.py terlebih dahulu pada directory aplikasi main.
28. Mengisi urls.py dengan import path dari django urls, import show_main dari main.views, variable app_name dengan string 'main', dan list urlpatterns yang berisi path('', show_main, name='show_main').
29. Mengkonfigurasi routing URL proyek agar dapat memetakan url aplikasi main dengan memodifikasi urls.py pada directory project dan impor fungsi include dari django.urls dengan from django.urls import path, include.
30. Menambahkan rute url path('', include('main.urls')), pada urlpatterns untuk rute aplikasi main.
31. Melakukan git add, commit, dan push kode ke github lalu melakukan push pws kembali untuk mengubah kode pada website PWS.

## 2. Bagan request client ke web aplikasi 
<img width="897" height="449" alt="Alur Request-Response Django" src="https://github.com/user-attachments/assets/3c4ffbcb-66a4-4d53-9ac6-2ccf0b41482c" />

Sumber : https://dev.to/_rohitshakya/django-the-request-response-cycle-2n6m

Bagan di atas menunjukkan alur request-response web aplikasi Django. Pada tahap pertama, ketika seorang client mengirim request, request tersebut akan terkirim kepada settings.py dan meload semua konfigurasi yang ada pada file tersebut, termasuk Middleware. Selanjutnya, pada tahap kedua, Middleware akan melakukan pengecekan seperti security check dan authentication. Apabila request terlihat aman, request tersebut kemudian menuju urls.py dan mencocokkan URL pola yang ada pada urls.py. Selanjutnya, apabila sudah cocok, pada tahap ketiga, request akan berlanjut ke file views.py yang bersesuaian. Dari tahap ini, apabila request membutuhkan informasi yang ada pada database, maka views.py akan mengakses database via models.py. Di sisi lain, templates juga akan dirender dari views.py dan apabila templatesnya tidak tersedia maka akan menampilkan page not found exception. Terakhir, response HTTP dari templates akhirnya dapat dirender dan ditampilkan pada web browser.


## 3. Peran settings.py dalam proyek Django
settings.py berperan sebagai file utama untuk melakukan konfigurasi proyek Django yang ingin kita buat.
Beberapa jenis konfigurasi yang dapat dilakukan adalah sebagai berikut.
- Security: SECRET_KEY, DEBUG, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS.
- Aplikasi: INSTALLED_APPS.
- Middleware : MIDDLEWARE.
- Template & static files: TEMPLATES['DIRS'], STATIC_URL, STATICFILES_DIRS, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT.
- Database: DATABASES (SQLite/PostgreSQL/MySQL)
- Internasionalisasi: LANGUAGE_CODE, TIME_ZONE, USE_TZ.
- Validasi password: AUTH_PASSWORD_VALIDATORS

Sebagai contoh, beberapa konfigurasi yang dilakukan pada pembuatan Django project football shop ini adalah dengan menambahkan string-string domain seperti 'localhost' pada ALLOWED_HOSTS ataupun menambahkan aplikasi yang dibuat seperti 'main' pada INSTALLED_APPS.

## 4. Cara kerja migrasi database di Django
Migrasi adalah proses atau instruksi yang perlu dijalankan untuk mengubah struktur database berdasarkan perubahan yang dibuat pada model yang didefinisikan pada kode terbaru kita.
Cara kerja migrasi model adalah sebagai berikut.
1. Memodifikasi models.py
2. Menjalankan perintah _**python manage.py makemigrations**_ pada terminal untuk membuat file migrasi, tetapi belum mengaplikasikan perubahannya pada database.
3. Menjalankan perintah _**python manage.py migrate**_ pada terminal untuk menerapkan migrasi tersebut ke dalam database. 

## 5. Alasan framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Menurut saya pribadi, framework Django cocok untuk dijadikan permulaan pembelajaran pengembangan perangkat lunak karena memakai struktur yang mudah dipahami, yaitu memakai konsep MVT (Model, View, Template). Bagi saya, struktur tersebut membantu dalam pembuatan kode yang lebih readable, modular, dan juga scalable untuk projek atau aplikasi yang akan dibuat kedepannya. Selain struktur MVT tersebut, alasan lain adalah mungkin karena Django juga memakai bahasa pemrograman Python yang memiliki sintaks yang lebih mudah dipahami dan juga lebih familiar karena kita sudah pernah menggunakannya pada mata kuliah DDP 1. 

## 6. Feedback untuk asisten dosen
Peran asisten dosen saat tutorial 1 sudah sangat bagus dalam membantu pengerjaan tutorial dengan adanya help center di VC discord. File tutorial pada web PBP juga mudah dipahami dan disertai penjelasan yang mendukung.

# Tugas 3 

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery dalam mengimplementasikan sebuah platform karena data delivery adalah konsep pemindahan data dari satu stack ke stack lainnya. Dalam hal ini, ketika kita sedang mengembangkan sebuah aplikasi web dan ingin mengirimkan suatu data dari backend ke frontend, data tersebut harus dikemas dalam format tertentu agar bisa dipahami. Beberapa contoh markup language yang biasa digunakan adalah HTML, XML, ataupun JSON.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya pribadi, secara visual, kode XML umumnya lebih rumit dan sulit dibaca dibandingkan markup language JSON. XML umumnya banyak menggunakan tag pembuka dan penutup '< >' sehingga filenya lebih panjang dan terkadang sulit dibaca dibandingkan JSON yang tidak menggunakan tag tersebut. Ditambah lagi, dengan banyak web yang menggunakan Javascripts, JSON lebih praktis untuk digunakan karena bisa langsung dipakai tanpa perlu parsing seperti XML. Dengan demikian, secara tidak langusung, JSON lebih populer digunakan dibandingkan XML karena lebih ringkas, mudah dibaca, dan bisa langsung dipakai pada Javascripts tanpa perlu parsing khusus.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
method is_valid() pada form Django berfungsi sebagai method yang memvalidasi input form yang dimasukkan oleh pengguna, contohnya seperti angka negatif pada field bilangan bulat ataupun panjang teks yang tidak sesuai. Method ini sangat penting untuk diimplementasikan karena jika ada input pada forms yang tidak valid, maka database dapat error karena telah memasukkan data yang tidak tervalidasi. Dari segi keamanan juga, input forms yang tidak tervalidasi dapat terancam oleh SQLinjection jika tidak ditangani dengan baik.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token sangat penting dan dibutuhkan dalam pembuatan form di Django agar server web yang kita gunakan dapat memvalidasi dan memastikan request form yang ada itu benar benar datang dari halaman web kita bukan dari situs yang berbahaya. Contohnya, ketika kita sedang mengakses situs web yang jahat, situs tersebut bisa saja mengirimkan request ke form pada web lainnya yang sedang kita gunakan. Hal ini bisa mengancam data kita dalam situs web tersebut dan bisa saja melakukan tindakan yang menghapus ataupun mengambil kepemilikan pribadi kita. Dengan adanya csrf_token, ketika kita mengakses form pada web, web akan membuat token unik yang hanya bisa diakses oleh web kita. Dengan demikian, penyerang tidak bisa sembarangan membuat request palsu pada form di website tersebut dan data kita akan aman dari serangan tersebut.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat berkas html bernama base.html pada root folder onif-sportswear sebagai template untuk kode html yang digunakan selanjutnya
2. Mengupdate bagian DIRS pada settings.py agar dapat mendeteksi base.html sebagai template html yang digunakan pada project
3. Mengupdate main.html pada directory main agar menyesuaikan base.html yang dibuat
4. Membuat berkas forms.py pada directory main untuk struktur form yang dapat menerima data Products yang baru dengan ketentuan sebagai berikut. Mengimport ModelForm dari django.forms dan Product pada main.models, Mmebuat class ProductForm dengan parameter Modelform dan sub class Meta dengan attributes variabel model = Products dan list fields sesuai field yang ada pada models.
5. Membuat fungsi create_product dengan parameter request, lalu membuat varible form baru dengan NewsForm(request.POST or None), lalu memvalidasi isi form tersebut dan redirect ke fungsi 'show_main' jika valid. Default fungsi akan melakukan render terhadap tampilan create_product html dan context sesuai form yang diisi.
6. Membuat fungsi show_product dengan parameter request dan id, lalu membuat variable product dengan get_object_or_404(Product, pk=id). Fungsi akan return render tampilan product_detail.html sesuai context product dengan return render(request, "product_detail.html", context)
7. Mengimport create_product dan show_product pada urls.py
8. Menambahkan urlpatterns baru berdasarkan fungsi baru views.py yang telah dibuat pada urls.py directory main
9. Memodifikasi main.html dengan <button>+ Add Product</button> untuk menampilkan button Add product pada web, if conditionals untuk melihat product_list ada atau tidak dan menampilkan "Belum ada product pada Onif Sportswear." apabila tidak ada. (Tampilan halaman main)
10. Menambahkan tampilan semua product pada product_list dan menambahkan tampilan product name, category, featured atau tidak, thumbnail, brand, price, dan stocknya jika product_list ada.
11. Membuat file create_product.html dengan {% csrf_token %} sebagai security dan juga {{ form.as_table }} sebagai template tag yang menampilkan fields model pada forms.py sebagai sebuah table. (Tampilan halaman form)
12. Membuat file product_detail.html sebagai tampilan halaman detail yang menampilkan nama produk, category, featured atau tidak, thumbnail, brand, price, stock, dan descriptionnya
13. Memodifikasi settings.py pada root project onif-sportswear dan menambahkan list CSRF_TRUSTED_ORIGINS dengan isi web pws "https://alfino-ahmad-footballshop.pbp.cs.ui.ac.id/"
14. Menambahkan import HttpResponse dan Serialzers pada views.py directory main
15. Membuat fungsi show_xml dengan parameter request yang melakukan parsing objects model dengan serializers menjadi xml dan mereturn httresponse dengan data xml tersebut serta content_type "application/xml"
16. Membuat fungsi show_json dengan parameter request yang melakukan parsing objects model dengan serializers menjadi json dan mereturn httresponse dengan data json tersebut serta content_type "application/json"
17. Mengimport fungsi show_xml dan show_json pada main.views
18. Menambahkan path url ke dalam url patterns untuk mengakses fungsi show_xml dan show_json tersebut
19. Menambahkan fungsi show_xml_by_id pada views.py dengan parameter request, variabel product_item = Product.objects.filter(pk=product_id) untuk menyimpan hasil query dari data dengan id tertentu pada models, dan melakukan parsing objects model dengan serializers menjadi xml. Fungsi mereturn httresponse dengan data xml tersebut serta content_type "application/xml"
20. Menambahkan fungsi show_json_by_id pada views.py dengan parameter request, variabel product_item = Product.objects.filter(pk=product_id) untuk menyimpan hasil query dari data dengan id tertentu pada models, dan melakukan parsing objects model dengan serializers menjadi json. Fungsi mereturn httresponse dengan data json tersebut serta content_type "application/json"
21. Memodifikasi show_json_by_id dan show_xml_by_id dengan menambahkan try except pada fungsi sehingga jika data tidak ditemukan akan mereturn httpresponse dengan status 404.
22. Mengimport kedua fungsi show_json_by_id dan show_xml_by_id pada urls.py
23. Menambahkan path url dalam urlpatters di urls.py untuk menampilkan kedua fungsi

## Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Dari segi materi, materi yang ada pada tutorial 2 PBP sudah sangat membantu dalam pengerjaan tugas ini. Mungkin menurut saya pribadi, tutorial kurang memberi tahu kita mengenai syntax-syntax dan penjelasan mengenai file html secara dasar sehingga kita harus belajar dari luar untuk penggunaan kode html. Postman juga tidak dijelaskan fungsi dan kegunannya apa. Dari segi ketersedian asdos pada sesi tutorial, menurut saya sudah sangat baik karena meskipun online, pada asdos tetap standby pada VC dan discord dan membantu mahasiswa yang membutuhkan. :D

## Screenshot hasil Postman
<img width="1911" height="887" alt="image" src="https://github.com/user-attachments/assets/09037d74-e725-4f3e-94f0-d2416c3d8360" />
<img width="1910" height="920" alt="image" src="https://github.com/user-attachments/assets/1b6cd22a-62fe-48d5-bb79-6d5903b4a208" />
<img width="1920" height="922" alt="image" src="https://github.com/user-attachments/assets/ba8c49a3-4c06-4940-b76f-13c5d99cd27b" />
<img width="1914" height="925" alt="image" src="https://github.com/user-attachments/assets/e59137f3-9525-4c7c-b7e6-a2de0eb58582" />








