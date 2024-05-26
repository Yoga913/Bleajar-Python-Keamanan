# Variabel umur adalah 61
umur = 61
if umur < 12:
    print("anak-anak")
elif umur < 18:
    print("remaja")
elif umur < 60:
    print("dewasa")
else:
    print("lansia")

# Di sini kita membuat sebuah loop, di mana nilai yang dimasukkan terus benar, program tidak akan berhenti sampai menekan CTRL+C
while True:
    print("Program Sederhana")
    print("1- Mendaftar\n")
    print("2- Kredit\n")
    print("3- Latihan")
    menu = str(input("Masukkan pilihan yang diinginkan: "))
    if menu == "1":
        print("\nSelamat datang di Pendaftaran")
        bagian1 = str(input("Siapa nama Anda? "))
        print(bagian1)
        bagian2 = int(input("Berapa umur Anda? "))
        print(bagian2)
        bagian3 = float(input("Berapa tinggi Anda? "))
        print(bagian3)
        print("\n SELAMAT DATANG!")
    elif menu == "2":
        print("\n Dibuat oleh Joas")
    elif menu == "3":
        print("\n Buatlah program serupa dengan ini, yang melakukan pendaftaran orang dan ada interaksi antara orang tersebut dengan program setelah melakukan pendaftaran")
