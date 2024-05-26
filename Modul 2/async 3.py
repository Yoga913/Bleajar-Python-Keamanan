# latihan kasus:
import asyncio

async def halo_dunia():
    print('Halo ...')
    await asyncio.sleep(1)
    print('... Dunia!')

asyncio.run(halo_dunia())
# ========================================================================
import aiohttp
import asyncio

async def main():

    async dengan aiohttp.ClientSession() sebagai session:

        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/1'
        async dengan session.get(pokemon_url) sebagai resp:
            pokemon = await resp.json()
            print(pokemon['name'])

asyncio.run(main())

# Dalam kode ini, dibuat sebuah coroutine bernama main, yang dijalankan
# dengan event loop asyncio. Di sini, kita memulai
# sebuah sesi klien aiohttp, sebuah objek unik yang dapat digunakan
# untuk berbagai permintaan individual dan, secara default,
# dapat terhubung dengan hingga 100 server berbeda sekaligus.
# Dengan sesi ini, kita membuat
# permintaan ke API Pokémon dan menunggu respons.
# ====================================================================
import aiohttp
import asyncio
import time

start_time = time.time()

async def main():

    async dengan aiohttp.ClientSession() sebagai session:

        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async dengan session.get(pokemon_url) sebagai resp:
                pokemon = await resp.json()
                print(pokemon['name'])

asyncio.run(main())
print("--- %s detik ---" % (time.time() - start_time))
# ====================================================================================
# Kali ini, kita juga akan menghitung durasi seluruh proses.

import aiohttp
import asyncio
import time

start_time = time.time()

async def get_pokemon(session, url):
    async dengan session.get(url) sebagai resp:
        pokemon = await resp.json()
        return pokemon['name']

async def main():

    async dengan aiohttp.ClientSession() sebagai session:

        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

asyncio.run(main())
print("--- %s detik ---" % (time.time() - start_time))

# Contoh ini menggunakan kode yang sepenuhnya non-blok, sehingga total waktu untuk menjalankan 150 permintaan
# akan hampir sama dengan waktu eksekusi permintaan yang paling lama.
# Angka pastinya bervariasi tergantung pada koneksi internet.


# note:Perhatikan bahwa kata kunci `as` dalam bahasa Inggris diganti dengan `sebagai` dalam bahasa Indonesia agar lebih mudah dipahami. Namun, dalam Python, kata kunci tetap harus dalam bahasa Inggris.
#  Kode ini menunjukkan bagaimana menggunakan coroutine dan asynchronous programming dalam Python untuk melakukan berbagai permintaan ke API secara efisien.

# Kode yang diberikan adalah contoh penggunaan asyncio dan aiohttp dalam Python. asyncio adalah modul dalam Python yang menyediakan infrastruktur untuk menulis kode asinkron (non-blok) menggunakan coroutine. Sedangkan aiohttp adalah klien HTTP asinkron untuk Python, yang memungkinkan kita untuk membuat permintaan HTTP secara efisien dalam lingkungan asinkron.

# Berikut adalah penjelasan singkat tentang setiap potongan kode:

# Contoh 1: Menunjukkan penggunaan asyncio untuk membuat sebuah coroutine yang mencetak "Halo ..." dengan jeda 1 detik, dan kemudian mencetak "... Dunia!" setelahnya.

# Contoh 2: Memperlihatkan cara menggunakan aiohttp untuk membuat permintaan HTTP ke API Pokemon. Coroutine main() membuat sebuah sesi klien dan kemudian melakukan permintaan GET ke API Pokemon untuk mendapatkan informasi tentang Pokemon pertama. Ini menunjukkan bagaimana kita dapat menggunakan aiohttp untuk melakukan permintaan HTTP secara asinkron.

# Contoh 3: Menunjukkan cara menggunakan aiohttp dan asyncio untuk melakukan banyak permintaan HTTP ke API Pokemon secara paralel. Coroutine main() membuat sebuah sesi klien dan kemudian membuat banyak coroutine untuk setiap permintaan ke API Pokemon. Coroutine get_pokemon() mengambil session dan URL, melakukan permintaan GET, dan mengembalikan nama Pokemon. Coroutine main() kemudian mengumpulkan hasilnya secara asinkron menggunakan asyncio.gather() dan mencetak nama-nama Pokemon yang diperoleh.

# Kode-kode ini merupakan contoh praktis penggunaan asynchronous programming dalam Python untuk menangani operasi I/O yang membutuhkan waktu, seperti permintaan HTTP ke server. Dengan menggunakan asyncio dan aiohttp, kita dapat membuat kode yang lebih efisien dan responsif dalam menangani permintaan I/O yang besar.
    
# ====================================================================================================================================
# berikuta adalah perbaikan dan kasus tujuan 

# ======================================================================================================================
# contoh 1:
import asyncio

async def halo_dunia():
    print('Halo ...')
    await asyncio.sleep(1)
    print('... Dunia!')

asyncio.run(halo_dunia())
# ============================================================================== 
# contoh 2:
import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/1'
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            print(pokemon['name'])

asyncio.run(main())


# Dalam kode ini, dibuat sebuah coroutine bernama main, yang dijalankan
# dengan event loop asyncio. Di sini, kita memulai
# sebuah sesi klien aiohttp, sebuah objek unik yang dapat digunakan
# untuk berbagai permintaan individual dan, secara default,
# dapat terhubung dengan hingga 100 server berbeda sekaligus.
# Dengan sesi ini, kita membuat
# permintaan ke API Pokémon dan menunggu respons.
# =======================================================================================
# contoh 3:
import aiohttp
import asyncio
import time

start_time = time.time()

async def main():
    async with aiohttp.ClientSession() as session:
        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])

asyncio.run(main())
print("--- %s detik ---" % (time.time() - start_time))
    
# kesalahan penulisan sintaks dalam bagian kode tersebut. Kata kunci async dan await seharusnya digunakan di luar blok async with.

# Dalam perbaikan ini, blok async with aiohttp.ClientSession() as session digunakan untuk membuat sesi klien, dan kemudian permintaan GET ke API Pokemon dilakukan di dalam loop for. 
# Di dalam loop, async with session.get(pokemon_url) as resp digunakan untuk melakukan permintaan GET, dan await resp.json() digunakan untuk mendapatkan respons JSON. Kemudian, nama Pokemon dicetak.
# =====================================================================================================
# Kali ini, kita juga akan menghitung durasi seluruh proses.
# contoh 4:
import aiohttp
import asyncio
import time

start_time = time.time()

async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

asyncio.run(main())
print("--- %s detik ---" % (time.time() - start_time))

# Contoh ini menggunakan kode yang sepenuhnya non-blok, sehingga total waktu untuk menjalankan 150 permintaan
# akan hampir sama dengan waktu eksekusi permintaan yang paling lama.
# Angka pastinya bervariasi tergantung pada koneksi internet.


# ========================================================================================================
# kesimpulan dari seluruh program : 

# Mari kita jelaskan setiap kode secara terpisah:

# 1. **Contoh 1 (halo_dunia)**:
#     - Ini adalah contoh sederhana dari asyncio yang menunjukkan bagaimana membuat dan menjalankan coroutine.
#     - Coroutine `halo_dunia()` mencetak "Halo ..." ke konsol, kemudian menunggu selama 1 detik menggunakan `asyncio.sleep(1)`, dan terakhir mencetak "... Dunia!".
#     - `asyncio.run(halo_dunia())` digunakan untuk menjalankan coroutine `halo_dunia()` dalam event loop asyncio.

# 2. **Contoh 2 (main)**:
#     - Ini adalah contoh penggunaan aiohttp untuk melakukan permintaan HTTP ke API Pokemon.
#     - Coroutine `main()` dibuat untuk melakukan permintaan ke API Pokemon menggunakan sesi klien aiohttp.
#     - Dalam blok `async with aiohttp.ClientSession() as session:`, sebuah sesi klien dibuat, dan kemudian permintaan GET dilakukan ke URL Pokemon untuk Pokemon pertama.
#     - Hasilnya adalah respons JSON yang berisi informasi Pokemon pertama, yang kemudian dicetak nama Pokemonnya.

# 3. **Contoh 3 (main dengan loop untuk 150 permintaan)**:
#     - Ini adalah contoh lain dari penggunaan aiohttp dan asyncio untuk melakukan banyak permintaan HTTP secara paralel.
#     - Coroutine `main()` membuat sesi klien aiohttp dan membuat daftar tugas untuk melakukan 150 permintaan ke API Pokemon.
#     - Setiap permintaan dilakukan dalam loop `for` menggunakan `session.get(url)` untuk mendapatkan respons JSON dari setiap Pokemon.
#     - Hasilnya adalah daftar nama Pokemon yang dicetak setelah semua permintaan selesai.

# 4. **Contoh 4 (main dengan non-blok untuk 150 permintaan)**:
#     - Ini adalah contoh lanjutan dari contoh sebelumnya, di mana kami menggunakan kode yang sepenuhnya non-blok untuk melakukan 150 permintaan HTTP secara paralel.
#     - Coroutine `get_pokemon()` dibuat untuk melakukan permintaan HTTP ke URL Pokemon tertentu dan mengembalikan nama Pokemon.
#     - Coroutine `main()` menggunakan `asyncio.gather()` untuk menunggu semua tugas selesai secara asinkron.
#     - Durasi waktu eksekusi keseluruhan proses dihitung menggunakan `time.time()` sebelum dan setelah menjalankan coroutine `main()`.

# Setiap contoh menunjukkan bagaimana menggunakan asyncio dan aiohttp untuk membuat kode yang efisien dalam menangani operasi I/O yang membutuhkan waktu, seperti permintaan HTTP ke server. Dengan menggunakan coroutine dan asynchronous programming, kita dapat melakukan operasi I/O secara paralel dan meminimalkan waktu tunggu, meningkatkan responsivitas dan kinerja aplikasi.

