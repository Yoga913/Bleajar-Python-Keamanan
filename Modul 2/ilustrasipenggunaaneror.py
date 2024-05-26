# Mari kita lihat kesalahan pembagian nol di interpreter dan kemudian kita akan menanganinya untuk menghasilkan output yang lebih ramah
#x = 12
#y = 0
#z = x/y

a = 12
b = 0
try:
    y = a/b
except ZeroDivisionError:
         print('Error: pembagian oleh nol')

#Kesalahan lain
#setiap kali kita menggunakan kelas yang kurang spesifik, kita dapat menangkap kesalahan dari kelas anaknya juga, misalnya kelas ZeroDivisionError adalah anak dari ArithmeticError
c = 12
d = 0
try:
    w = c/d
except ArithmeticError:
     print('Error dalam aritmatika')

 
#Kesalahan lain, kita dapat menggunakan jumlah excepts terbesar di dalam pengecualian
#Demonstrasi pada kesalahan logika
e = 12
f = 2
li = [1, 2, 3, 4]
try:
    z = int(e/f)
    p = li[z]
except ZeroDivisionError:
     print('Error pembagian oleh nol')
except IndexError:
    print('Error: mencoba mencapai indeks yang tidak ada dalam daftar')

#Contoh lain
#kita bisa memiliki klausa finally yang selalu dijalankan pada akhir independen dari apakah pengecualian dilemparkan dari klausa else yang digunakan atau tidak
try:
     arq = open('data/arquivo.txt', 'r')
except FileNotFoundError:
    print('Error: file tidak ditemukan')
else:
    print('Suite ini tidak dijalankan')
finally:
    print('Selalu dieksekusi')  

#========================================================================================== 
# kesimpulan : 
# Kode tersebut bertujuan untuk mengilustrasikan penggunaan penanganan kesalahan (error handling) dalam bahasa pemrograman Python. Tujuan dari kode tersebut adalah:

# 1. Mengidentifikasi kesalahan pembagian oleh nol (ZeroDivisionError) dan menangani kesalahan tersebut dengan mencetak pesan yang ramah.
# 2. Menunjukkan bahwa ketika menggunakan pengecualian yang lebih umum, seperti ArithmeticError, kita dapat menangkap kesalahan turunannya, seperti ZeroDivisionError.
# 3. Menunjukkan penggunaan beberapa blok except dalam satu blok try untuk menangani berbagai jenis kesalahan.
# 4. Mendemonstrasikan penggunaan blok finally, yang akan dieksekusi terlepas dari apakah pengecualian dilemparkan atau tidak, serta apakah blok else digunakan atau tidak.

# Dengan demikian, tujuan utama dari kode tersebut adalah untuk memberikan pemahaman tentang bagaimana cara menangani kesalahan dalam Python dengan menggunakan berbagai mekanisme yang tersedia, seperti blok try-except dan blok finally.
