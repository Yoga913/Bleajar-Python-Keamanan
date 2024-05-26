# Argumen yang dilewatkan ke socket() adalah konstan yang digunakan untuk menentukan keluarga alamat dan jenis soket. AF_INET adalah keluarga alamat Internet untuk IPv4. SOCK_STREAM adalah jenis soket untuk TCP, 
# protokol yang akan digunakan untuk mengirim pesan melalui jaringan.

import socket

HOST = "127.0.0.1"  # Alamat antarmuka loopback standar (localhost)
PORT = 65432  # Port yang digunakan (port tidak berizin adalah > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Metode .bind() digunakan untuk mengaitkan soket dengan antarmuka jaringan dan nomor port tertentu:
    s.bind((HOST, PORT))
    # Dalam contoh server, .listen() memungkinkan server menerima koneksi. Ini membuat server menjadi soket "mendengarkan":
    s.listen()
    # conn, adalah objek soket yang dapat Anda gunakan untuk mengirim dan menerima data dari klien yang terhubung.
    # addr, berisi informasi alamat tentang klien yang terhubung (misalnya, alamat IP dan port remote).
    # Soket harus diikat ke suatu alamat dan mendengarkan koneksi.
    conn, addr = s.accept()
    # Penggunaan pernyataan with digunakan untuk secara otomatis menutup soket pada akhir blok.
    with conn:
        print(f"Terkoneksi oleh {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

# ==================================================================================================================================================== 
# kesimpulan : 
# Kode tersebut bertujuan untuk membuat sebuah server sederhana menggunakan modul `socket` dalam Python. Maksud dan tujuannya adalah sebagai berikut:

# Maksud:
# 1. Memperkenalkan konsep penggunaan modul `socket` dalam Python untuk membuat server TCP/IP.
# 2. Menjelaskan argumen yang digunakan dalam pembuatan objek socket, seperti `AF_INET` yang merupakan konstanta untuk menentukan keluarga alamat (IPv4) dan `SOCK_STREAM` yang merupakan konstanta untuk menentukan jenis soket (TCP).
# 3. Menggambarkan langkah-langkah yang diperlukan untuk membuat server, termasuk mengikat soket ke alamat dan port tertentu, mendengarkan koneksi dari klien, dan menerima dan mengirim data.

# Tujuan:
# 1. Mengikat server ke alamat dan port tertentu sehingga dapat menerima koneksi dari klien.
# 2. Menerima koneksi dari klien yang terhubung dan menangani komunikasi dengan klien tersebut.
# 3. Menerima pesan dari klien, mengirimkan pesan balasan yang sama, dan mencetak informasi tentang koneksi klien yang terhubung.
# 4. Menjelaskan konsep penggunaan pernyataan `with` untuk memastikan penutupan soket secara otomatis setelah penggunaan selesai.

# Dengan demikian, kode tersebut merupakan dasar untuk membuat server TCP/IP sederhana dalam Python yang dapat menerima dan menanggapi koneksi dari klien.
