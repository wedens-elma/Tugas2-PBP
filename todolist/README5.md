# Tugas 5 PBP

Nama: Wedens Elma Malau

NPM: 2106751165

Link: https://tugas-2-pbp-wedens.herokuapp.com/todolist/

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Inline CSS memberikan style kepada halaman HTML dengan cara menuliskannya langsungke dalam tag. Inline CSS digunakan untuk membuat hanya elemen spesifik tertentu yang mempunyai style tersebut. Kekurangannya adalah style yang berlebihan membuat kode sangat panjang ke kanan, sehingga sulit dibaca. Berikut contoh penggunaan Inline CSS pada tag:

<h2 style="font-family:'Courier New', Courier, monospace">Welcome, {{user}}!</h2>

Internal CSS memberikan style kepada halaman HTML dengan cara menuliskan stylesheet ke dalam halaman HTML dengan tag <style>. Internal CSS digunakan untuk memberikan style pada satu halaman tersebut saja. Namun, penggunaan internal CSS yang sama di berbagai halaman membuat kode menjadi repetitif. Berikut contoh penggunaan Internal CSS:

<style>
    body {
      font-family: 'Courier New', Courier, monospace;
      background: rgb(2,0,36);
      background: radial-gradient(circle, rgb(255, 255, 255) 0%, rgb(218, 255, 204) 35%, rgb(173, 250, 255) 100%);
    }
</style>
  
External CSS memberikan style kepada halaman HTML dengan cara menuliskan sebuah stylesheet di luar file HTML. Stylesheet untuk dapat dimasukkan ke suatu folder static. Kelebihannya adalah pemberian style akan konsisten untuk semua halaman. Kelemahannya adalah runtime akan sedikit memakan waktu lebih lama, karena browser harus melakukan request ke halaman style lagi selain HTML. Berikut contoh penggunaan External CSS:

<link rel="stylesheet" href="{% static 'css/style.css' %}">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

## Jelaskan tag HTML5 yang kamu ketahui.

1. <nav> dapat digunakan untuk membuat navigation bar dan menu.
2. <picture> digunakan untuk menampilkan sebuah gambar
3. <audio> digunakan untuk memberikan suara atau audio

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

1. namaElement {} digunakan untuk memberikan style pada elemen tertentu. Contohnya, body mengaplikasikan style kepada seluruh elemen <body>.
  
2. .namaClass digunakan untuk memberikan style pada elemen anggota class tertentu. Contohnya, .login mengaplikasikan style kepada seluruh elemen yang termasuk class login.

3. #id digunakan untuk memberikan style pada elemen dengan id tertentu. Contohnya, #id-abc mengaplikasikan style kepada elemen yang mempunyai id id-abc.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

