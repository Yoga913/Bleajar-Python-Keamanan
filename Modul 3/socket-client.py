# echo-client.py

# Dibandingkan dengan server, klien cukup sederhana.
# Ini membuat objek socket, menggunakan .connect() untuk terhubung ke server, dan memanggil s.sendall() untuk mengirim pesan.
# Akhirnya, ia memanggil s.recv() untuk membaca respons dari server dan mencetaknya.

import socket

HOST = "127.0.0.1"  # Nama host atau alamat IP server
PORT = 65432  # Port yang digunakan oleh server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Terima {data!r}")

# ================================================================ 
# kesimpulan : 
# Kode tersebut merupakan implementasi sederhana dari sebuah klien untuk protokol TCP/IP. Maksud dan tujuannya adalah sebagai berikut:

# Maksud:
# 1. Memperkenalkan cara menggunakan modul `socket` dalam Python untuk membuat klien TCP/IP.
# 2. Menjelaskan langkah-langkah yang diperlukan untuk membuat koneksi klien ke server, mengirim pesan, dan menerima respons.
# 3. Mengilustrasikan bagaimana objek socket dibuat, dihubungkan ke server, pesan dikirim, dan responsnya diterima.

# Tujuan:
# 1. Menghubungkan klien ke server dengan menggunakan protokol TCP/IP.
# 2. Mengirimkan pesan "Hello, world" ke server.
# 3. Menerima respons dari server.
# 4. Mencetak respons tersebut di layar.

# Dengan demikian, kode tersebut dapat digunakan sebagai dasar untuk mengembangkan klien yang lebih kompleks yang berkomunikasi dengan server menggunakan protokol TCP/IP.
