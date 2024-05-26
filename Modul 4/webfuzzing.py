#!/usr/bin/python
# Melakukan permintaan web
import requests
# Mengelola masukan dan keluaran data dalam berbagai format
import io
# Menggunakan agen pengguna palsu untuk melakukan crawling
from fake_useragent import UserAgent
# Membuka variabel dengan nilai UserAgent
ua = UserAgent()
# akhirnya, menghasilkan agen pengguna acak
user_agent = ua.random
# URL target Anda
host='https://uniciv.com.br/'
# wordlist list
filepath = 'wordlist.txt'
# Loop untuk menguji halaman satu per satu dalam wordlist
with open(filepath) as fp:
    line = fp.readline()
    # Menggabungkan hasil host dan baris yang dibaca dari wordlist
    while line:
        combined = host+line.strip()
        # Menggunakan agen dengan metode Get. Dan jika semuanya 200, itu akan ditampilkan di layar
        r = requests.get(combined, headers={'User-Agent': user_agent})
        if r.status_code == 200:
            # print('\n',r).format(line.strip())
            print(combined)
        line = fp.readline()

# =============================================================================================================== 

# Skrip ini bertujuan untuk melakukan crawling pada sebuah situs web dengan menggunakan wordlist sebagai daftar potensi halaman yang akan diakses. Berikut adalah maksud dan tujuan dari skrip ini:

# 1. **Melakukan Permintaan Web**: Skrip menggunakan modul `requests` untuk melakukan permintaan HTTP ke server. Ini memungkinkan skrip untuk mengakses halaman web dan mendapatkan respons dari server.

# 2. **Menggunakan Fake User-Agent**: Skrip menggunakan modul `fake_useragent` untuk menghasilkan User-Agent palsu secara acak. Ini membantu dalam mengelabui server dan mencegah deteksi otomatis dari bot.

# 3. **Mengakses Halaman Target**: Skrip menentukan URL target dalam variabel `host`, yang merupakan situs web yang akan di-crawl. Selain itu, skrip membaca daftar kata kunci dari file `wordlist.txt` yang berisi daftar potensi halaman yang akan diakses.

# 4. **Loop untuk Menguji Halaman**: Skrip menggunakan loop untuk menguji setiap halaman yang tercantum dalam wordlist. Untuk setiap halaman, skrip membentuk URL lengkap dengan menggabungkan URL target dengan setiap baris dalam wordlist. Kemudian, skrip melakukan permintaan GET ke halaman tersebut menggunakan User-Agent palsu yang dihasilkan sebelumnya.

# 5. **Mencetak Halaman yang Ditemukan**: Jika respons dari server memiliki status code 200 (OK), artinya halaman tersebut berhasil diakses, dan URL-nya akan dicetak ke layar. Ini memungkinkan pengguna untuk melihat halaman-halaman yang berhasil diakses selama proses crawling.

# Tujuan utama dari skrip ini adalah untuk melakukan crawling pada situs web tertentu dan mengidentifikasi halaman-halaman yang dapat diakses berdasarkan daftar kata kunci yang disediakan dalam wordlist. Ini dapat berguna dalam skenario seperti pengujian keamanan, pemetaan situs web, atau pengumpulan informasi untuk analisis.
