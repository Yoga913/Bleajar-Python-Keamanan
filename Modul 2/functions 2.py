# Mendeklarasikan sebuah fungsi dasar dalam Python
def halo(nama_saya):
     print('Halo', nama_saya)
halo('Joas')

# Mendeklarasikan sebuah fungsi dengan nama dan usia
def halo2(nama_saya2, usia):
        print('Halo', nama_saya2, '\nUsiamu adalah:', usia)
halo2('José', 21)

# Sekarang kita punya sebuah fungsi yang menghitung gaji dan mengembalikan nilai yang harus dibayarkan sesuai dengan jumlah jam kerja.
# Fungsi calcular_pagamento() menerima dua parameter, qtd_jam dan nilai_jam, yang mewakili, masing-masing,
# jumlah jam yang akan dihitung dan nilai per jam.
def hitung_pembayaran(qtd_jam, nilai_jam):
  jam = float(qtd_jam)
  tarif = float(nilai_jam)
  if jam <= 40:
    gaji = jam*tarif # Jika jam kurang dari atau sama dengan 40, variabel gaji dibuka dan melakukan perhitungan kali jam dan tarif
  else:
    jam_lebih = jam - 40 # Jika tidak, ia menghitung jam ekstra - 40
    gaji = 40*tarif+(jam_lebih*(1.5*tarif)) # Jika lebih dari 40 jam, tambahkan ke gaji nilai tambahan untuk jam ekstra
  return gaji

# Sekarang mari gunakan fungsi ini untuk memasukkan nilai dan mencetaknya ke layar nanti
str_jam = input('Masukkan jumlah jam: ') # Informasi yang akan disimpan dalam string
str_tarif = input('Masukkan tarif: ')
total_gaji = hitung_pembayaran(str_jam, str_tarif) # Kemudian kita dapatkan hasil dari fungsi dan kami atributkan ke variabel total_gaji
print('Nilai penghasilan Anda adalah Rp', total_gaji)

# Fungsi bawaan di Python
# Fungsi tanpa perlu mengimpor pustaka
angka_terbesar = max(1, 2, 3)
huruf_terbesar = max('a', 'b', 'c')
print(angka_terbesar) # Akan menerima nilai 3
print(huruf_terbesar) # Akan menerima nilai c

# Beberapa fungsi hanya tersedia dalam modul
import math
eksponensial = math.exp(3)
print(eksponensial)
# Dalam kasus ini, untuk menggunakan perintah exp, perlu mengimpor modul MATH

# =========================================================================================== 
# Kesimpulan : 

# Kode tersebut bertujuan untuk mengilustrasikan penggunaan fungsi dalam bahasa pemrograman Python serta beberapa konsep dasar terkait operasi file dan fungsi bawaan dalam Python.

# Maksud dari setiap bagian kode adalah sebagai berikut:

# 1. **Deklarasi Fungsi:**
#    - Maksud: Mendemonstrasikan cara mendefinisikan dan menggunakan fungsi dalam Python untuk melakukan tugas tertentu.
#    - Tujuan: Memberikan pemahaman tentang sintaksis dasar untuk mendefinisikan dan memanggil fungsi dalam Python.

# 2. **Fungsi untuk Menghitung Gaji:**
#    - Maksud: Menunjukkan bagaimana membuat fungsi yang lebih kompleks untuk melakukan perhitungan gaji berdasarkan jumlah jam kerja.
#    - Tujuan: Memperkenalkan konsep penggunaan parameter dalam fungsi, penggunaan percabangan if-else untuk logika perhitungan, dan penggunaan fungsi return untuk mengembalikan nilai.

# 3. **Penggunaan Fungsi bawaan dan Modul:**
#    - Maksud: Memperlihatkan penggunaan fungsi bawaan dalam Python dan penggunaan modul untuk fungsi yang tidak tersedia secara langsung.
#    - Tujuan: Menunjukkan kepada pembaca beberapa fungsi bawaan yang berguna dalam Python seperti `max()`, serta bagaimana cara mengimpor dan menggunakan fungsi dari modul standar Python, dalam hal ini modul `math`.

# Dengan menggunakan contoh-contoh tersebut, tujuannya adalah memberikan pemahaman tentang penggunaan fungsi dalam Python, baik fungsi bawaan maupun fungsi yang didefinisikan sendiri, serta memperkenalkan beberapa konsep dasar seperti parameter, percabangan, dan penggunaan modul.
