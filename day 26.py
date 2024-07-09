import random

def tampilkan_menu():
    print("\nMenu:")
    print("1. Tambah nama ke daftar")
    print("2. Hapus nama dari daftar")
    print("3. Tampilkan semua nama")
    print("4. Pilih nama secara acak")
    print("5. Keluar")

def tambah_nama(daftar_nama):
    nama = input("Masukkan nama yang ingin ditambahkan: ")
    daftar_nama.append(nama)
    print(f"Nama '{nama}' telah ditambahkan ke daftar.")

def hapus_nama(daftar_nama):
    nama = input("Masukkan nama yang ingin dihapus: ")
    if nama in daftar_nama:
        daftar_nama.remove(nama)
        print(f"Nama '{nama}' telah dihapus dari daftar.")
    else:
        print(f"Nama '{nama}' tidak ditemukan dalam daftar.")

def tampilkan_nama(daftar_nama):
    if not daftar_nama:
        print("Tidak ada nama dalam daftar.")
    else:
        print("Daftar Nama:")
        for nama in daftar_nama:
            print(f"- {nama}")

def pilih_nama_acak(daftar_nama):
    if not daftar_nama:
        print("Tidak ada nama dalam daftar untuk dipilih.")
    else:
        nama_acak = random.choice(daftar_nama)
        print(f"Nama yang dipilih secara acak adalah: {nama_acak}")

def main():
    daftar_nama = []
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
        if pilihan == '1':
            tambah_nama(daftar_nama)
        elif pilihan == '2':
            hapus_nama(daftar_nama)
        elif pilihan == '3':
            tampilkan_nama(daftar_nama)
        elif pilihan == '4':
            pilih_nama_acak(daftar_nama)
        elif pilihan == '5':
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
