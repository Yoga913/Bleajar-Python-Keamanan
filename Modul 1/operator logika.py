# COMPARATOR == >= <= != < >

# ==	identik
# !=	tidak sama
# >	lebih besar
# <	lebih kecil
# >=	lebih besar atau sama dengan
# <=	lebih kecil atau sama dengan

var = 5

if var == 5:
    print('Nilainya sama')

if var != 7:
    print('Nilainya berbeda dari 7')

if var > 2:
    print('Nilai variabel lebih besar dari 2')

if var >= 5:
    print('Nilai variabel lebih besar atau sama dengan 5')

if var < 7:
    print('Nilai variabel lebih kecil dari 7')

if var <= 5:
    print('Nilai variabel lebih kecil atau sama dengan 5')


# and	Mengembalikan True jika kedua pernyataan benar
# or	Mengembalikan True jika salah satu pernyataan benar
# not	Mengembalikan False jika hasilnya benar

num1 = 7
num2 = 4

# Contoh and
# Jika num1 lebih besar dari 3 dan num2 lebih kecil dari 8
if num1 > 3 and num2 < 8:
    print("Kedua kondisi benar")

# Jika num1 lebih besar dari 4 atau num2 lebih kecil atau sama dengan 8
# Contoh or
if num1 > 4 or num2 <= 8:
    print("Satu atau kedua kondisi benar")

# Jika num1 tidak lebih besar dari 8 dan num2 tidak lebih kecil dari 8
# Contoh not
if not (num1 > 8 and num2 < 8):
    print('Salah satu kondisi salah')
