#pip install pyelftools
# Mengimpor modul os ELFFile untuk menganalisis file ELF
from elftools.elf.elffile import ELFFile
# Dan modul capstone yang membantu dalam disassembler
from capstone import *

print("JOAS ANTONIO")
# Di bawah ini saya pilih file yang akan dibuka dan dibaca
with open('.\test.elf', 'rb') as f:   #ubah nama file sesuai dengan yang Anda lakukan pada rekayasa balik
    # di sini ia akan membuka file elffile 
    elf = ELFFile(f)
    # mengumpulkan bagian .text yang mengembalikan potongan terkait kode
    code = elf.get_section_by_name('.text')
    # merupakan referensi ke instruksi yang dimiliki oleh prosesor tertentu untuk melakukan tugas tertentu.
    ops = code.data()                 # mengembalikan string byte dengan opcodes
    # Jika bagian ini muncul dalam gambar memori proses, anggota ini berisi alamat di mana byte pertama dari bagian harus berada.
    addr = code['sh_addr']            # alamat awal dari `.text`
    # Definisi arsitektur aplikasi, baik dikompilasi dalam x86 atau x64
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    for i in md.disasm(ops, 0x7aa):    # melintasi setiap opcode
        # Di sini ia akan membawa opcodes, baik alamat memori
# mnemonik digunakan untuk menentukan opcode yang mewakili instruksi bahasa mesin lengkap dan operasional
# Akhirnya, representasi objek
        print(f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}") #mengembalikan setiap opcode, alamat, string, dan menomonic yang merupakan instruksi

# ===============================================================================================================================================================
# kesimpulan :

# Skrip ini dirancang untuk menganalisis dan mengekstrak informasi dari sebuah file dalam format ELF (Executable and Linkable Format), yang merupakan format umum untuk file biner dalam lingkungan Linux dan Unix. Tujuan utama dan maksud dari skrip ini adalah sebagai berikut:

# 1. **Analisis File ELF**: Skrip ini membuka sebuah file ELF (`test.elf`), yang biasanya merupakan program atau file biner lainnya yang ditujukan untuk dieksekusi pada sistem Linux atau Unix.

# 2. **Ekstraksi Bagian .text**: Skrip ini mengambil bagian `.text` dari file ELF. Bagian `.text` umumnya berisi kode eksekusi dari program, yang akan diuraikan lebih lanjut oleh skrip.

# 3. **Disassembler**: Skrip ini menggunakan Capstone, sebuah pustaka disassembler, untuk menguraikan opcodes dalam bagian `.text`. Proses disassembly mengonversi instruksi mesin (opcodes) menjadi representasi teks yang lebih mudah dipahami manusia, seperti mnemonic dan operan.

# 4. **Iterasi melalui Opcodes**: Skrip ini melintasi setiap opcode dalam bagian `.text` dari file ELF dan mencetak informasi penting tentang setiap instruksi. Informasi ini termasuk alamat opcode dalam format heksadesimal, mnemonic (kode operasi), dan operan (argumen) yang terkait dengan instruksi tersebut.

# Dengan demikian, skrip ini berguna untuk analisis keamanan, pemecahan masalah, atau pemahaman lebih lanjut tentang bagaimana program bekerja di tingkat instruksi mesin. Ini bisa digunakan oleh peneliti keamanan, insinyur revers, atau pengembang yang tertarik dalam memahami implementasi internal dari sebuah program atau sistem.
