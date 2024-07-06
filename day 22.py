def hitung_balok():
    # Meminta pengguna memasukkan panjang, lebar, dan tinggi balok
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))

    # Menghitung volume balok
    volume = panjang * lebar * tinggi

    # Menghitung luas permukaan balok
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

    # Menampilkan hasil
    print(f"Volume balok: {volume:.2f}")
    print(f"Luas permukaan balok: {luas_permukaan:.2f}")

# Memanggil fungsi hitung_balok
hitung_balok()
