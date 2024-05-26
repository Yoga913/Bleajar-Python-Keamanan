import smtplib 

try: 
    # Membuat sesi SMTP 
    smtp = smtplib.SMTP('smtp.mail.yahoo.com', 465) 

    # Menggunakan TLS untuk menambahkan keamanan 
    smtp.starttls() 

    # Otentikasi Pengguna 
    smtp.login("fsociety405@yahoo.com","Mrrobot#22")

    # Mendefinisikan Pesan 
    message = "Pesan_yang_ingin_anda_kirim" 

    # Mengirim Email
    smtp.sendmail("fsociety405@yahoo.com", "joasantonio109@gmail.com", message) 

    # Mengakhiri sesi 
    smtp.quit() 
    print ("Email terkirim dengan sukses!") 

except Exception as ex: 
    print("Ada kesalahan....", ex)

# Maksud dari kode ini adalah untuk mengirim email menggunakan protokol SMTP (Simple Mail Transfer Protocol). Kode ini mencoba untuk terhubung ke server SMTP Yahoo menggunakan alamat dan kata sandi yang disediakan, kemudian mengirimkan email dari alamat "fsociety405@yahoo.com" ke alamat "joasantonio109@gmail.com" dengan pesan yang telah ditentukan. Tujuannya adalah untuk mengirim email melalui program Python menggunakan modul `smtplib`.
