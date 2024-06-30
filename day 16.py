def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial(n - 1)

def main():
    print("Program untuk menghitung faktorial sebuah angka")
    angka = int(input("Masukkan sebuah angka: "))
    
    if angka < 0:
        print("Faktorial tidak terdefinisi untuk angka negatif.")
    else:
        hasil = hitung_faktorial(angka)
        print(f"Faktorial dari {angka} adalah: {hasil}")

if __name__ == "__main__":
    main()
