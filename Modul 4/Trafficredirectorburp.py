# -*- coding: utf-8 -*-

# Bibliotek API
from burp import IBurpExtender
# Bibliotek untuk komunikasi HTTP
from burp import IHttpListener
from java.io import PrintWriter

# Tentukan host sumber
HOST_FROM = "127.0.0.1"
# Tentukan host tujuan
HOST_TO = "www.google.com"

# Membuat kelas BurpExtender yang mengimplementasikan IBurpExtender dan IHttpListener
class BurpExtender(IBurpExtender, IHttpListener):

    #
    # Implementasi IBurpExtender 
    #
    
    def registerExtenderCallbacks(self, callbacks):
        # Dapatkan objek bantuan ekstensi
        self._helpers = callbacks.getHelpers()
        
        # Tentukan nama ekstensi
        callbacks.setExtensionName("Traffic redirector")

        # Aktifkan mode Debug untuk mengumpulkan keluaran dan masukan kesalahan
        self.stdout = PrintWriter(callbacks.getStdout(), True);
        self.stdout.println("DEBUG: Aktif!")
        
        # Daftarkan pendengar HTTP
        callbacks.registerHttpListener(self)

    #
    # Implementasi IHttpListener
    #
    
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        # Cetak masuk ke fungsi processHttpMessage untuk debug        
        self.stdout.println("DEBUG: Memasuki fungsi processHttpMessage") 
        # Hanya proses permintaan
        if not messageIsRequest:
            self.stdout.println("Debug: Ini bukan permintaan, hentikan proses")
            return

        # Dapatkan layanan HTTP untuk permintaan dan ambil informasinya
        httpService = messageInfo.getHttpService()
        self.stdout.print("Debug: httpservice ")
        self.stdout.println(httpService)
        self.stdout.print("Debug: httpservice.gethost() ")
        self.stdout.println(httpService.getHost())
        self.stdout.print("Debug: HOST_TO")
        self.stdout.println(HOST_TO)
        self.stdout.print("Debug: HOST_FROM ")
        self.stdout.println(HOST_FROM)
        
        # Jika host adalah HOST_FROM, ubah menjadi HOST_TO
        if (HOST_FROM == httpService.getHost()):
            self.stdout.println("Debug: HOST_TO dan HOST_FROM adalah server yang sama")
            # Bangun layanan http dan lakukan pengalihan
            messageInfo.setHttpService(self._helpers.buildHttpService(HOST_TO,
                httpService.getPort(), httpService.getProtocol()))
            self.stdout.println("Debug: Jika HOST_FROM, ubah menjadi HOST_TO ")
            self.stdout.println(httpService)

# ==================================================================================================== 
# kesimpulan : 

# Skrip ini bertujuan untuk membuat ekstensi (plugin) untuk Burp Suite yang akan memungkinkan pengguna untuk melakukan pengalihan lalu lintas (traffic redirection) dari satu host ke host lainnya. Berikut adalah maksud dan tujuan dari skrip ini:

# 1. **Implementasi Ekstensi Burp**: Skrip ini mengimplementasikan antarmuka `IBurpExtender` dan `IHttpListener`, yang diperlukan untuk membuat ekstensi Burp Suite. Ini menunjukkan bahwa skrip ini dimaksudkan untuk digunakan sebagai ekstensi Burp Suite dan akan berinteraksi dengan lalu lintas HTTP.

# 2. **Pengaturan Host**: Skrip ini menetapkan dua variabel `HOST_FROM` dan `HOST_TO`, yang menentukan host sumber dan tujuan untuk pengalihan lalu lintas. Tujuan pengalihan ini adalah untuk mengarahkan lalu lintas dari host sumber ke host tujuan.

# 3. **Registrasi dan Inisialisasi Ekstensi**: Metode `registerExtenderCallbacks` digunakan untuk mendaftarkan ekstensi dengan Burp Suite. Di dalamnya, nama ekstensi ditetapkan dan pendengar HTTP didaftarkan untuk memantau lalu lintas HTTP yang masuk dan keluar.

# 4. **Pemrosesan Pesan HTTP**: Metode `processHttpMessage` digunakan untuk memproses setiap pesan HTTP yang melewati proxy Burp Suite. Dalam metode ini, skrip memeriksa apakah host dari pesan HTTP adalah `HOST_FROM`. Jika ya, maka skrip akan mengubah host dalam pesan HTTP menjadi `HOST_TO`, sehingga mengalihkan lalu lintas ke host tujuan yang ditentukan.

# 5. **Debugging dan Logging**: Skrip ini mencetak pesan debug untuk membantu pemantauan dan pemecahan masalah. Ini membantu pengembang untuk memahami alur kerja dan mengidentifikasi masalah saat menjalankan ekstensi.

# Tujuan utama dari skrip ini adalah untuk memberikan pengguna kemampuan untuk mengarahkan lalu lintas HTTP dari satu host ke host lainnya menggunakan Burp Suite. Ini dapat berguna dalam skenario pengujian penetrasi, analisis keamanan, dan penanganan lalu lintas untuk keperluan debugging atau analisis.
