# Impor modul socket untuk koneksi
import socket
# Target akan dimasukkan oleh pengguna
target = input('Masukkan IP/Domisili: ')
# Perulangan sebanyak 65535 kali (jumlah port TCP)
for port in range(1, 65535):
    
    # Menetapkan dan mengkonfigurasi klien
    klien = socket.socket()
    klien.settimeout(0.05)
    # Jika port terbuka, tampilkan di layar
    if klien.connect_ex((target, port)) == 0:
        print('Porta Terbuka ==>', port)

# ===================================================== 
# Kode tersebut bertujuan untuk melakukan pemindaian port pada sebuah alamat IP atau domain yang dimasukkan oleh pengguna. 

# Maksud dari kode tersebut adalah:

# 1. Menggunakan modul `socket` untuk mengatur koneksi.
# 2. Mengambil alamat IP atau domain sebagai input dari pengguna.
# 3. Melakukan iterasi melalui semua port TCP (dari 1 hingga 65535) untuk memeriksa apakah port tersebut terbuka pada alamat yang ditentukan.
# 4. Mengatur dan mengkonfigurasi klien socket untuk melakukan koneksi ke setiap port.
# 5. Jika koneksi berhasil dilakukan ke suatu port, artinya port tersebut terbuka, maka informasi tentang port tersebut akan ditampilkan di layar.

# Tujuan dari kode tersebut adalah memberikan kemampuan kepada pengguna untuk melakukan pemindaian port pada sebuah alamat IP atau domain tertentu, sehingga mereka dapat memeriksa port mana yang terbuka dan mungkin memerlukan perhatian lebih lanjut untuk keperluan pengujian keamanan atau pemecahan masalah jaringan.
