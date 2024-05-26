# prn memungkinkan Anda untuk meneruskan sebuah fungsi yang akan dijalankan setiap kali paket disniff. Tujuan dari fungsi ini adalah mengontrol bagaimana paket dicetak di konsol, memungkinkan Anda mengganti format cetak standar paket dengan format pilihan Anda

# Untuk membuat program/skrip Anda memformat dan mengembalikan informasi paket sesuai keinginan Anda, 
# fungsi sniff meneruskan objek paket sebagai satu-satunya argumen ke fungsi yang Anda tentukan dalam argumen prn dari sniff

# Lambda mengambil konten dan memformatnya sebagai string

# sniff

sniff(count=4)
a = _
a.summary()
sniff(count=4, prn=lambda x: x.summary())
sniff(iface="enp0s3", prn=lambda x: x.summary())
sniff(count=1, iface="enp0s3", prn=lambda x: x.show())

# membaca pcaps

scapy
p = rdpcap("contoh.pcap")
p
len(p)
pkt = p[1000] # mencetak paket nomor 1000
pkt 
type(pkt)
dir(pkt)
lsc()
hexdump(pkt)
ls(pkt)
pkt.summary()
pkt.show()

# =======================================
# kesimpulan

Kode tersebut menjelaskan penggunaan fungsi `sniff()` dalam modul Scapy untuk memantau dan menganalisis lalu lintas jaringan. 

Maksud dari kode tersebut adalah:

1. Menjelaskan konsep argumen `prn` yang diterima oleh fungsi `sniff()`, yang memungkinkan kita untuk meneruskan sebuah fungsi yang akan dijalankan setiap kali paket disniff.
2. Menggambarkan penggunaan fungsi lambda untuk mencetak ringkasan atau tampilan dari setiap paket yang ditangkap.
3. Menunjukkan contoh pemantauan lalu lintas jaringan dengan berbagai opsi seperti jumlah paket yang ingin ditangkap dan antarmuka jaringan yang digunakan.

Tujuan dari kode tersebut adalah memberikan pemahaman tentang bagaimana menggunakan fungsi `sniff()` untuk memantau lalu lintas jaringan, serta bagaimana menggunakan argumen `prn` untuk mengontrol cara informasi paket dicetak di konsol. Dengan demikian, kita dapat menyesuaikan format cetak paket sesuai kebutuhan analisis atau debugging jaringan yang sedang dilakukan.