import aiohttp
import asyncio

async def main():
    # Pertama, kita mendefinisikan sesi klien dengan aiohttp:
    async with aiohttp.ClientSession() as session:
        # Selanjutnya, dengan sesi kita, kita melakukan permintaan get pada satu URL:
        async with session.get('http://python.org') as response:
            print("Status:", response.status)
            print("Jenis Konten:", response.headers['content-type'])
            # Ketiga, perhatikan bagaimana kita menggunakan kata kunci await di depan response.text() seperti ini:
            # response.text mengembalikan konten respons dalam bentuk unicode. Ini mengacu pada konten respons biner. 
            #Permintaan Python umumnya digunakan untuk mengambil konten dari URI sumber tertentu. 
            #Setiap kali kita melakukan permintaan ke URI tertentu melalui Python, itu mengembalikan objek respons. 
            #Sekarang, objek respons ini akan digunakan untuk mengakses sumber daya tertentu, seperti konten, header, dll.
            html = await response.text()
            print("Isi:", html[:15], "...")
            # Terakhir, itu menampilkan jenis konten dan khususnya baris ke-15, kita bisa meminta untuk menampilkan dari baris 5:15 dan mengabaikan 5 digit pertama.

# await: Ini berarti bahwa coroutine akan dijeda pada titik itu menunggu hasil yang akan datang. Dengan kata lain,
# kontrol eksekusi akan diberikan kepada coroutine lain dan hanya akan dilanjutkan ketika hasilnya siap.
# Akhirnya kita menjalankan asyncio.run(main()), ini membuat loop event dan mengeksekusi semua tugas di dalamnya.
#Setelah semua tugas selesai, loop event akan dihancurkan secara otomatis.
asyncio.run(main())


# Maksud dari kode ini adalah untuk melakukan permintaan HTTP GET ke situs web tertentu (`http://python.org` dalam kasus ini) menggunakan pustaka `aiohttp`, yang memungkinkan operasi asinkron. Setelah mendapatkan tanggapan dari situs web, kode ini mencetak status respons, jenis konten, dan sebagian kecil dari isi halaman web tersebut. Tujuannya adalah untuk mendemonstrasikan penggunaan `aiohttp` untuk mengambil konten dari situs web secara asinkron.
