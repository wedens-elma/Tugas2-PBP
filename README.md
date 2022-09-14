# Tugas 2 PBP

Nama: Wedens Elma Malau

NPM: 2106751165

Link: https://tugas-2-pbp-wedens.herokuapp.com/katalog/

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![bagan](https://github.com/wedens-elma/Tugas2-PBP/blob/main/bagan%20readme%20tugas%202.png)

Ketika user mengetikkan url pada browser, itu artinya user sedan melakukan request. Selanjutnya, terjadi pemetaan alamat dari URL ke Views yang tepat. Views akan meminta data ke Models yang akan mengembalikan data dari database. Setelah Views mendapatkan datanya melalui Models, Views juga akan berhubungan dengan berkas HTML pada template. Views akan menunjuk kepada berkas HTML yang ada di fungsi. Data yang telah didapatkan dari akses Models ke database lalu dikembalikan sesuai pemanggilan pada berkas HTML. Dengan begitu, webpage akan ditampilkan ke user sesuai dengan pengaturan di berkas HTML yang telah dibuat. 

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita tetap dapat membuat aplikasi web berbasis Django walaupun tanpa menggunakan virtual environment. Tetapi, jika menggunakan virtual environment, kita dapat lebih mudah memisahkan project-project Django yang kita buat, dari segi pengaturan maupun dependencies. Hal ini membuat project-project kita lebih rapih dan kekurangan dari satu project tidak terlalu berpengaruh pada yang lain. Selain itu, virtual environment juga memudahkan dari sisi mobilitas. Jika menggunakan virtual environment yang sama, kita tidak perlu menginstall ulang requirements yang sudah pernah diinstall walaupun dalam device yang berbeda.

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Pada views, saya membuat sebuah fungsi bernama show_katalog dengan satu parameter request yang returnnya memanggil fungsi render dari Django shortcuts dengan parameter request, file katalog.html, dan sebuah variabel bernama context. Variabel context di sini mengandung sebuah set yang values-nya merupakan data, dan keys-nya merupakan sebuah nama yang nantinya dapat digunakan di file html untuk menampilkan datanya.

Implementasi routings dilakukan di file url. Pemetaan dilakukan dengan membuat suatu variabel bernama urlpatterns yang berisi sebuah list. Di dalam list tersebut, terpanggil sebuah fungsi bernama path. Routings ini dilakukan untuk memetakan fungsi pada views. Tidak lupa, kita juga harus melakukan routing ke katalog/ dengan menambahkannya ke urlpatterns di file urls yang di folder project.

Pemetaan ke dalam HTML dibuat menggunakan nama-nama variabel yang ada di dalam file models. Pemanggilan nama-nama variabel tersebut akan mengembalikan data-data models yang juga terhubung dengan file JSON di fixtures.

Setelah semua views, models, dan template selesai dirancang, kita melakukan deployment ke Heroku. Setelah melakukan add, commit, push ke github, kita menambahkan secrets ke dalam repo. Secrets tersebut adalah nama dari app yang kita buat di Heroku dan API key dari akun Heroku kita. Karena sebelum ditambahkan secrets deployment di github akan gagal, kita dapat me-rerun jobs yang gagal. Setelah itu, barulah kita dapat mengakses aplikasi yang selesai kita buat melalui internet.
