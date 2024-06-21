def main():
    while True:
        print("\nPilih Operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator.")
            break

        if pilihan in ['1', '2', '3', '4']:
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Harap masukkan angka yang valid.")
                continue

            if pilihan == '1':
                hasil = angka1 + angka2
            elif pilihan == '2':
                hasil = angka1 - angka2
            elif pilihan == '3':
                hasil = angka1 * angka2
            elif pilihan == '4':
                if angka2 != 0:
                    hasil = angka1 / angka2
                else:
                    hasil = "Tidak dapat membagi dengan nol"
            
            print(f"Hasil: {hasil}")
        else:
            print("Pilihan tidak valid. Harap pilih antara 1 hingga 5.")

if __name__ == "__main__":
    main()
