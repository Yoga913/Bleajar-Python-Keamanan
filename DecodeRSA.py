#import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

f = open ('encryption.txt', 'r')
message = f.read()

decrypted = key.decrypt(message)

print('decrypted', decrypted)

f = open ('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()

# Kode ini adalah contoh penggunaan pustaka Crypto (dengan modul `Crypto.PublicKey.RSA` dan `Crypto.Random`) untuk melakukan enkripsi dan dekripsi teks menggunakan algoritma RSA. 
# 1. `from Crypto.PublicKey import RSA`: Baris ini mengimpor kelas RSA dari modul `Crypto.PublicKey`, yang digunakan untuk membuat kunci RSA.

# 2. `from Crypto import Random`: Baris ini mengimpor modul `Random` dari pustaka Crypto, yang akan digunakan untuk menghasilkan bilangan acak.

# 3. `f = open('encryption.txt', 'r')`: Program membuka file `encryption.txt` untuk dibaca.

# 4. `message = f.read()`: Isi dari file `encryption.txt` dibaca dan disimpan dalam variabel `message`, yang akan dienkripsi.

# 5. `decrypted = key.decrypt(message)`: Program mencoba mendekripsi pesan menggunakan kunci privat yang telah diperoleh sebelumnya (variabel `key`). Namun, tidak ada inisialisasi atau pembuatan objek kunci dalam kode yang disediakan, yang berarti akan terjadi kesalahan pada bagian ini.

# 6. `print('decrypted', decrypted)`: Hasil dekripsi (jika berhasil) dicetak.

# 7. `f = open('encryption.txt', 'w')`: File `encryption.txt` dibuka untuk ditulis (mode `'w'`).

# 8. `f.write(str(message))`: Isi pesan yang asli (sebelum dienkripsi) ditulis kembali ke dalam file.

# 9. `f.write(str(decrypted))`: Jika ada, hasil dekripsi juga ditulis ke dalam file. Namun, karena tidak ada inisialisasi atau dekripsi yang benar dilakukan, ini mungkin akan menulis nilai `None` atau menyebabkan kesalahan lain.

# 10. `f.close()`: File ditutup setelah selesai ditulis.

# Kode ini tidak lengkap dan mungkin tidak berfungsi secara benar karena kurangnya inisialisasi kunci dan enkripsi sebelumnya. Untuk memperbaikinya, Anda perlu membuat kunci RSA terlebih dahulu menggunakan pustaka Crypto dan melakukan proses enkripsi sebelum mencoba mendekripsinya.
