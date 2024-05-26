# Ini dijalankan begitu objek dari sebuah kelas diinstansiasi. Metode ini berguna untuk melakukan
# inisialisasi apa pun yang ingin Anda lakukan dengan objek Anda.
class Orang:
    def __init__(self, nama):
        self.nama = nama
    def __str__(self):
        return self.nama
# Self merujuk pada atribut dari sebuah instance

joas = Orang('Joas')
print(joas)
michael = Orang('Michael')
print(michael)
lucas = Orang('Lucas')
print(lucas)

class Anjing:
 
    # Kelas sederhana
    # Mari kita buat dua atribut dengan nama anjing
    attr1 = "spike"
    attr2 = "bob"
 
    # Gunakan metode sederhana untuk merujuk atribut
    def fun(self):
        print("Aku adalah", self.attr1)
        print("Aku adalah", self.attr2)
 
 
# Variabel dengan nama anjing, mengirimkan
# objek Anjing
namaanjing = Anjing()
 
# Mengakses atribut kelas
# dan metode melalui objek, melewati fungsi fun dengan objek Anjing
print(namaanjing.attr1)
print(namaanjing.attr2)
namaanjing.fun()

# ================================================================================== 
# kesimpulan : 

# Kode tersebut adalah contoh Python yang menciptakan dua kelas, yaitu `Pessoa` (Orang dalam Bahasa Indonesia) dan `Dog` (Anjing dalam Bahasa Indonesia). Berikut adalah penjelasan dari setiap bagian kode:

# 1. **Kelas Pessoa**:
#    - Ini adalah definisi dari kelas `Pessoa` yang memiliki dua metode, yaitu `__init__` dan `__str__`.
#    - `__init__` adalah metode khusus yang disebut sebagai constructor. Metode ini dijalankan secara otomatis ketika objek dari kelas `Pessoa` dibuat (diinstansiasi). Metode ini menerima parameter `nome` yang merupakan nama dari orang tersebut, kemudian menyimpannya dalam atribut `self.nome`.
#    - `__str__` adalah metode khusus yang menggantikan representasi string bawaan dari objek. Metode ini mengembalikan nilai dari atribut `self.nome`, sehingga ketika objek `Pessoa` dicetak, nama orangnya akan ditampilkan.

# 2. **Instansiasi Objek `Pessoa`**:
#    - Tiga objek `Pessoa` dibuat, yaitu `joas`, `michael`, dan `lucas`, masing-masing dengan nama `'Joas'`, `'Michael'`, dan `'Lucas'`.
#    - Setelah objek dibuat, metode `__str__` akan dipanggil secara otomatis saat objek tersebut dicetak, sehingga nama orangnya akan ditampilkan.

# 3. **Kelas Anjing**:
#    - Ini adalah definisi dari kelas `Anjing` yang memiliki satu metode, yaitu `fun`.
#    - Dalam kelas ini, ada dua atribut kelas, yaitu `attr1` dan `attr2`, yang mewakili nama anjing.
#    - Metode `fun` mencetak nama anjing yang disimpan dalam atribut kelas.

# 4. **Instansiasi Objek `Anjing`**:
#    - Objek `Anjing` dengan nama `namedog` dibuat.
#    - Atribut kelas `attr1` dan `attr2` dicetak.
#    - Metode `fun` dipanggil dengan objek `namedog`, yang mencetak nama anjing dari atribut kelas.

# Maksud dan tujuan dari kode ini adalah untuk mendemonstrasikan konsep dasar dari OOP (Object-Oriented Programming) dalam Python, termasuk pembuatan kelas, konstruktor, atribut kelas, dan metode. Kode ini menunjukkan cara membuat objek dari kelas-kelas yang telah didefinisikan, mengakses atribut kelas, dan memanggil metode dari objek tersebut.
