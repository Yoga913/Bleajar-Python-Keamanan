#!/usr/bin/python
#realizar permintaan web
import requests
#lidar dengan input dan output data, dalam berbagai cara
import io
#Usar agen acak untuk melakukan fuzzing
from fake_useragent import UserAgent
ua = UserAgent()
user_agent = ua.random
host='target'
filepath = 'wordlist.txt'
with open(filepath) as fp:
    line = fp.readline()
    while line:
        combined = host+line.strip()
        r = requests.get(combined, headers={'User-Agent': user_agent})
        if r.status_code == 200:
            #print('\n',r).format(line.strip())
            print(combined)
        line = fp.readline()
# ============================================================================== 
# PYTHON yang bertujuan untuk melakukan fuzzing atau serangan pencarian kata kunci pada sebuah target tertentu menggunakan daftar kata-kata yang disediakan dalam file `wordlist.txt`. 

# 1. `#!/usr/bin/python`: Ini adalah shebang line yang menentukan bahwa skrip ini akan dieksekusi menggunakan interpreter Python.

# 2. `import requests`: Modul `requests` digunakan untuk melakukan HTTP request ke target.

# 3. `import io`: Modul `io` digunakan untuk menangani input dan output data dalam berbagai bentuk.

# 4. `from fake_useragent import UserAgent`: Ini mengimpor kelas `UserAgent` dari modul `fake_useragent`. Modul ini digunakan untuk menghasilkan string User-Agent acak yang akan digunakan dalam setiap request. Hal ini dapat membantu dalam menghindari deteksi atau pemblokiran oleh firewall atau sistem keamanan.

# 5. `ua = UserAgent()`: Membuat objek `UserAgent` yang akan digunakan untuk mendapatkan string User-Agent.

# 6. `user_agent = ua.random`: Menghasilkan string User-Agent acak dari objek `UserAgent`.

# 7. `host='target'`: Variabel `host` ditetapkan sebagai target yang akan diserang.

# 8. `filepath = 'wordlist.txt'`: Variabel `filepath` menunjukkan path ke file `wordlist.txt` yang berisi daftar kata-kata yang akan digunakan dalam fuzzing.

# 9. `with open(filepath) as fp:`: Membuka file `wordlist.txt` untuk dibaca.

# 10. `line = fp.readline()`: Membaca baris pertama dari file `wordlist.txt`.

# 11. `while line:`: Memulai loop while untuk membaca setiap baris dari file `wordlist.txt`.

# 12. `combined = host+line.strip()`: Menggabungkan target dengan setiap kata kunci dari file `wordlist.txt`, menghilangkan karakter baris baru (`\n`) dari setiap baris.

# 13. `r = requests.get(combined, headers={'User-Agent': user_agent})`: Melakukan permintaan HTTP GET ke URL yang telah dibentuk sebelumnya (`combined`). Header request menyertakan string User-Agent yang telah di-generate sebelumnya.

# 14. `if r.status_code == 200:`: Memeriksa apakah respons dari server adalah 200 (OK).

# 15. `print(combined)`: Jika respons dari server adalah 200, maka URL yang berhasil diakses akan dicetak.

# 16. `line = fp.readline()`: Membaca baris berikutnya dari file `wordlist.txt` dan kembali ke langkah 11 sampai tidak ada baris lagi yang tersisa.

# Intinya, skrip ini membaca setiap kata kunci dari file `wordlist.txt`, menggabungkannya dengan target, dan mengirim permintaan HTTP GET ke URL yang dihasilkan dengan menggunakan string User-Agent acak. Jika respons dari server adalah 200, maka URL tersebut akan dicetak, menandakan bahwa kata kunci tersebut valid atau dapat diakses pada target yang ditentukan.
