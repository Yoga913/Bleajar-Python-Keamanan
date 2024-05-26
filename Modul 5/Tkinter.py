from tkinter import *

class Aplikasi:
    def __init__(self, master=None):
        self.fontStandar = ("Arial", "10")
        self.kontainerPertama = Frame(master)
        self.kontainerPertama["pady"] = 10
        self.kontainerPertama.pack()

        self.kontainerKedua = Frame(master)
        self.kontainerKedua["padx"] = 20
        self.kontainerKedua.pack()

        self.kontainerKetiga = Frame(master)
        self.kontainerKetiga["padx"] = 20
        self.kontainerKetiga.pack()

        self.kontainerKeempat = Frame(master)
        self.kontainerKeempat["pady"] = 20
        self.kontainerKeempat.pack()

        self.judul = Label(self.kontainerPertama, text="Data Pengguna")
        self.judul["font"] = ("Arial", "10", "bold")
        self.judul.pack()

        self.labelNama = Label(self.kontainerKedua, text="Nama", font=self.fontStandar)
        self.labelNama.pack(side=LEFT)

        self.inputNama = Entry(self.kontainerKedua)
        self.inputNama["width"] = 30
        self.inputNama["font"] = self.fontStandar
        self.inputNama.pack(side=LEFT)

        self.labelSandi = Label(self.kontainerKetiga, text="Sandi", font=self.fontStandar)
        self.labelSandi.pack(side=LEFT)

        self.inputSandi = Entry(self.kontainerKetiga)
        self.inputSandi["width"] = 30
        self.inputSandi["font"] = self.fontStandar
        self.inputSandi["show"] = "*"
        self.inputSandi.pack(side=LEFT)

        self.tombolAutentikasi = Button(self.kontainerKeempat)
        self.tombolAutentikasi["text"] = "Autentikasi"
        self.tombolAutentikasi["font"] = ("Calibri", "8")
        self.tombolAutentikasi["width"] = 12
        self.tombolAutentikasi["command"] = self.verifikasiSandi
        self.tombolAutentikasi.pack()

        self.pesan = Label(self.kontainerKeempat, text="", font=self.fontStandar)
        self.pesan.pack()

    # Metode verifikasi sandi
    def verifikasiSandi(self):
        pengguna = self.inputNama.get()
        sandi = self.inputSandi.get()
        if pengguna == "pengguna" and sandi == "sandi":
            self.pesan["text"] = "Terautentikasi"
        else:
            self.pesan["text"] = "Kesalahan saat otentikasi"


root = Tk()
Aplikasi(root)
root.mainloop()

# ============================================================================= 
# Maksud dan tujuan dari kode tersebut adalah untuk membuat sebuah aplikasi sederhana menggunakan modul Tkinter dalam bahasa pemrograman Python. Aplikasi ini bertujuan untuk meminta pengguna memasukkan nama pengguna dan sandi, dan kemudian mengautentikasi masukan tersebut. Jika nama pengguna dan sandi yang dimasukkan cocok dengan nilai yang telah ditentukan (`pengguna` dan `sandi`), maka aplikasi akan menampilkan pesan "Terautentikasi". Namun, jika masukan tidak cocok, maka akan ditampilkan pesan "Kesalahan saat otentikasi".

# Tujuan dari aplikasi ini mungkin untuk memperkenalkan pemrograman antarmuka grafis (GUI) menggunakan Tkinter kepada pengguna, serta memperkenalkan konsep dasar autentikasi pengguna. Aplikasi ini bisa dijadikan sebagai dasar untuk pengembangan aplikasi yang lebih kompleks di masa depan.
