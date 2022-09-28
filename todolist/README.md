# Tugas 4 PBP

Nama: Wedens Elma Malau

NPM: 2106751165

Link: https://tugas-2-pbp-wedens.herokuapp.com/todolist/

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
{% csrf_token %} pada form digunakan untuk menghindari Cross-Site Request Forgery (CSRF), atau sebuah kondisi ketika ada sebuah request dari user, walaupun user tersebut tidak melakukan request apa-apa. Istilah awamnya, akun user tersebut seperti dibajak, contohnya ketika seseorang mendapatkan pesan mengatasnamakan orang lain yang tidak mengirimkan pesan tersebut, bahkan tanpa diketahui sang pengirim. Ketika ada {% csrf_token %} pada form, setelah user memasukkan data login, token yang dihasilkan akan dicocokkan dengan token pengguna. Jika tidak

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Kita dapat membuat form secara manual, dengan membuat <form method="post">. Kita juga dapat menambahkan action untuk menspesifikasi ke mana data yang kita submit akan disampaikan. Sementara untuk men-submit data tersebut, kita dapat menggunakan input ataupun button submit. Contoh implementasi pembuatan form secara manual dapat dilihat di todolist.html line 28.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Setelah pengguna men-submit data melalui form, maka akan disampaikan sebuah request sesuai dengan yang ada di tag di <form> ke alamat pada atribut action. Dari path di action tersebut, kita akan dibawa ke suatu fungsi yang terdaftar pada file urls. Fungsi tersebut akan menerima parameter request, dan melakukan operasi di dalamnya sesuai dengan yang sudah didefinisikan pada file views.py. Ketika fungsi tersebut menerima POST dari input, maka objects akan disimpan ke database admin. 
  
Objek-objek yang tersimpan di database ada yang berbentuk sesuai class di file models.py, ada juga yang merupakan user. Sesuai path yang diakses di url, ada fungsi yang dipetakan, yang didefinisikan pada file views.py. Pada definisi di fungsi tersebut, jika return-nya mengembalikan render, maka akan diarahkan ke suatu file HTML yang tersimpan di template. Selain alamat file HTML, akan ada juga data context yang dibawakan. Context ini merupakan sebuah dictionary, di mana key-nya merupakan sebuah nama yang dapat diakses melalui file HTML tersebut, sedangkan value-nya merupakan data yang dikembalikan dari pemanggilan namanya di file HTML. Dengan begitu, ketika kita memanggil sebuah key dari context menggunakan {{ key }} di file HTML, maka akan dimunculkanlah data sesuai dengan yang ada di value-nya.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
  
Pertama-tama, saya melakukan startapp todolist di proyek Django. Perintah python manage.py startapp todolist akan membuat folder baru bernama todolist di repository lokal. Folder tersebut awalnya berisi admin, models, apps, test, views, dan folder migration.

Lalu, saya menambahkan path todolist/ di urls.py pada folder project_django untuk menampilkan app todolist ini. Ini juga akan menambahkan segala path lanjutan yang terdaftar di urls.py di folder todolist.

Selanjutnya, saya memasukkan atribut-atribut user, date, title, description, dan is_finished di models. Variabel-variabel ini berisi berbagai macam field yang ada di Models turunan Django, disesuaikan dengan kebutuhan bentuk tampilan. 

Untuk membuat halaman form, saya membuat sebuah file Forms.py yang berisi sebuah class bernama Form, dengan atribut title dan description, sesuai dengan yang diperlukan ketika menginput. Lalu, saya mengimplementasikan fungsi login_user, logout_user, dan register di file views.py. Fungsi-fungsi ini memanfaatkankan UserCreationForm. Selanjutnya, saya membuat sebuah file HTML di templates untuk ditampilkan. Ada dua file HTML untuk form, yaitu login dan register. Di dalam kedua file HTML tersebut, digunakan method POST sehingga input yang dimasukkan dapat tersimpan ke database.
  
Untuk halaman yang menampilkan todolist, saya membuat sebuah fungsi bernama show_todolist di views.py. Fungsi tersebut mengembalikan render ke todolist.html dan context yang berisi objek-objek task sesuai dengan user yang sedang login. Sedangkan isi dari todolist.html sendiri merupakan tabel dari iterasi objek-objek task yang telah di-create.
  
Untuk implementasi tombol create task, saya membuat sebuah fungsi create_task di views.py yang mengembalikan render ke create-task.html dan context yang merupakan form. File create-task.html di templates berisi field untuk menginput title dan description, serta sebuah tombol untuk meng-add input tersebut.
  
Setelah itu, saya mengimplementasikan routings di file urls.py. Di variabel URLPATTERNS, saya menambahkan path-path lanjutan seperti login/, logout/, create-task/, status, dan hapus/ sesuai dengan ketentuan di soal. Di bagian ini, ketiga fungsi yang telah dibuat di views.py akan dimanfaatkan. Contohnya, untuk path login/, kita akan memanfaatkan fungsi login_user untuk beralih ke halaman login.

Karena kita menggunakan repository yang sama dengan tugas pekan lalu yang telah dimasukkan secrets heroku, maka kita tinggal melakukan add, commit, dan push saja ke github dan deployment pun berhasil dilakukan.
