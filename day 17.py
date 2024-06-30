import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)  # Menghasilkan angka acak antara 1 dan 100
    percobaan = 0

    print("Selamat datang di permainan Tebak Angka!")
    print("Saya telah memilih angka antara 1 dan 100.")
    print("Coba tebak angkanya!")

    while True:
        tebak = int(input("Masukkan tebakan Anda: "))
        percobaan += 1

        if tebak < angka_rahasia:
            print("Terlalu rendah! Coba lagi.")
        elif tebak > angka_rahasia:
            print("Terlalu tinggi! Coba lagi.")
        else:
            print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
            break

# Menjalankan permainan
tebak_angka()
