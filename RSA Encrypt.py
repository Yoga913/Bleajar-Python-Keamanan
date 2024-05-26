import rsa
 
# menghasilkan kunci publik dan pribadi dengan
# metode rsa.newkeys, metode ini menerima
# panjang kunci sebagai parameternya
# panjang kunci harus minimal 16
publicKey, privateKey = rsa.newkeys(512)
 
# ini adalah string yang akan kita enkripsi
message = "RSAA_Flag_Secret"
 
# Metode RSA.ENCRYPT digunakan untuk mengenkripsi
# string dengan string kunci publik harus
# menyandikan ke byte string sebelum enkripsi
# dengan metode encode
encMessage = rsa.encrypt(message.encode(),
                         publicKey)

print("string asli: ", message)
print("string terenkripsi: ", encMessage)

decMessage = rsa.decrypt(message, privateKey).decode()
 
print("string yang didekripsi: ", decMessage)

# Program ini adalah contoh penggunaan pustaka RSA (Rivest-Shamir-Adleman) dalam Python untuk melakukan enkripsi dan dekripsi pesan menggunakan kunci publik dan privat.
#  Berikut adalah penjelasan mengenai kode dan alur kerjanya:

# 1. `import rsa`: Baris ini mengimpor modul `rsa`, yang menyediakan fungsi-fungsi untuk enkripsi RSA.

# 2. `publicKey, privateKey = rsa.newkeys(512)`: Fungsi `rsa.newkeys()` digunakan untuk membuat pasangan kunci publik dan privat baru. Dalam kasus ini, kita membuat pasangan kunci dengan panjang 512 bit. Kunci yang dihasilkan disimpan dalam variabel `publicKey` dan `privateKey`.

# 3. `message = "RSAA_Flag_Secret"`: Ini adalah pesan yang akan dienkripsi.

# 4. `encMessage = rsa.encrypt(message.encode(), publicKey)`: Fungsi `rsa.encrypt()` digunakan untuk mengenkripsi pesan menggunakan kunci publik. Pesan harus diubah menjadi byte string sebelum dienkripsi, oleh karena itu kita menggunakan metode `encode()` untuk mengubah pesan menjadi byte string.

# 5. `print("original string: ", message)`: Mencetak pesan asli sebelum dienkripsi.

# 6. `print("encrypted string: ", encMessage)`: Mencetak pesan yang telah dienkripsi.

# 7. `decMessage = rsa.decrypt(message, privateKey).decode()`: Fungsi `rsa.decrypt()` digunakan untuk mendekripsi pesan yang telah dienkripsi menggunakan kunci privat. Hasil dekripsi berupa byte string, oleh karena itu kita gunakan metode `decode()` untuk mengubahnya kembali menjadi string.

# 8. `print("decrypted string: ", decMessage)`: Mencetak pesan yang telah didekripsi.

# Alur kerja program ini adalah sebagai berikut:

# - Pertama-tama, pasangan kunci RSA (publik dan privat) dibuat.
# - Sebuah pesan ditentukan untuk dienkripsi.
# - Pesan tersebut dienkripsi menggunakan kunci publik.
# - Pesan yang telah dienkripsi dicetak.
# - Pesan yang telah dienkripsi kemudian didekripsi menggunakan kunci privat.
# - Pesan yang telah didekripsi dicetak.

