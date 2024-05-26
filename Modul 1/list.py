# Mari kita buat sebuah daftar sederhana
daftar = ['Mobil', 'ikan', 123, 111, True]
print(daftar)

# Mari kita buat daftar baru dan menambahkan daftar sebelumnya
daftar_baru = ['batu', daftar]
print(daftar_baru)

# MENGAKSES ELEMEN MENGGUNAKAN SINTAKS DAN INDEKS
print(daftar[0])
print(daftar[1])
print(daftar[2])
print(daftar[3])
print(daftar[4])

print(daftar_baru[0])
print(daftar_baru[1][2])

# Panjang sebuah daftar
print(len(daftar))
print(len(daftar_baru))

# Menggabungkan dan mengulangi daftar
print(daftar + daftar_baru)
print(daftar * 3)

# Memeriksa keberadaan sebuah informasi dalam sebuah daftar
ada1 = 'ikan' in daftar
ada2 = 'kucing' in daftar
ada3 = 'felipe' in daftar

print(ada1)
print(ada2)
print(ada3)

# Menemukan nilai terkecil, nilai terbesar, dan menjumlahkan semuanya kemudian
angka = [14.55, 67, 89.88, 10, 21.5]
print(min(angka))
print(max(angka))
print(sum(angka))
print(angka)

programmer = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(type(programmer)) # type 'list'
print(len(programmer)) # 5
print(programmer[4]) # Luana

programmer = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(programmer) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']

programmer.append('Renato')
print(programmer) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana', 'Renato']

programmer = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
programmer.insert(1, 'Rafael')

print(programmer) # ['Victor', 'Rafael', 'Juliana', 'Samuel', 'Caio', 'Luana']
