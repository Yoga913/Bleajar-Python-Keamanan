# Metode str.encode mengembalikan versi string yang dienkripsi sebagai objek byte. Encoding bawaannya adalah utf-8.

# Metode encode() mengembalikan versi string yang dienkripsi.
# Encoding bawaannya adalah encoding string saat ini. Kesalahan dapat diberikan untuk menetapkan skema penanganan kesalahan yang berbeda.

# Sebuah teks dalam UTF-8 sederhana, terbuat sepenuhnya dari ASCII dan,
# ketika kita membutuhkan karakter UNICODE, kita menggunakan karakter khusus yang menunjukkan 'Perhatian, karakter berikutnya dalam UNICODE'.

# UNICODE MEREKAM HURUF DAN ANGKA, BUKAN HANYA KODE 0 SAMPAI 127

# Alih-alih hanya menggunakan kode 0 hingga 127, UNICODE menggunakan kode dengan nilai yang jauh lebih besar. Dengan demikian, bisa merepresentasikan semua karakter spesifik
# dari berbagai bahasa.
# Kode baru secara teratur diberikan untuk karakter baru, seperti karakter Latin (dengan aksen atau tidak), Yunani, Sirilik, Armenia, Ibrani,
# Thailand, hiragana, katakana, dll.
# Hanya alfabet Tionghoa Kanji yang berisi 6.879 karakter. Oleh karena itu, UNICODE menetapkan korespondensi antara simbol dan angka.

# Ada berbagai kode. Yang paling terkenal adalah kode ASCII (American Standard Code for Information Interchange).
# Ini adalah standar Amerika, tetapi salah satu yang paling banyak digunakan di seluruh dunia. Kode ASCII menetapkan dengan tepat korespondensi
# antara simbol dan angka hingga angka 127:

# Namun, apakah Anda menyadari bahwa tidak ada karakter aksen? Yah, orang Amerika tidak memikirkan sisa dunia.
# Seringkali kita menggunakan kode 128 hingga 255 untuk aksen, tetapi kode-kode tersebut berbeda dari satu negara ke negara lainnya.
# Tidak praktis untuk pertukaran dokumen. Oleh karena itu, perlu menemukan kode yang lebih praktis: UNICODE.

# -*- coding: latin-1 -*-

string = "joas"
print(string.encode())

string.encode(encoding='UTF-8', errors='strict')

# Secara default, metode encode() tidak memerlukan parameter apa pun.

# Ini mengembalikan versi yang dienkripsi dalam utf-8 dari string. Jika gagal, itu akan menghasilkan pengecualian UnicodeDecodeError.

# Namun, dua parameter diperlukan:

# encoding - jenis encoding di mana sebuah string harus dienkripsi
# errors - respons ketika encoding gagal. Ada enam jenis respons kesalahan
# strict - respons default yang menghasilkan pengecualian UnicodeDecodeError jika gagal

# -- CONTOH encoding UTF-8
# string unicode
string = 'pythön!'

# cetak string
print('Stringnya adalah:', string)

# encoding default menjadi utf-8
string_utf = string.encode()

# cetak hasil
print('Versi terenkripsi:', string_utf)

# ================================================================================================ 
# kesimpulan : 

# Kode tersebut menjelaskan tentang konsep encoding dalam pemrograman Python, khususnya dengan menggunakan metode `encode()` untuk mengonversi string ke format byte dengan encoding tertentu, dalam contoh ini menggunakan UTF-8.

# Maksud dari kode tersebut adalah untuk memberikan pemahaman tentang cara menggunakan metode `encode()` dalam Python untuk mengonversi string ke bentuk yang dienkripsi sebagai objek byte dengan menggunakan encoding tertentu, dalam hal ini, UTF-8. Dijelaskan pula mengenai beberapa parameter yang dapat digunakan dengan metode `encode()`, seperti `encoding` untuk menentukan jenis encoding yang digunakan dan `errors` untuk menentukan respons saat terjadi kesalahan encoding.

# Tujuan dari kode tersebut adalah untuk memberikan contoh penggunaan metode `encode()` dengan encoding UTF-8 dan untuk memahamkan tentang pentingnya encoding dalam pemrosesan string, terutama dalam konteks pengolahan teks yang melibatkan karakter yang bukan merupakan bagian dari set karakter ASCII.
