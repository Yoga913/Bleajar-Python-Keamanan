# Instruksi With
# Instruksi with digunakan untuk menjamin penyelesaian sumber daya yang diperoleh.
# Misalnya: ketika sebuah file dibuka, kita bisa menggunakan try dan finally,
# untuk menjalankan logika kita dan kemudian menutup file tersebut.

#with open('readme.txt', 'w') sebagai f:
#    f.write('readme')

#lines = ['Readme', 'Cara menulis file teks di Python']
#with open('readme.txt', 'w') sebagai f:
# Loop for memungkinkan kita membaca baris per baris
#    for line in lines:
#        f.write(line)
#        f.write('\n')

# 'a' adalah untuk menambahkan
#more_lines = ['', 'Menambahkan teks pada file', 'Akhir']
#with open('readme.txt', 'a') sebagai f:
#    f.write('\n'.join(more_lines))

# Membaca dan mencetak isi file
#f = open("readme.txt", "r")
#print(f.read())

#with open('readme.txt') sebagai f:
#    lines = f.readlines()
#    print(lines)
