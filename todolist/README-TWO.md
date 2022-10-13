# Tugas 6 PBP

Nama: Wedens Elma Malau

NPM: 2106751165

Link: https://tugas-2-pbp-wedens.herokuapp.com/todolist/

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Pada asynchronus programming, program berjalan secara paralel. Asynchronus programming adalah cara agar tidak perlu menunggu antrian ketika terjadi request, sehingga user tidak perlu menunggu browser loading ketika sedang mengakses data di database. Dengan begitu, user dapat melakukan berbagai request ataupun aktivitas lain sekaligus, karena proses pengaksesan data hanya terjadi di background.

Sementara itu, synchronus programming bersifat single-thread. Pada synchronus programming, user harus mengantri terlebih dahulu dalam melakukan request. Pada synchronus programming, user harus menunggu browser loading ketika melakukan request, sehingga tidak dapat sambil melakukan berbagai request atau aktivitas lain sekaligus.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-driven programming adalah paradigma pemrograman yang berdasar pada event-event atau peristiwa yang terjadi, seperti input yang diberikan oleh pengguna, perangkat keras, ataupun aplikasi lain. Contohnya adalah ketika user mengklik sebuah tombol, maka terciptalah sebuah event. Lalu, akan terjadi handling oleh kode JS yang telah didefinisikan. Setelah operasi-operasi di dalamnya terjadi, halaman akan ter-refresh dan menyesuaikan dengan hasil operasi atau return dari handling tadi.

Contoh kode yang mengandung event handler pada tugas saya:

`<a style="width: 15rem;" class="btn login_btn btn btn-outline-primary form-control" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Create Task</a>`

Ketika tombol di atas diklik, maka akan diarahkan ke kode berikut, sehingga muncullah sebuah modal:
```<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">New Task</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <form id="formtask">
            {% csrf_token %}
            <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Task:</label>
            <input type="text" class="form-control" id="field_title" name="title">
            </div>
            <div class="mb-3">
            <label for="message-text" class="col-form-label">Description:</label>
            <textarea class="form-control" id="field_desc" name="description"></textarea>
            </div>
            </form>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" id="addtaskbutton" data-bs-dismiss="modal">Add</button>
        </div>
        </div>
    </div>
    </div>
```

## Jelaskan penerapan asynchronous programming pada AJAX.

Kepanjangan dari AJAX adalah Asynchronous JavaScript and XML. Pada dasarnya, AJAX memang sudah dirancang untuk dipakai dalam asynchronus programming. Cara kerjanya adalah dengan memuat data dari database melalui background, sehingga browser tidak ter-reload ulang. AJAX akan memanggil sebuat HTTP melalui background, sehingga halaman tetap ready dan user tetap dapat beraktivitas di halaman tersebut

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama, saya membuat view yang mengembalikan seluruh data task dalam bentuk JSON pada view.py. Lalu saya membuat path /todolist/json yang mengarah ke view yang baru dibuat.

Lalu, saya membuat sebuah tombol Create Task yang membuka sebuah modal dengan form untuk menambahkan task. Saya juga membuat sebuah fungsi view baru untuk menambahkan task baru ke dalam database, dan menambahkan path /todolist/add yang mengarah ke view yang baru saya buat. Selanjutnya, halaman akan direfresh secara asinkronus dengan otomatis untuk menampilkan list terbaru tanpa perlu me-reload seluruh page.