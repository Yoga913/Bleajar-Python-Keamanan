import aiohttp
import asyncio
import time

# Membuat metode untuk mengunduh file dari URL untuk mengumpulkan informasi, membuat sesi HTTP di URL untuk melaksanakan prosesnya
async def unduh_berkas(url):
  print(f'Memulai pengunduhan {url}')
  async with aiohttp.ClientSession() as sesi:
    async with sesi.get(url) as resp:
      konten = await resp.read()
      print(f"Menyelesaikan pengunduhan {url}")
      return konten

# Pada tahap ini, ia akan membaca konten berkas yang dibuat dengan nama async_{name} dan membuka berkas dalam mode biner agar tidak mengubah data saat disimpan
async def tulis_berkas(nama, konten):
  nama_berkas = f'async_{nama}.html'
  with open(nama_berkas, 'wb') as f:
    print(f'Membaca berkas {nama_berkas}')
    f.write(konten)
    print(f'Menyelesaikan pembacaan {nama_berkas}')

# Berikutnya adalah tugas-tugas yang akan dieksekusi dengan berkas
async def tugas_penambangan(nama, url):
  konten = await unduh_berkas(url)
  await tulis_berkas(nama, konten)

async def utama():
  tugas = []
  for nama, url in enumerate(open('urls.txt').readlines()):
    tugas.append(tugas_penambangan(nama,url))
  await asyncio.wait(tugas)
 
if __name__ == '__main__':
  t = time.perf_counter()
  asyncio.run(utama())
  t2 = time.perf_counter() - t
  print(f'Waktu berlalu: {t2:0.2f} detik')

# =======================================================================================================
# kesimpulan : 
# Kode program ini merupakan contoh implementasi dari *asynchronous programming* menggunakan modul `asyncio` dan `aiohttp` dalam bahasa Python. Tujuan utamanya adalah untuk melakukan pengunduhan berkas dari beberapa URL secara bersamaan tanpa memblok eksekusi program, sehingga meningkatkan efisiensi waktu.

# Berikut adalah penjelasan dan alur kerja dari kode program ini:

# 1. **Import Modul**: Kode program mengimpor modul `aiohttp` untuk mengelola permintaan HTTP secara asynchronous, `asyncio` untuk mengelola *asynchronous tasks*, dan `time` untuk mengukur waktu eksekusi.

# 2. **Definisi Fungsi `unduh_berkas(url)`**: Ini adalah fungsi `async` yang bertugas untuk mengunduh konten dari sebuah URL. Dalam fungsi ini, sesi HTTP dibuat menggunakan `ClientSession` dari `aiohttp`. Kemudian, permintaan HTTP dilakukan menggunakan metode `get()` pada sesi tersebut, dan konten dari responsnya diunduh menggunakan `resp.read()`.

# 3. **Definisi Fungsi `tulis_berkas(nama, konten)`**: Fungsi ini bertugas untuk menulis konten yang diunduh ke dalam sebuah berkas dengan nama yang ditentukan. Berkas dibuka dalam mode biner (`'wb'`) agar konten dapat ditulis dalam bentuk biner.

# 4. **Definisi Fungsi `tugas_penambangan(nama, url)`**: Fungsi ini merupakan tugas utama yang akan dieksekusi. Pertama, ia akan memanggil fungsi `unduh_berkas()` untuk mengunduh konten dari URL yang diberikan. Setelah itu, konten tersebut akan ditulis ke dalam berkas menggunakan fungsi `tulis_berkas()`.

# 5. **Definisi Fungsi `utama()`**: Fungsi utama yang akan dijalankan. Di dalamnya, dilakukan iterasi melalui daftar URL yang dibaca dari berkas `urls.txt`. Setiap URL akan dimasukkan ke dalam tugas penambangan dan akan dieksekusi secara asynchronous.

# 6. **Eksekusi Utama**: Pada bagian `if __name__ == '__main__':`, waktu awal diukur menggunakan `time.perf_counter()`. Fungsi `asyncio.run()` kemudian digunakan untuk menjalankan fungsi utama secara asynchronous. Setelah selesai, waktu eksekusi dihitung kembali dan perbedaannya dicetak sebagai waktu yang diperlukan untuk menjalankan semua tugas.

# Dengan menggunakan pendekatan *asynchronous programming* seperti ini, program dapat secara efisien mengunduh berkas dari beberapa URL secara bersamaan, meningkatkan kinerja secara keseluruhan.