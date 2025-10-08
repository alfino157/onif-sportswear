Alfino Ahmad Feriza - 2406405304 - PBP C

URL PWS : https://alfino-ahmad-footballshop.pbp.cs.ui.ac.id/

<details>
  <summary> Tugas 2 </summary>

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

</details>



<details> 
<summary> Tugas 3 </summary>

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
5. Membuat fungsi create_product dengan parameter request, lalu membuat varible form baru dengan productForm(request.POST or None), lalu memvalidasi isi form tersebut dan redirect ke fungsi 'show_main' jika valid. Default fungsi akan melakukan render terhadap tampilan create_product html dan context sesuai form yang diisi.
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

</details>
<details>
<summary> Tugas 3 </summary>

## Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django AuthenticationForm adalah form bawaan dari Django yang dapat kita import melalui django.contrib.auth.forms dan digunakan sebagai form untuk autentikasi login pengguna. Form ini memiliki 2 field input yaitu username dan password. Kelebihan dari Django AuthenticationForm adalah form ini langsung siap pakai sehingga kita tidak perlu susah-susah membuat form login sendiri dan tinggal import dari Django. Selain itu, AuthenticationForm juga sudah memiliki tingkat keamanan awal yang baik sehingga autentikasi pengguna dapat berjalan secara aman, seperti fitur password hashing dan validasi. Namun, kelemahan dari AuthenticationForm adalah form ini memiliki fitur yang sangat basic dan minimal, cuman ada username dan password, tidak ada fitur captcha ataupun 2 factor authentication yang diimplementasikan. Form ini juga hanya khusus digunakan untuk login sehingga fitur lain seperti register perlu diimplementasikan di form yang berbeda. Terakhir, Django AuthenticationForm juga memiliki tampilan yang mendasar sehingga terlihat kurang menarik jika tidak dimodifikasi.

## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah proses memastikan atau memverifikasi identitas pengguna yang sesuai, contohnya penggunaan login dengan username dan password yang sesuai. Sementara itu, otorisasi adalah proses memverifikasi hak akses pengguna yang sudah tervalidasi, contohnya pengguna biasa tidak bisa mengakses halaman admin karena dia bukan seorang admin. 

Dalam Django sendiri, autentikasi dan otorisasi berjalan beriringan melalui sistem bawaan django.contrib.auth. Autentikasi digunakan untuk memastikan identitas pengguna, misalnya saat login dengan username dan password, lalu Django menyimpannya di session sehingga setiap request berikutnya bisa mengenali siapa pengguna melalui request.user. Setelah identitas jelas, barulah otorisasi bekerja untuk menentukan apa saja yang boleh dilakukan pengguna tersebut. Django menyediakan mekanisme izin (permissions) dan grup untuk mengatur hak akses, misalnya hanya admin yang boleh menghapus data atau hanya user tertentu yang bisa membuka halaman khusus. Penerapan otorisasi ini bisa dilakukan langsung di view dengan decorator seperti @login_required atau @permission_required. Dengan cara ini, Django tidak hanya memastikan siapa pengguna, tetapi juga membatasi tindakan mereka sesuai peran dan hak akses yang diberikan.

## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Dalam sebuah aplikasi web, session dan cookies sama-sama dipakai untuk menyimpan state yaitu informasi agar server bisa mengingat pengguna. Meskipun demikian, keduanya memilki kelebihan dan kekurangan masing-masing.

Session disimpan di server (contohnya di database, cache, atau file), sementara browser hanya menyimpan ID session dalam cookie. Kelebihannya, data lebih aman karena detailnya tidak ada di sisi client, kapasitas penyimpanan lebih besar, dan mudah dihapus atau dikontrol server. Kekurangannya, session membebani server karena butuh ruang simpan dan manajemen tambahan kalau tidak diatur dengan baik, bisa bikin server yang digunakan boros memori.

Cookies disimpan langsung di browser pengguna. Kelebihannya, tidak membebani server, sederhana, dan bisa dipakai lintas request atau bahkan lintas kunjungan (selama cookie belum expired). Kekurangannya, kapasitas penyimpanan kecil (umumnya maksimal 4 KB per cookie), mudah dilihat atau dimanipulasi oleh client jika tidak dienkripsi dengan baik, serta rawan disalahgunakan untuk tracking.

Kesimpulannya, session lebih aman dan cocok untuk data sensitif seperti login, sedangkan cookies lebih ringan dan praktis untuk preferensi pengguna seperti theme atau bahasa yang digunakan

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Secara default, penggunaan cookies dalam pengembangan web tidak sepenuhnya aman, karena ada beberapa risiko potensial yang harus diwaspadai. Misalnya, cookie bisa dicuri lewat session hijacking, dimanipulasi di sisi client, terekspos lewat XSS (Cross-Site Scripting), atau disalahgunakan dalam serangan CSRF (Cross-Site Request Forgery). Django menangani hal ini dengan sejumlah mekanisme keamanan bawaan. Secara standar, cookie session Django diberi atribut HttpOnly, sehingga tidak bisa diakses melalui JavaScript. Django juga menyediakan opsi SESSION_COOKIE_SECURE, agar cookie hanya dikirim melalui HTTPS, serta SESSION_COOKIE_SAMESITE untuk membatasi pengiriman cookie lintas situs. Terakhir, Django juga memiliki csrf token yang dapat diimplementasikan pada kode project kita sehingga cyber attack seperti CSRF dapat terhindarkan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Mengimport UserCreationForm dari  django.contrib.auth.forms dan messages dari django.contrib pada views.py yang digunakan untuk form register nanti
2. Menambahkan fungsi register pada vies.py dan membuat form baru dengan UserCreationForm(). Lalu, memvalidasi form dengan form.is_valid() apabila request "POST" dan ngesave form tersebut dengan form.save(). Fungsi dirender dengan context form dan tampilan register.html.
3. Membuat berkas register.html untuk tampilan registernya dengan csrf_token agar aman dari serangan (pada directory templates dalam main)
4. Menghubungkan fungsi register tersebut pada urls.py dengan mengimport fungsinya dan membuat path baru 'register/' dengan nama register
5. Mengimport AuthenticationForm, authenticate, dan login pada views.py untuk login pengguna
6. Menambahkan fungsi login_user yang membuat form dengan AuthenticationForm dan memvalidasi form dengan form.is_valid() apabila request "POST". Lalu menambahkan login(request, user) untuk login user. Fungis dirender dengan context form dan tampilan login.html.
7. Membuat berkas login.html pada directory templates dalam main untuk tampilan login
8. Menghubungkan fungsi login tersebut pada urls.py dengan mengimport fungsi login_user dari views dan membuat path baru 'login/' dengan nama login
9. Mengimport logout dari django.contrib.auth pada views.py
10. Membuat fungsi logout pada views.py dengan logout(request) dan return redirect ke tampilan main
11. Membuat button 'Logout' baru pada halaman main 
12. Menghubungkan fungsi logout tersebut pada urls.py dengan mengimport fungsi logout dari views dan membuat path baru 'logout/' dengan nama logout
13. Mengimport login_required dari django.contrib.auth.decorators dan menambahkan @login_required(login_url='/login') pada fungsi show_main dan create_product agar pengguna perlu autentikasi terlebih dahulu sebelum mengakses halaman tersebut
14. Mengimport HttpResponseRedirect, reverse, dan datetime pada views.py
15. Memodifikasi fungsi login_user pada bagian form.is_valid() dengan response = HttpResponseRedirect(reverse("main:show_main")) untuk balik ke tampilan utama dan juga response.set_cookie('last_login', str(datetime.datetime.now()) untuk cookie last login pengguna
16. Menambahkan context baru pada fungsi show_main di views.py dengan 'last_login': request.COOKIES['last_login'] agar dapat ngeshow di tampilan main
17. Memodifikasi fungsi logout pada views.py dengan menambahkan  response = HttpResponseRedirect(reverse('main:login')) dan response.delete_cookie('last_login') untuk redirect ke halaman login lagi jika logout dan ngedelete cookie last login yang ada
18. Menambahkan header baru pada main.html yang menampilkan sesi terakhir login dengan {{last_login}}
19. Mengimport User dari django.contrib.auth.models pada models.py
20. Menambahkan field baru pada class Product yaitu user dengan models.ForeignKey(User, on_delete=models.CASCADE, null=True) untuk menghubungkan user dengan model product
21. Melakukan migrasi dengan makemigrations dan migrate agar perubahan dapat tersimpan di database
22. Memodifikasi fungsi create_product di views.py pada bagian if form.is_valid() dengan menambahkan product_entry = form.save(commit = False) agar productnya tidak langsung menyimpan objek hasil form ke database. Lalu,  menambahkan product_entry.user = request.user untuk user yang sedang login dan ngesave product_entry tersebut dengan .save().
23. Memodifikasi fungsi show_main di views.py dengan membuat filter terlebih dahulu filter_type = request.GET.get("filter", "all"). Lalu menambahkan if conditionals (apabila filternya "all" maka akan menampilkan semua product dengan Product.objects.all() dan else maka akan menampilkan product si pengguna yang sedang login itu dengan Product.objects.filter(user=request.user)).
24. Memodifikasi tampilan main.html dengan menambahkan button 'All products' dengan href = ?filter=all untuk menampilkan semua product dan juga buttonn 'My products' dengan href = ref="?filter=my" untuk menampilkan product user yang sedang login.
25. Memodifikasi product_detail.html dengan menambahkan nama penjual dengan {{product.user.username}} apabila dibuat oleh user dan Anonymous apabila tidak dibuat oleh user (sebelum implementasi login).
26. Memodifikasi main.html dengan menambahkan <p> Selamat datang, <b> {{ user.username }}</b>! </p> untuk informasi nama user yang sedang login
27. Membuat 3 account baru yaitu test101, alfino101, dan alfino67 dan menambahkan 3 product baru pada masing masing account.
28. Melakukan add commit dan push ke github dan juga PWS
    
</details>

# Tugas 4

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Dalam CSS, apabila suatu elemen HTML dipengaruhi oleh lebih dari satu aturan style, browser akan menentukan aturan mana yang diterapkan melalui mekanisme prioritas yang disebut _specificity_. Urutan prioritas dimulai dari deklarasi !important, karena aturan ini akan selalu mengesampingkan aturan lainnya, kecuali terdapat deklarasi !important lain dengan tingkat specificity yang lebih tinggi. Setelah itu, prioritas berikutnya ditempati oleh inline style, yaitu aturan yang ditulis langsung pada atribut style dalam elemen HTML.

Di bawah inline style, ID selector memiliki tingkat specificity yang tinggi karena umumnya digunakan untuk menargetkan elemen yang bersifat unik. Selanjutnya, class selector, attribute selector, dan pseudo-class berada pada tingkat prioritas berikutnya. Sementara itu, element selector (seperti p, h1) serta pseudo-element (misalnya ::before, ::after) memiliki prioritas yang paling rendah.

Apabila dua aturan memiliki tingkat specificity yang sama, maka aturan yang ditulis terakhir dalam file CSS akan digunakan. Dengan demikian, semakin spesifik sebuah selector, semakin besar kemungkinan aturan tersebut diterapkan pada elemen dibandingkan dengan selector lain yang lebih umum

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design memiliki peran yang sangat penting dalam pengembangan aplikasi web karena memastikan tampilan dapat diakses dengan baik pada berbagai perangkat, mulai dari smartphone, tablet, hingga desktop. Tanpa adanya pendekatan ini, sebuah situs dapat mengalami permasalahan tampilan pada ukuran layar tertentu, seperti teks yang terlalu kecil untuk dibaca atau tombol yang sulit disentuh. Kondisi tersebut tidak hanya menurunkan kualitas user experience (UX) dan membuat pengunjung cepat meninggalkan situs, tetapi juga dapat memengaruhi peringkat pencarian di Google yang saat ini mengutamakan desain ramah mobile.

Salah satu contoh implementasi responsive design yang berhasil adalah YouTube. Platform ini secara cerdas menyesuaikan tata letak sesuai ukuran layar pengguna. Pada perangkat desktop, YouTube menampilkan grid multi-kolom dengan navigasi lengkap di sisi kiri. Ketika diakses melalui tablet, jumlah kolom dikurangi agar tetap nyaman dilihat, sementara menu utama dipindahkan ke bagian bawah layar untuk memudahkan akses, meskipun fitur navigasinya tidak selengkap versi desktop. Pada smartphone, tampilannya lebih sederhana dengan hanya satu kolom vertikal yang mudah digulir, serta menu utama tetap ditempatkan di bagian bawah layar. Dengan strategi ini, YouTube berhasil menghadirkan pengalaman pengguna yang konsisten dan optimal bagi miliaran penggunanya, terlepas dari perangkat yang digunakan.

Sebaliknya, SIAK-NG milik Universitas Indonesia dapat dijadikan contoh aplikasi yang belum mendukung responsive design dengan baik. Tampilan sistem ini masih mengandalkan tata letak statis (fixed layout) yang hanya sesuai untuk layar desktop. Saat diakses melalui smartphone, halaman situs hanya mengecil secara proporsional sehingga teks tampak sangat kecil dan sulit dibaca tanpa melakukan zoom. Pengguna juga terpaksa menggulir layar secara horizontal untuk melihat keseluruhan konten, sementara tombol navigasi menjadi sulit ditekan dengan akurat. Hal ini menunjukkan bahwa desain SIAK-NG masih mengabaikan kebutuhan pengguna mobile, sehingga menurunkan kenyamanan dan aksesibilitas informasi bagi sebagian besar audiens.

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Perbedaan utama antara margin, border, dan padding terletak pada posisi serta fungsinya dalam sebuah elemen. Margin berada di bagian paling luar, berfungsi sebagai ruang transparan untuk memberikan jarak antara satu elemen dengan elemen lain di sekitarnya. Lebih ke dalam, terdapat border, yaitu garis tepi yang membingkai elemen dan memisahkannya dari area luar. Sementara itu, di sisi dalam sebelum konten, terdapat padding, yakni ruang antara border dan konten yang berfungsi memberi jarak internal sehingga konten tidak menempel langsung pada tepi elemen.

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dan CSS Grid Layout merupakan dua sistem tata letak modern dalam CSS yang berbeda dari segi dimensi pengaturan elemen. Flexbox berfokus pada satu dimensi saja, baik baris (row) maupun kolom (column). Oleh karena itu, flexbox sangat ideal digunakan untuk menyusun elemen-elemen yang berjajar searah, misalnya menu navigasi, daftar produk, atau tombol yang perlu disejajarkan. Melalui flexbox, developer dapat dengan mudah mengatur perataan elemen, distribusi ruang kosong, serta fleksibilitas ukuran agar menyesuaikan dengan lebar atau tinggi layar.

Sebaliknya, CSS Grid Layout dirancang untuk tata letak dua dimensi, sehingga mampu mengatur elemen sekaligus dalam baris dan kolom. Grid lebih sesuai digunakan pada struktur halaman web yang kompleks, misalnya tata letak dengan header, sidebar, konten utama, dan footer. Grid memberikan kontrol penuh terhadap ukuran baris dan kolom, posisi setiap elemen, serta mendukung desain yang responsif.

Dengan demikian, dalam penggunannya, flexbox lebih tepat dimanfaatkan untuk menyusun elemen sederhana yang berjalan searah, sedangkan grid digunakan untuk mengelola layout halaman yang lebih kompleks dan terstruktur.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. Menambahkan tailwind ke aplikasi Django agar sytyling css lebih mudah dan menarik dengan <script src="https://cdn.tailwindcss.com"> pada base.html
2. Menambahkan fungsi edit_product pada views.py yang akan mencari product dengan get_object_or_404(product, pk=id) dan membuat form berdasarkan instance product tersebut
3. Membuat file edit_product.html pada templates main untuk menampilkan tampilan form tersebut
4. Menghubungkan fungsi edit_product pada urls.py dengan path 'product/<uuid:id>/edit'
5. Memodifikasi main.html pada templates dan menambahkan button Edit dengan href="{% url 'main:edit_product' product.pk %}"
6. Menambahkan fungsi delete_product yang akan mencari product berdasarkan id dengan get_object_or_404(product, pk=id) dan mendelete product tersebut dengan product.delete()
7. Menghubungkan fungsi edit_product pada urls.py dengan path 'news/<uuid:id>/delete'
8. Memodifikasi main.html pada templates main dan menambahkan button Delete
9. Membuat nvabar.html pada root directory templates yang nantinya akan dimodifikasi dengan css tailwind
10. menambahkan {% include 'navbar.html' %} pada main.html untuk menginclude navigation bar tersebut
11. Memodifikasi settings.py dengan menambahkan 'whitenoise.middleware.WhiteNoiseMiddleware' pada list Middleware agar Django dapat mengelola file statis secara otomatis
12. Mengkonfigurasi STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL pada settings.py berdasarkan mode DEBUG atau tidak
13. Membuat folder baru static pada root directory dan menambahkan folder css di dalamnya dan menambahkan file global.css
14. Menghubungkan global.css ke base.html dengan menambahkan <link rel="stylesheet" href="{% static 'css/global.css' %}"/> pada base.html
15. Menambahkan custom styling pada global.css yang momodifikasi style pada form yang dibuat untuk edit atau create product
16. Memodifikasi navbar.html dengan membuat nav wrapper yang menempel di atas halaman (fixed top-0 w-full z-50) dengan latar putih semi-transparan (bg-white/80) plus blur (backdrop-blur-sm), garis bawah halus, dan bayangan ringan agar modern dan tetap terbaca saat scroll. Di dalamnya ada container terpusat (max-w-7xl mx-auto px-6 lg:px-8) berbaris fleksibel (flex items-center justify-between h-16) untuk tiga section: logo/brand (judul tebal dengan aksen warna), menu desktop (link Home, Apparels, Shoes, Others, Create Product—ditautkan via {% url %}—ditampilkan hanya ≥ md dengan hidden md:flex dan gaya teks abu + hover gelap transition-colors), serta user section (menampilkan nama/NPM/kelas saat login beserta tombol Logout bentuk pill merah, atau Login/Register saat belum login). Untuk mobile, kita tambahkan tombol hamburger (md:hidden) yang menampilkan panel menu tersembunyi berisi link yang sama seperti desktop. interaksinya sederhana dengan JS yang toggle kelas hidden. Secara keseluruhan, gaya mengutamakan tipografi tegas, spacing rapi, kontras abu–hitam dengan aksen ungu/merah/hijau, responsif melalui utilitas Tailwind (hidden md:flex, padding responsif), dan transisi halus saat hover untuk pengalaman yang konsisten di berbagai ukuran layar.
17. Menambahkan card_product.html pada directory templates main. komponen dibungkus dengan <article> bergaya kotak putih (bg-white) berbingkai tipis (border border-gray-200), sudut melengkung (rounded-xl), dan diberi efek transisi saat hover (hover:-translate-y-1 hover:shadow-xl) sehingga terasa interaktif. Bagian atas berisi thumbnail dengan rasio 4:5. jika ada gambar produk ditampilkan penuh dengan efek zoom (group-hover:scale-110), jika tidak ada diganti blok abu dengan teks No Image. Di sudut kiri atas ditambahkan badge kategori hitam semi-transparan (bg-black/80 text-white uppercase). Bagian isi (p-5) menampilkan nama produk sebagai judul link dengan efek hover ungu, diikuti harga dan stok dengan teks abu lebih gelap. Di bagian bawah setelah garis tipis (border-t) terdapat aksi berupa tombol: View Product (utama, border ungu dengan efek hover jadi ungu penuh), serta bila pemilik login akan muncul Edit (abu dengan hover gelap) dan Delete (merah dengan hover merah solid). Secara keseluruhan, desain kartu bersih, responsif, modern, dengan interaksi hover yang jelas membedakan tiap aksi.
18. Memodifikasi halaman utama (main.html): struktur dimulai dengan extends base.html dan menyertakan navbar agar konsisten di semua halaman. Bagian utama dibungkus div berwarna abu terang (bg-gray-50) dengan padding atas (pt-16) supaya konten tidak menabrak navbar, serta lebar maksimum tengah (max-w-7xl mx-auto). Di dalamnya terdapat header section dengan judul besar tebal (text-3xl font-bold text-gray-900) dan subteks abu. Selanjutnya ada filter section dalam kotak putih (bg-white rounded-lg border p-4) yang berisi tombol untuk menampilkan All Product atau My Product dengan gaya berbeda tergantung kondisi filter aktif, serta tambahan teks “Last login” untuk pengguna yang login. Setelah itu, isi halaman menampilkan grid produk. jika tidak ada produk, ditampilkan kartu kosong dengan ilustrasi gambar default, teks keterangan, dan tombol hijau Create product. Jika ada produk, setiap item ditampilkan dalam grid responsif (grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6) menggunakan komponen card_product.html. Secara keseluruhan tampilannya bersih, responsif, dengan hierarki jelas: judul → filter → daftar produk.
19. Memodifikasi halaman login (login.html): tampilan dibungkus penuh layar dengan latar abu terang (bg-gray-50 min-h-screen flex items-center justify-center) agar form berada di tengah. Kotak form dibuat sederhana dan modern (bg-white rounded-lg border border-gray-200 p-6 sm:p-8 form-style) dengan judul “Sign In” serta subteks sambutan di bagian atas. Selanjutnya ada penanganan error: jika terjadi error umum atau error per field, pesan akan ditampilkan dalam kotak merah lembut (bg-red-50 border-red-200 text-red-700). Form terdiri dari input Username dan Password, masing-masing diberi padding, border abu, serta efek fokus berwarna hijau (focus:border-green-500). Tombol login ditampilkan penuh lebar, berwarna hijau solid dengan hover lebih gelap (bg-green-600 hover:bg-green-700). Setelah form, jika ada messages (misalnya berhasil login atau error), akan ditampilkan dalam kotak dengan warna berbeda sesuai tipe pesan (hijau untuk sukses, merah untuk error, abu untuk info). Di bagian paling bawah terdapat link untuk registrasi, ditulis ringan dengan teks kecil dan tautan hijau.
20. Memodifikasi halaman register (register.html): tampilan dibungkus penuh layar dengan latar abu terang (bg-gray-50 min-h-screen flex items-center justify-center) agar form registrasi berada di tengah. Kotak utama dibuat putih dengan border tipis dan bayangan halus (bg-white border rounded-lg shadow-sm) berisi judul “Join Us” serta subteks abu sebagai pengantar. Jika ada error dari form, akan muncul pesan dalam kotak merah lembut (bg-red-50 border-red-200 text-red-700) baik untuk error umum maupun error per field. Form terdiri dari input Username, Password, dan Confirm Password, masing-masing diberi padding, border abu, serta efek fokus hijau (focus:border-green-500). Tombol registrasi penuh lebar, berwarna hijau dengan efek hover dan fokus (bg-green-600 hover:bg-green-700 focus:ring-green-500). Jika ada pesan (success/error/info), ditampilkan dalam kotak warna berbeda sesuai status. Di bagian bawah terdapat teks kecil dengan tautan menuju halaman login. Secara keseluruhan, desain register bersih, simpel, modern, responsif, dengan fokus pada aksesibilitas dan pengalaman pengguna.
21. Memodifikasi halaman detail produk (show_product.html): halaman ini dibungkus dengan latar abu terang (bg-gray-50 min-h-screen py-10) dan konten difokuskan di tengah (max-w-5xl mx-auto). Bagian atas terdapat tombol navigasi sederhana “Back to Products” dengan teks abu yang berubah lebih gelap saat hover. Konten utama berupa kartu putih (bg-white rounded-xl shadow-md border border-gray-100) dengan bayangan lembut. Di bagian atas kartu ditampilkan badge kategori dengan gaya bulat kecil (px-3 py-1 rounded-full bg-gray-100 text-gray-800 uppercase). Jika produk memiliki gambar, ditampilkan penuh dengan sudut membulat (rounded-lg), tinggi proporsional (h-72 sm:h-96), dan efek zoom saat hover (hover:scale-105). Bagian isi diatur berurutan dengan spasi antar elemen (space-y-4): nama produk sebagai judul besar tebal (text-2xl sm:text-3xl font-bold), brand bila tersedia, harga dengan teks tebal abu, stok, serta deskripsi dengan teks abu lebih lembut. Secara keseluruhan, halaman detail ini bersih, terstruktur, dan responsif dengan urutan informasi jelas: kategori → gambar → nama → brand → harga → stok → deskripsi.
22. Memodifikasi halaman create product (create_product.html): halaman dibuat dengan latar abu terang (bg-gray-50 min-h-screen) dan konten dipusatkan di tengah (max-w-3xl mx-auto). Bagian atas berisi tombol kembali “Back to our Products” dengan teks abu yang berubah lebih gelap saat hover. Kotak form utama menggunakan kartu putih (bg-white rounded-lg border border-gray-200 p-6 sm:p-8 form-style) dengan judul “Create New Product”. Formulir menggunakan loop untuk menampilkan setiap field dengan label kecil (text-sm font-medium text-gray-700), input penuh lebar (w-full), serta pesan bantuan (text-sm text-gray-500) atau error (text-sm text-red-600) bila ada. Di bagian bawah form terdapat dua tombol aksi: Cancel berupa tombol abu dengan border (border border-gray-300 text-gray-700 hover:bg-gray-50) dan Add Product berupa tombol utama hijau penuh lebar (bg-green-600 hover:bg-green-700 text-white). Secara keseluruhan, desain bersih, terstruktur, responsif, dan memudahkan pengguna untuk menambahkan produk baru dengan pengalaman input yang rapi.
23. Menambahkan halaman edit product yang tampilannya kurang lebih sama dengan create_product.html bedanya judulnya adalah edit product dan formnya sudah difilter berdasarkan id yang ingin di edit sehingga formnya nanti sudah ada inputan dan bisa diganti. Mengganti buttonnya menjadi 'Update Product'.
24. Menambahkan fungsi product_list_by_category dengan parameter category = None secara default dan request. Fungsi pertama akan mengambil semua products dengan products = Product.objects.all() lalu memfilter berdasarkan category yang ada (apparel, shoes, dan others). Contohnya jika categorynya apparel maka  product akan difilter dengan kode products = products.filter(category__in=["Shirts", "Hoodies", "Socks", "Shorts"]). Lalu menambahkan filter type extra agar bisa menampilkan product user yang sedang login. Selanjutnya products, category, last login, nama, npm, kelas akan dibungkus menjadi context dan fungsi akan merender context pada "product_list.html".
25. Menghubungkan fungsi product_list_by_category pada urls.py dengan path "products/category//<str:category>/"
26. Memodifikasi navbar.html agar button Apparels, Shoes, dan Others yang ditambahkan akan mengimplementasikan url product_list_by_category dengan <a href="{% url 'main:product_list_by_category' '(categorynya)' %}"
27. Membuat product_list.html yang tampilannya sama dengan main.html namun karena fungsi yang diimplementasikan sudah memfilter product berdasarkan category yang dipencet pada navbar.html. maka cards yang akan ditampilkan adalah cards dengan category tersebut.
28. Melakukan add, commit, dan push pada github dan PWS.


# Tugas 5

## Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous berarti prosesnya berjalan secara berurutan dan harus ditunggu. Saat sebuah aksi dilakukan, misalnya sebuah tombol diklik, browser akan mengirim permintaan ke server. Selama permintaan diproses, seluruh halaman menjadi tidak responsif atau freeze. Tidak ada interaksi lain yang dapat dilakukan hingga server selesai memproses dan mengirim kembali satu halaman penuh yang baru.

Sedangkan Asynchronous (AJAX), prosesnya tidak saling menunggu. Ketika sebuah aksi dilakukan, permintaan akan dikirim ke server di latar belakang. Sambil menunggu respons dari server, halaman web tetap bisa di-scroll, formulir tetap bisa diisi, atau interaksi lainnya dapat terus dilakukan. Begitu server selesai merespons, hanya bagian tertentu dari halaman saja yang akan diperbarui dengan data baru, tanpa perlu ada proses muat ulang keseluruhan.

## Bagaimana AJAX bekerja di Django (alur request–response)?

Pemicu di Browser: Sebuah event (misalnya, klik tombol atau input data) memicu fungsi JavaScript.
Pengiriman Request: JavaScript, melalui fetch API atau XHR, mengirimkan request ke URL spesifik di server Django tanpa me-reload halaman. Untuk request POST, header X-CSRFToken harus disertakan untuk keamanan.
Routing di Django: urls.py menerima request dan meneruskannya ke view yang sesuai.
Proses di View: View memproses data yang diterima, berinteraksi dengan database jika perlu, dan menyiapkan response, biasanya dalam format JSON.
Pembaruan Halaman: Response dikirim kembali ke browser. JavaScript kemudian menerima data JSON ini dan secara dinamis mengubah konten HTML (DOM) pada halaman, seperti mengisi tabel atau menampilkan notifikasi tanpa perlu memuat ulang seluruh halaman.

## Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Responsivitas Tinggi: Aplikasi terasa lebih cepat karena hanya bagian kecil dari halaman yang diperbarui, bukan seluruhnya. Ini menghilangkan jeda yang disebabkan oleh full page reload.
Pengalaman Pengguna yang Lancar: Pengguna dapat terus berinteraksi dengan halaman web bahkan saat server sedang memproses permintaan di latar belakang, sangat ideal untuk fitur real-time seperti chat atau notifikasi.
Pemisahan Frontend dan Backend: AJAX mendorong pemisahan tugas yang jelas. Tim backend (Django) fokus pada penyediaan data melalui API, sementara tim frontend (JavaScript) fokus pada tampilan dan interaksi pengguna, sehingga mempermudah kolaborasi.

## Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Proteksi CSRF (Cross-Site Request Forgery): Pastikan {% csrf_token %} ada di template dan JavaScript mengirimkan token tersebut dalam header X-CSRFToken pada setiap request POST. Ini mencegah pihak luar memalsukan permintaan atas nama pengguna.
Otentikasi dan Otorisasi: Gunakan decorator seperti @login_required untuk melindungi view yang hanya boleh diakses oleh pengguna yang sudah login. Selain itu, selalu verifikasi kepemilikan data (misalnya, produk.user == request.user) untuk memastikan pengguna tidak mengubah data milik orang lain.
Validasi di Sisi Server: Selalu gunakan Django Forms untuk memvalidasi semua data yang masuk dari request. Gunakan form.is_valid() untuk memastikan tipe dan format data sudah benar sebelum disimpan.
Respons Error yang Minimal: Jika terjadi kegagalan login, kirim JsonResponse dengan pesan yang umum (contoh: "Kredensial tidak valid") dan jangan memberikan detail spesifik tentang kesalahan (seperti "Password salah") yang bisa dieksploitasi.

## Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX secara signifikan meningkatkan User Experience (UX) dengan membuat website terasa lebih dinamis dan interaktif. Karena tidak ada proses muat ulang halaman penuh, interaksi seperti memfilter produk, mencari data, atau validasi formulir terjadi secara instan dan mulus. Fitur seperti notifikasi atau pembaruan data real-time juga dapat diimplementasikan dengan mudah. Ini memberikan pengalaman pengguna yang lebih lancar dan modern. Namun, jika tidak diimplementasikan dengan baik, perubahan konten yang tiba-tiba dapat membingungkan pengguna. Oleh karena itu, penting untuk memberikan umpan balik visual yang jelas, seperti ikon loading, untuk menandakan bahwa sebuah proses sedang berjalan di latar belakang.
















