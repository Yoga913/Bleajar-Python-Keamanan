from pywebcopy import save_webpage

# 
kwargs = {'project_name': 'folder situs'}
 
save_webpage(
   
    # URL situs web
    url='http://pudim.com.br/',
     
    # Direktori tempat situs akan disimpan
    project_folder='pycopy/',
    **kwargs
    # **kwargs adalah argumen bernama
    # yang memungkinkan Anda meneruskan sejumlah argumen yang tidak ditentukan ke fungsi.
    # Dengan cara ini, saat menulis fungsi, Anda tidak perlu menentukan berapa banyak argumen yang akan diteruskan ke fungsi Anda.
 # **kwargs memungkinkan kita untuk memeriksa parameter bernama fungsi, yaitu, parameter yang diteruskan dengan nama!
# Mereka akan tersedia sebagai kamus ({'kunci': 'nilai'}) di dalam fungsi.
)
# ============================================================================================================================================ 
# kesimpulan : 

# Skrip ini bertujuan untuk menyimpan salinan lokal dari situs web tertentu ke dalam folder yang ditentukan. Berikut adalah maksud dan tujuan dari skrip ini:

# 1. **Import Modul `save_webpage`**: Skrip ini mengimpor fungsi `save_webpage` dari modul `pywebcopy`, yang digunakan untuk menyimpan salinan lokal dari situs web.

# 2. **Konfigurasi Argument**: Skrip ini menyiapkan sebuah kamus (`kwargs`) yang berisi argumen-argumen bernama yang akan diteruskan ke fungsi `save_webpage`. Dalam contoh ini, argumen bernama yang ditentukan adalah `project_name`, yang menentukan nama proyek folder.

# 3. **Panggilan Fungsi `save_webpage`**: Fungsi `save_webpage` dipanggil dengan parameter-parameter berikut:
#    - `url`: URL dari situs web yang akan disalin.
#    - `project_folder`: Direktori tempat salinan situs web akan disimpan.
#    - `**kwargs`: Argumen-argumen bernama tambahan yang diteruskan ke fungsi, dalam hal ini adalah `project_name`.

# 4. **Tujuan**: Tujuan utama dari skrip ini adalah untuk mengunduh dan menyimpan salinan dari situs web yang diberikan ke dalam folder lokal. Ini dapat berguna dalam skenario seperti membuat salinan cadangan situs web, mengumpulkan data untuk analisis, atau menjalankan situs web secara lokal untuk pengujian atau pengembangan. Dengan menggunakan fungsi ini, pengguna dapat dengan mudah membuat salinan dari situs web yang diinginkan dan menyimpannya ke dalam struktur folder yang ditentukan.
