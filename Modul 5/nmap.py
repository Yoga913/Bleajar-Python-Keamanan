# pip install python-nmap
import nmap 

# Mulai dari port 75
mulai = 75
akhir = 443
target = '127.0.0.1'

# Di sini kita memanggil fungsi port scanner dari pustaka nmap
scanner = nmap.PortScanner() 

# Kami membuat loop for untuk melakukan pemindaian pada setiap port
for i in range(mulai, akhir + 1): 
   
    hasil = scanner.scan(target, str(i))     
    
    hasil = hasil['scan'][target]['tcp'][i]['state'] 
   
    print(f'port {i} is {hasil}.') 

# ====================================================================================== 
# Kode tersebut bertujuan untuk melakukan pemindaian (scanning) port pada sebuah host dengan menggunakan pustaka Python bernama `python-nmap`, yang merupakan antarmuka untuk program Nmap (Network Mapper), sebuah alat untuk pemindaian jaringan dan audit keamanan. Berikut adalah maksud dan tujuan dari setiap bagian kode:

# 1. `import nmap`: Mengimpor modul `nmap` yang memungkinkan akses ke fitur-fitur Nmap dalam Python.

# 2. `mulai = 75`, `akhir = 443`: Menentukan rentang port yang akan dipindai, dimulai dari port 75 hingga port 443.

# 3. `target = '127.0.0.1'`: Menentukan host yang akan dipindai. Dalam kasus ini, host yang ditentukan adalah localhost (127.0.0.1), yang merupakan alamat jaringan loopback.

# 4. `scanner = nmap.PortScanner()`: Membuat objek `PortScanner` dari modul `nmap`, yang akan digunakan untuk melakukan pemindaian port.

# 5. `for i in range(mulai, akhir + 1):`: Membuat loop `for` untuk melakukan pemindaian pada setiap port dalam rentang yang ditentukan.

# 6. `hasil = scanner.scan(target, str(i))`: Melakukan pemindaian pada port tertentu pada host yang ditentukan, menggunakan metode `scan` dari objek `PortScanner`. Hasil pemindaian disimpan dalam variabel `hasil`.

# 7. `hasil = hasil['scan'][target]['tcp'][i]['state']`: Mengambil status (open, closed, filtered, etc.) dari port yang dipindai dari hasil pemindaian dan menyimpannya dalam variabel `hasil`.

# 8. `print(f'port {i} is {hasil}.')`: Mencetak hasil pemindaian untuk setiap port dalam format yang sesuai, menampilkan nomor port dan statusnya.

# Tujuan dari kode ini adalah untuk memberikan informasi tentang status port tertentu pada host yang ditentukan, sehingga pengguna dapat memahami kondisi keamanan jaringan dan melakukan tindakan yang sesuai jika diperlukan.
