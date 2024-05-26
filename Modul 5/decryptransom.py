import os
import pyaes

# Buka file yang terenkripsi
nama_file = "test.txt.hacked"
file = open(nama_file, "rb")
data_file = file.read()

# Kunci saya untuk mendekripsi
kunci = b"blackhatpythoncs"  # kunci 16 byte
aes = pyaes.AESModeOfOperationCTR(kunci)
data_dekripsi = aes.decrypt(data_file)

# Hapus file terenkripsi
# os.remove(nama_file)

# Buat file terdekripsi baru
nama_file_baru = "decrypted.txt"
file_baru = open(f'{nama_file_baru}', "wb")
file_baru.write(data_dekripsi)
file_baru.close()

# ======================================================
# Secara singkat, kode tersebut melakukan dekripsi file yang telah dienkripsi menggunakan algoritma AES dengan mode operasi CTR.
#  Tujuan dari kode tersebut adalah untuk membuka file terenkripsi, mendekripsi datanya menggunakan kunci yang ditentukan, dan menyimpan hasil dekripsi ke dalam file baru agar dapat diakses dalam bentuk aslinya. 
# Opsi untuk menghapus file terenkripsi juga disertakan dalam kode, tetapi dijadikan sebagai komentar sehingga tidak dieksekusi secara otomatis.
