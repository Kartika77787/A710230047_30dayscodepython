def hitung_harga_makanan():
    daftar_makanan = []
    total_harga = 0
    
    while True:
        nama = input("Masukkan nama makanan (atau 'selesai' untuk berhenti): ")
        if nama.lower() == 'selesai':
            break
        
        try:
            harga_per_satuan = float(input(f"Masukkan harga per satuan untuk {nama}: "))
            jumlah = int(input(f"Masukkan jumlah {nama} yang dibeli: "))
        except ValueError:
            print("Input tidak valid, silakan masukkan angka yang benar.")
            continue

        total_item = harga_per_satuan * jumlah
        daftar_makanan.append((nama, harga_per_satuan, jumlah, total_item))
        total_harga += total_item

    print("\nDaftar Makanan dan Total Harganya:")
    for makanan in daftar_makanan:
        print(f"{makanan[0]}: {makanan[2]} x {makanan[1]} = {makanan[3]}")

    print(f"\nTotal Harga Keseluruhan: {total_harga}")

hitung_harga_makanan()