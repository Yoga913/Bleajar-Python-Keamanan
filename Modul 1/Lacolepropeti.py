for i in range(100): # Ia menyimpan di i nilai dari 0 hingga 99
    print(i) # Di sini ia menampilkan di layar hingga nilai 99, setelah itu berhenti

i = 0 # Setiap kali masuk ke dalam While, ia melewati i = 0 ini, artinya selama i = 0 ia akan bekerja dengan loop
# jika saya memasukkan i = 1500, ia hanya akan mencetak nilai 5 sekali
while True: # Ia masuk ke dalam loop selama nilainya True, ketika nilainya tidak True ia akan menghentikan loop ini
    print("5") # Saya akan mencetak angka 5
    if i == 1500: # Di sini ia mencetak angka 5 sebanyak 1500 kali
        break # Ia menghentikan struktur loop ketika i sama dengan 1500, artinya ketika angka 5 telah dicetak 1500 kali ia akan berhenti
    i += 1 # Ia menghitung satu per satu, contoh: Menghitung hingga 10 dengan kelipatan 2, maka akan menjadi i += 2 dan menghitung 2, 4, 6, 8, 10
print("OK")
