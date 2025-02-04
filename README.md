Penjelasan Proyek: Black Hole and Wormhole Simulation
Proyek ini adalah simulasi interaktif yang menggabungkan teknologi HTML, CSS, JavaScript untuk frontend dan Python (Flask) untuk backend. Simulasi ini menampilkan bola-bola yang ditarik oleh black hole secara perlahan, kemudian muncul kembali melalui wormhole. Berikut adalah penjelasan rinci tentang isi proyek:

1. Backend dengan Python (Flask)
Backend dibangun menggunakan Flask , sebuah framework Python ringan yang digunakan untuk menyajikan halaman web secara dinamis. Flask bertugas sebagai server lokal yang menyediakan file HTML, CSS, dan JavaScript kepada browser pengguna.

File app.py :
Mengatur routing untuk halaman utama (/) yang akan menampilkan file index.html.
Menggunakan fungsi render_template untuk menyajikan file HTML dari folder templates.
Server Flask dijalankan dalam mode debug untuk mempermudah pengembangan.
2. Frontend dengan HTML, CSS, dan JavaScript
Frontend adalah bagian visual dari simulasi yang berinteraksi langsung dengan pengguna. Ini mencakup tiga komponen utama:

a. File index.html
File ini adalah kerangka utama halaman web.
Menggunakan tag <canvas> untuk menggambar grafis animasi.
Memuat file CSS (styles.css) dan JavaScript (script.js) dari folder static.
b. File styles.css
Menyediakan styling dasar untuk halaman web.
Latar belakang halaman diatur menjadi hitam untuk memberikan kesan ruang angkasa.
Canvas diperluas ke seluruh layar untuk memaksimalkan area simulasi.
c. File script.js
Berisi logika utama simulasi, termasuk:
Kelas Ball : Mewakili bola dengan atribut seperti posisi, kecepatan, warna, dan radius.
Gravitasi : Menghitung gaya tarik black hole terhadap bola berdasarkan jarak.
Teleportasi : Saat bola masuk ke black hole, ia dipindahkan ke wormhole dengan kecepatan yang ditingkatkan.
Animasi : Menggunakan requestAnimationFrame untuk menjalankan loop animasi yang halus.
Responsif : Ukuran canvas disesuaikan secara otomatis saat jendela browser diubah ukurannya.



---

## **Bouncing Ball in Rotating Hexagon**
### **Deskripsi**
Proyek ini adalah simulasi bola yang memantul di dalam heksagon berputar menggunakan **Pygame**. Bola dipengaruhi oleh gravitasi dan gesekan saat mengenai dinding heksagon yang berotasi.

---

### **Struktur Folder**
```
/bouncing-ball.py                 # Kode utama simulasi
/blackhole&wormhole-with.html      # (Opsional) File terkait blackhole & wormhole
/blackhole&wormhole-with.py        # (Opsional) Kode terkait blackhole & wormhole
```

---

### **Fitur**
✅ Bola bergerak secara realistis dengan efek gravitasi dan gesekan  
✅ Heksagon berputar terus-menerus  
✅ Interaksi fisika antara bola dan dinding yang bergerak  
✅ Dibangun menggunakan **Python** dan **Pygame**  

---

### **Persyaratan**
Pastikan Anda menginstal **Pygame** sebelum menjalankan skrip:
```sh
pip install pygame
```

---

### **Cara Menjalankan**
1. **Clone atau unduh** repositori ini  
2. **Jalankan program** dengan perintah berikut:
   ```sh
   python bouncing-ball.py
   ```
3. Nikmati simulasi bola yang memantul di dalam heksagon berputar!

---

### **Lisensi**
Proyek ini dirilis di bawah **MIT License**. Bebas digunakan dan dimodifikasi sesuai kebutuhan.

---
