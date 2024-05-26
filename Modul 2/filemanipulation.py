# Meneruskan nama file dan membuatnya
#fo = open("test.txt", "wb")
#print ("Nama file: ", fo.name)

# Menutup file yang dibuka
#fo.close()


# Membuat file dan menulis di dalamnya
#file = open('geek.txt','w')
#file.write("Ini adalah perintah tulis")
#file.write("Ini memungkinkan kita untuk menulis di dalam file tertentu")
#file.close()


# Membuka sebuah file dan menulis di dalamnya
#fo = open("test.txt", "w")
#fo.write("Python adalah bahasa yang hebat\nYa, itu hebat!!\n")

# Menutup file yang dibuka
#fo.close()

# Menggunakan pustaka OS untuk mengubah nama file
#import os

# Mengubah nama file dari test1.txt menjadi test2.txt
#os.rename( "test.txt", "test2.txt" )

# Menggunakan pustaka OS untuk menghapus sebuah file
import os
os.remove("test2.txt")

# ================================================================= 
# Kesimpulan : 
# Kode tersebut bertujuan untuk mendemonstrasikan beberapa operasi dasar pada file dalam bahasa pemrograman Python, seperti pembuatan, penulisan, penamaan ulang, dan penghapusan file. Berikut adalah maksud dan tujuan dari setiap bagian kode:

# 1. **Membuat dan Menutup File:**
#    - Maksud: Bagian ini bertujuan untuk menunjukkan cara membuat file baru dan menutupnya setelah selesai digunakan.
#    - Tujuan: Memperlihatkan cara menggunakan fungsi `open()` untuk membuat file baru dengan mode tertentu (dalam kasus ini, mode biner) dan kemudian menutupnya dengan fungsi `close()` setelah selesai.

# 2. **Menulis di dalam File:**
#    - Maksud: Bagian ini dimaksudkan untuk menunjukkan bagaimana menulis teks ke dalam file yang sudah dibuat sebelumnya.
#    - Tujuan: Mendemonstrasikan penggunaan mode 'w' pada fungsi `open()` untuk menulis teks ke dalam file dan kemudian menutup file tersebut setelah selesai menulis.

# 3. **Mengubah Nama File:**
#    - Maksud: Bagian ini bertujuan untuk menunjukkan cara mengubah nama file yang sudah ada menggunakan pustaka `os`.
#    - Tujuan: Menunjukkan penggunaan fungsi `rename()` dari pustaka `os` untuk mengubah nama file dari `test.txt` menjadi `test2.txt`.

# 4. **Menghapus File:**
#    - Maksud: Bagian ini dimaksudkan untuk menunjukkan cara menghapus file yang sudah ada menggunakan pustaka `os`.
#    - Tujuan: Menunjukkan cara menggunakan fungsi `remove()` dari pustaka `os` untuk menghapus file dengan nama `test2.txt`.

# Dengan menggunakan contoh-contoh tersebut, tujuannya adalah memberikan pemahaman tentang bagaimana melakukan operasi dasar pada file dalam Python dan penggunaan pustaka standar seperti `os` untuk manipulasi file.
