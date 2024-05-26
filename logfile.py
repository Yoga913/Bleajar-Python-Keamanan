import re

logfile="sample-log.log"

logreg ="\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}."
#logreg="\bhttp:\/\/([^\/]*)\/([^\s]*)"
#logreg="\bhttp:\/\/"
logreg2 = "https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
with open (logfile) as f:
        fread = f.read()
        ip_list = re.findall(logreg, fread)
        ip_list2 = re.findall(logreg2, fread)
        print(ip_list)
        print(ip_list2)

# Program ini adalah contoh sederhana dari penggunaan modul `re` (Regular Expression) di Python untuk menganalisis file log. 


# 1. `import re`: Baris ini mengimpor modul `re`, yang digunakan untuk bekerja dengan ekspresi reguler.

# 2. `logfile = "sample-log.log"`: Ini adalah nama file log yang akan dibaca.

# 3. `logreg = "\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}."`: Ini adalah sebuah pola regular expression (regex) yang digunakan untuk menemukan alamat IP dalam file log. Pola ini mencocokkan empat angka yang dipisahkan oleh tiga titik, yang merupakan format umum untuk alamat IP.

# 4. `logreg2 = "https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+`: Ini adalah pola regex kedua yang digunakan untuk menemukan URL dalam file log. Pola ini dapat menangkap URL yang dimulai dengan "http://" atau "https://".

# 5. `with open(logfile) as f:`: Membuka file log menggunakan pernyataan `with`, yang memastikan bahwa file ditutup secara otomatis setelah selesai digunakan.

# 6. `fread = f.read()`: Membaca seluruh konten dari file log ke dalam string `fread`.

# 7. `ip_list = re.findall(logreg, fread)`: Menggunakan fungsi `findall()` dari modul `re` untuk mencari semua kecocokan pola `logreg` dalam string `fread`. Hasilnya adalah daftar semua alamat IP yang ditemukan dalam file log.

# 8. `ip_list2 = re.findall(logreg2, fread)`: Mencari semua kecocokan pola `logreg2` dalam string `fread`. Hasilnya adalah daftar semua URL yang ditemukan dalam file log.

# 9. `print(ip_list)`: Mencetak daftar alamat IP yang ditemukan.

# 10. `print(ip_list2)`: Mencetak daftar URL yang ditemukan.

# Jadi, program ini membaca file log, mencari alamat IP dan URL di dalamnya menggunakan ekspresi reguler, dan kemudian mencetak hasilnya.
