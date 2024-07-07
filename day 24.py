import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    percobaan = 0

    print("Selamat datang di permainan tebak angka!")
    print("Saya telah memilih sebuah angka antara 1 dan 100. Cobalah tebak!")

    while tebakan != angka_rahasia:
        tebakan = int(input("Masukkan tebakanmu: "))
        percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu rendah! Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Terlalu tinggi! Coba lagi.")
        else:
            print(f"Selamat! Kamu berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")

if __name__ == "__main__":
    tebak_angka()
