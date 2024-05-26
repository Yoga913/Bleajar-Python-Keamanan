# Import modul analisis file PE
import pefile

def func5():
    # file = input("Select File: ")
    # pe = pefile.PE(file)
    # Meneruskan parameter pe.file dan menentukan exe yang akan digunakan
    pe = pefile.PE("test.exe")
    # Mencetak semua header file dalam format yang dapat dibaca manusia
    pe.print_info()
    # Di bawah ini, ia mencetak hexadesimal dari header DOS e_magic dan e_lfanew
    # print("e_magic : " + hex(pe.DOS_HEADER.e_magic)) # Mencetak bidang e_magic dari DOS_HEADER
    # print("e_lfnew : " + hex(pe.DOS_HEADER.e_lfanew)) # Mencetak bidang e_lfnew dari DOS_HEADER
    
    # e_magic → angka ajaib dari header DOS adalah 'MZ' (0x5a4d) dan 'MZ' merujuk pada Mark Zbikowski, pencipta format file eksekusi MS-DOS.
    # e_lfnew → pointer ke header PE (NT Header).
    # Untuk sebagian besar program Windows, header DOS berisi program DOS yang tidak melakukan apa-apa kecuali mencetak "Program ini tidak dapat dijalankan dalam mode DOS".
    
if __name__ == '__main__':
    func5()

# ====================================================================================================================================================================================== 
# Skrip ini bertujuan untuk menganalisis file PE (Portable Executable), yang merupakan format file yang digunakan oleh sistem operasi Windows untuk menjalankan program aplikasi. Berikut adalah maksud dan tujuan dari skrip ini:

# 1. **Import Modul `pefile`**: Skrip ini mengimpor modul `pefile`, yang digunakan untuk melakukan analisis terhadap file PE.

# 2. **Fungsi `func5`**: Fungsi ini adalah tempat di mana analisis file PE dilakukan. Pada bagian yang di-comment-out, ada kemungkinan untuk memilih file PE yang ingin dianalisis melalui masukan pengguna. Namun, dalam contoh ini, file "test.exe" telah ditentukan secara langsung.

# 3. **Menggunakan `pefile.PE`**: Dalam fungsi `func5`, file PE "test.exe" dibuka dan dipecah oleh `pefile.PE`, sehingga memungkinkan akses ke berbagai bagian dari file tersebut.

# 4. **Mencetak Informasi Header**: Metode `print_info()` digunakan untuk mencetak semua informasi header dari file PE dalam format yang dapat dibaca oleh manusia. Ini akan mencakup informasi seperti tipe arsitektur, entri titik, dan banyak lagi.

# 5. **Pengertian dari `e_magic` dan `e_lfanew`**: Dua informasi spesifik yang di-comment-out ("e_magic" dan "e_lfanew") memberikan pemahaman tentang struktur file PE. "e_magic" adalah angka ajaib di dalam header DOS yang menandakan bahwa file adalah file PE. "e_lfanew" adalah pointer ke bagian NT Header dalam file PE, yang penting karena NT Header berisi informasi lebih lanjut tentang file, termasuk direktori berbagai tabel dan entri titik.

# Tujuan utama dari skrip ini adalah untuk memberikan pemahaman dasar tentang struktur dan konten dari file PE yang diberikan. Ini bisa digunakan untuk tujuan analisis keamanan, penelitian malware, atau pemecahan masalah ketika bekerja dengan aplikasi Windows.
