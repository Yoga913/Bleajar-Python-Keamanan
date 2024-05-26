from scapy.all import *

ans = input("Masukkan IP: ")

ip = IP()
ping = ICMP()
ip.dst = ans
reply = sr1(ip/ping)
if reply.ttl < 65:
    os = "linux"
else:
    os = "windows"
print(" Sistem operasi adalah: " + os)

# =======================================================
# kesimpulan : 
# Kode tersebut bertujuan untuk mendeteksi sistem operasi dari sebuah host yang diidentifikasi melalui alamat IP yang dimasukkan oleh pengguna.

# Maksud dari kode tersebut adalah:

# 1. Menggunakan modul Scapy untuk melakukan operasi pemindaian jaringan dan analisis paket.
# 2. Meminta pengguna untuk memasukkan alamat IP tujuan.
# 3. Membangun paket IP dan ICMP untuk melakukan ping ke alamat IP yang dimasukkan.
# 4. Mengirimkan paket ping menggunakan fungsi `sr1()` dan menunggu balasan.
# 5. Berdasarkan nilai TTL (Time-To-Live) yang diterima dari balasan ping, menentukan sistem operasi host tersebut. TTL yang lebih rendah biasanya menunjukkan sistem operasi Linux, sedangkan TTL yang lebih tinggi cenderung menunjukkan sistem operasi Windows.
# 6. Mencetak informasi sistem operasi ke layar.

# Tujuan dari kode tersebut adalah memberikan fungsionalitas untuk mendeteksi sistem operasi dari sebuah host dengan menggunakan teknik ping dan analisis paket. Ini dapat digunakan sebagai alat bantu dalam pengelolaan jaringan atau penelitian keamanan untuk mengetahui sistem operasi host yang sedang beroperasi.
