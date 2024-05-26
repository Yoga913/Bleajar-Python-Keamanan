# Impor pustaka regex
import re

# Tetapkan file log ke variabel
logfile = "sample-log.log"

cpf = "412.111.210-03"

# Dalam kurung kurawal, kami menentukan jumlah kemunculan karakter tersebut. Dengan ini, kami dapat menemukan 3 digit.
# Sekarang datang "titik" tetapi kita tahu bahwa karakter ini memiliki arti khusus.
# Namun, kami ingin mencari titik secara literal dan bukan karakter apa pun.
# Untuk menegaskan bahwa titik harus menjadi titik saja, karakter tersebut harus di-escape dengan \. Dengan begitu kami memiliki:
cpfreg = "\d{3}\.\d{3}\.\d{3}\-\d{2}"

# Mengembalikan semua kecocokan yang tidak tumpang tindih dari pola dalam string, sebagai daftar string atau tuple.
# String diperiksa dari kiri ke kanan dan kecocokan dikembalikan dalam urutan yang ditemukan.
# Kecocokan kosong disertakan dalam hasil.

cpf_find = re.findall(cpfreg, cpf)

print(cpf_find, "\n")
# Semua di antara [] adalah karakter yang akan cocok
# \d cocok dengan digit dari [0-9], kami menetapkan bahwa digit muncul 1 hingga 3 karakter
# . cocok dengan setiap karakter
# Kami menambahkan dua titik tambahan, sehingga kecocokan cocok persis dengan alamat IP
logreg = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Dalam ekspresi reguler ini, kami akan menyaring semua yang HTTPS, yang cocok dengan satu-satunya ekspresi yang cocok dengan digit dan karakter yang setara dengan huruf kecil dan besar
# Jumlah kali kelas karakter ini harus muncul ditentukan oleh penghitung
# Tanda tanya (?), Yang berarti nol atau satu kali, adalah penghitung tambahan.
# Penghitung menunjukkan jumlah karakter atau ekspresi untuk dicocokkan.
# + Membuat hasil menjadi 1 dan melakukan pengulangan proses regex
logreg2 = "https?://(?:[-\w.]|(?:%[\da-fA-Z]{2}))+"

with open(logfile) as f:
    fread = f.read()
    # re.findall adalah untuk mencocokkan segalanya yang cocok dengan regex yang dilewati
    ip_list = re.findall(logreg, fread)
    ip_list2 = re.findall(logreg2, fread)
    # ip_list3 = re.findall(logreg3, fread)
    print(ip_list)
    print(ip_list2)
    # print(ip_list3)

#========================================================================================================= 
# kesimpulan : 
# Kode tersebut bertujuan untuk mengilustrasikan penggunaan ekspresi reguler (regex) dalam pemrograman Python untuk mencocokkan pola tertentu dalam string, serta penggunaan modul `re` untuk melakukan pencocokan pola tersebut.

# Maksud dari kode tersebut adalah sebagai berikut:

# 1. Memperkenalkan konsep ekspresi reguler dan cara penggunaannya dalam Python.
# 2. Menunjukkan bagaimana menggunakan ekspresi reguler untuk mencari pola tertentu dalam string, seperti pencarian nomor CPF dalam string.
# 3. Menjelaskan sintaks ekspresi reguler yang digunakan dalam contoh, seperti penggunaan `\d` untuk mencocokkan digit, `.` untuk mencocokkan titik secara literal, dan penggunaan penghitung untuk menentukan jumlah kemunculan karakter.
# 4. Menunjukkan penggunaan `re.findall()` untuk mencari semua kecocokan dalam sebuah string berdasarkan pola yang diberikan.

# Tujuan dari kode tersebut adalah memberikan pemahaman tentang penggunaan ekspresi reguler dalam Python untuk melakukan pencarian dan pencocokan pola tertentu dalam string, serta mengilustrasikan bagaimana hal itu dapat diterapkan dalam konteks pengolahan data seperti pembacaan file log dan pencarian alamat IP atau URL dalam teks log.
