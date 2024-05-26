import socket

# Tentukan host mesin Anda
HOST = '10.0.0.115' # '192.168.43.82'
# Porta yang akan digunakan
PORT = 8081 # 2222
# Buat soket
server = socket.socket()
# Aktifkan dan konfigurasikan koneksi soket kita
server.bind((HOST, PORT))
print('[+] Server Dimulai')
print('[+] Mendengarkan Koneksi Klien ...')
# Menetapkan soket untuk mendengarkan
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Klien terhubung ke server')

# Membuat loop untuk mengirim perintah
while True:
    command = input('Masukkan Perintah : ')
    command = command.encode()
    # Mengirim perintah yang diencode
    client.send(command)
    print('[+] Perintah terkirim')
    output = client.recv(1024)
    # Menggunakan encoding untuk menentukan format karakter yang akan dimasukkan ke dalam soket
    output = output.decode(encoding='iso8859-1')
    print(f"Output: {output}")

# iso8859-1 ISO/IEC 8859-1 adalah set karakter standar untuk sebagian besar browser. Dikenal sebagai latin-1, ini adalah standar karakter Latin yang banyak digunakan

# ========================================================================================================================================================================================== 
# kesimpulan : 

# Skrip ini bertujuan untuk membuat server sederhana yang menerima koneksi dari klien dan memungkinkan pengguna untuk mengirim perintah kepada server melalui socket. Setelah menerima perintah dari pengguna, server akan mengirimkan perintah tersebut ke klien, menjalankannya, dan mengirimkan output kembali ke server untuk ditampilkan kepada pengguna.

# Berikut adalah maksud dan tujuan dari skrip ini:

# 1. **Membuat Server**: Skrip ini membuat server menggunakan modul `socket` dari Python. Server diikat ke alamat HOST dan PORT yang telah ditentukan.

# 2. **Menerima Koneksi Klien**: Server menunggu koneksi dari klien dengan menggunakan metode `listen()` dan `accept()`. Setelah koneksi diterima, informasi tentang klien yang terhubung akan dicetak.

# 3. **Mengirim dan Menerima Perintah**: Server menggunakan loop tak terbatas (`while True`) untuk terus menerima perintah dari pengguna. Pengguna diminta untuk memasukkan perintah, kemudian perintah tersebut dikirim ke klien menggunakan metode `send()`. Server kemudian menerima output dari klien setelah menjalankan perintah tersebut menggunakan metode `recv()`. Output tersebut kemudian dicetak untuk ditampilkan kepada pengguna.

# 4. **Penggunaan Encoding**: Skrip menggunakan encoding `iso8859-1` untuk mengonversi data yang dikirim melalui socket. Hal ini memastikan bahwa karakter-karakter khusus yang mungkin digunakan dalam output perintah dapat ditampilkan dengan benar.

# Tujuan utama dari skrip ini adalah untuk memberikan pengguna kemampuan untuk berinteraksi dengan server secara langsung melalui terminal dan menjalankan perintah pada mesin yang terhubung. Ini dapat berguna untuk administrasi jarak jauh, pengujian sistem, atau skenario lain di mana pengguna perlu berkomunikasi dengan server secara langsung melalui perintah.
