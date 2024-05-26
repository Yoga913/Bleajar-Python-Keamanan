# Import library requests
import requests
# Menetapkan variabel host
host = "http://testphp.vulnweb.com/"
# Menetapkan metode yang ada
metodos = ['OPTIONS', 'GET', 'POST', 'DELETE', 'TRACE', 'CONNECT']
# Membuat loop for untuk menguji setiap metode
for metodo in metodos:
    # Menguji setiap metode yang ada untuk melihat apakah berfungsi pada host
    response = requests.request(metodo, host)
    print(metodo, "->", response.reason)

# ========================================================================================== 
# Skrip ini digunakan untuk melakukan pengujian terhadap berbagai metode HTTP yang didukung oleh sebuah host. Berikut adalah maksud dan tujuan dari skrip ini:

# 1. **Import Library `requests`**: Skrip ini mengimpor library `requests`, yang digunakan untuk melakukan permintaan HTTP.

# 2. **Variabel Host**: Variabel `host` menentukan URL host yang akan diuji. Dalam contoh ini, host yang digunakan adalah "http://testphp.vulnweb.com/", tetapi bisa diganti dengan host lain yang ingin diuji.

# 3. **Metode yang Ada**: Daftar `metodos` (metode) berisi berbagai metode HTTP yang akan diuji. Ini termasuk OPTIONS, GET, POST, DELETE, TRACE, dan CONNECT. Setiap metode akan diuji satu per satu untuk melihat apakah mereka didukung oleh host yang ditentukan.

# 4. **Loop For**: Skrip menggunakan loop `for` untuk menguji setiap metode HTTP yang ada dalam daftar `metodos`. Setiap metode diuji dengan mengirimkan permintaan HTTP ke host yang ditentukan menggunakan metode tersebut.

# 5. **Mencetak Hasil**: Setelah menerima respons dari host untuk setiap metode, skrip mencetak hasilnya. Ini mencakup metode yang diuji dan alasan respons yang diberikan oleh host.

# Tujuan utama dari skrip ini adalah untuk menguji apakah berbagai metode HTTP dapat digunakan untuk berinteraksi dengan host yang ditentukan. Hal ini dapat membantu dalam mengidentifikasi potensi kerentanan atau konfigurasi server yang tidak aman, serta memastikan bahwa host mendukung metode HTTP yang diharapkan.
