# Tugas 3 PBP

Nama: Wedens Elma Malau

NPM: 2106751165

Link: https://tugas-2-pbp-wedens.herokuapp.com/mywatchlist/


## Jelaskan perbedaan antara JSON, XML, dan HTML!

JSON (JavaScript Object Notation) adalah turunan dari Object di Javascript yang digunakan sebagai format untuk data delivery. Data pada JSON disimpan dalam bentuk array yang berisi key dan value. Key akan dipanggil dan value akan dikembalikan. Value dapat berupa tipe data primitif (string, number, boolean) ataupun berupa objek. Dengan demikian, JSON menyimpan elemennya dengan cara yang efisien, sehingga JSON banyak digunakan untuk pemrograman di berbagai bahasa, seperti C++ dan Python. Kekurangannya adalah, Tampilan JSON kurang rapih sehingga kurang mudah dimengerti oleh pembacanya.

Sedangkan, XML (Extensible Markup Language) adalah sebuah bahasa markup. Berbeda dengan JSON, XML lebih berfokus pada penampilan data yang tersimpan secara terstruktur dan rapi. Namun, dapat dikatakan kurang efisien. Bahasa markup yang ada di XML lebih mudah dimengerti manusia dibandingkan JSON yang hanya berupa array.

Sama seperti XML, HTML (HyperText Markup Language) juga merupakan bahasa markup. Hanya saja, HTML lebih berfokus pada proses menyajikan data, bukan mentransfer data. HTML digunakan untuk menerapkan tata letak dan konvensi pemformatan ke dokumen teks.


## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Dalam membuat suatu platform, tentunya kita tidak hanya perlu menampilkan teks, melainkan juga data. Untuk itu, kita perlu suatu struktur penyimpanan data yang dapat dengan mudah diakses untuk dipanggil dan ditampilkan ke platform yang kita buat. Data delivery berfungsi untuk menjadi sistem yang dapat membantu kita menampilkan data yang kita perlukan dalam pengembangan platform.


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 
Pertama-tama, saya melakukan startapp mywatchlist di proyek Django. Perintah python manage.py startapp mywatchlist akan membuat folder baru bernama mywatchlist di repository lokal. Folder tersebut awalnya berisi admin, models, apps, test, views, dan folder migration. 

Lalu, saya menambahkan path mywatchlist/ di urls.py pada folder project_django untuk menampilkan app mywatchlist ini. Ini juga akan menambahkan segala path lanjutan yang terdaftar di urls.py di folder mywatchlist.

Selanjutnya, saya memasukkan atribut-atribut watched, title, release_date, rating, dan review di models. Variabel-variabel ini berisi berbagai macam field yang ada di Models turunan Django. Contohnya, untuk title saya memanfaatkan CharField karena berisi teks yang tidak terlalu panjang, sedangkan untuk release_date saya memanfaatkan DateField untuk menampilkan tanggal dalam format yang rapi.

Selanjutnya, saya membuat folder bernama fixtures, lalu memasukkan 12 data dari watchlist saya dengan atribut judul, tanggal rilis, review, rating, dan status sudah ditonton atau belum. Data tersebut disimpan dalam array di file initial_watchlist_data.json.

Data yang sudah disimpan di file JSON tersebut saya manfaatkan untuk ditampilkan dalam tiga format sesuai soal, yaitu XML, HTML, dan JSON. Hal ini dapat dilakukan dengan membuat tiga fungsi di views.py. Fungsi pertama ialah show_mywatchlist, yang berfungsi untuk menampilkan file HTML di templates dalam bentuk HTML yang rapi. Fungsi kedua adalah show_xml, digunakan untuk menampilkan data dalam bentuk XML. Fungsi yang terakhir adalah show_json, yang berfungsi menampilkan data dalam bentuk array yang tersimpan pada file initial_watchlist_data.json.

Setelah itu, saya mengimplementasikan routings di file urls.py. Di variabel URLPATTERNS, saya menambahkan path-path lanjutan seperti html/, xml/, dan json/ sesuai dengan ketentuan di soal. Di bagian ini, ketiga fungsi yang telah dibuat di views.py akan dimanfaatkan. Contohnya, untuk path xml/, kita akan memanfaatkan fungsi show_xml untuk menampilkan data dalam format XML.

Karena kita menggunakan repository yang sama dengan tugas pekan lalu yang telah dimasukkan secrets heroku, maka kita tinggal melakukan add, commit, dan push saja ke github dan deployment pun berhasil dilakukan.


## Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md

### URL pertama: https://tugas-2-pbp-wedens.herokuapp.com/mywatchlist/html/

![postman_html](https://user-images.githubusercontent.com/94461284/191579147-237e32c4-29cf-49aa-9b6b-4dce6adc3e83.png)

### URL kedua: https://tugas-2-pbp-wedens.herokuapp.com/mywatchlist/xml/

![postman_xml](https://user-images.githubusercontent.com/94461284/191579422-5c9413e2-3492-470f-8fd0-094e48f346be.png)

### URL ketiga: https://tugas-2-pbp-wedens.herokuapp.com/mywatchlist/json/

![postman_json](https://user-images.githubusercontent.com/94461284/191579578-bece7f27-ebdb-488c-a250-7daef2596f3a.png)


## Menambahkan unit test pada tests.py untuk menguji bahwa tiga URL di poin 6 dapat mengembalikan respon HTTP 200 OK

![test_code](https://user-images.githubusercontent.com/94461284/191579827-0981a776-7b04-4fc5-9937-47d975f07930.png)

Hasil ketika dijalankan di terminal:

![test_result](https://user-images.githubusercontent.com/94461284/191579965-32eb1c0a-00c4-41af-b552-c1132299a6d5.png)
