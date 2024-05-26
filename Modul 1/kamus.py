# Membuka variabel data_pelanggan
# Menambahkan informasi, nama, alamat, dan telepon dipisahkan dengan :
data_pelanggan = {
    'Nama': 'Renan',
    'Alamat': 'Jalan Cruzeiro do Sul',
    'Telepon': '982503645'
}

# Sekarang kita akan menampilkan hanya yang ada di dalam kamus yang mengacu pada nama
# Maka ia akan menampilkan nama Renan
print(data_pelanggan['Nama']) # Renan

# Sekarang kita akan menampilkan semua data dari sebuah kamus
data_pelanggan2 = {
    'Nama': 'Renan',
    'Alamat': 'Jalan Cruzeiro do Sul',
    'Telepon': '982503645'
}

print(data_pelanggan2) # {'Nama': 'Renan', 'Alamat': 'Jalan Cruzeiro do Sul', 'Telepon': '982503645'}

# Menambahkan umur ke dalam kamus dengan nilai 40
data_pelanggan2['Umur'] = 40

# Mencetak
print(data_pelanggan2)
