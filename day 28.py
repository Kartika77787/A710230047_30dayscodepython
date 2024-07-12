def hitung_vokal(teks):
    vokal = "aeiouAEIOU"
    jumlah_vokal = 0
    for char in teks:
        if char in vokal:
            jumlah_vokal += 1
    return jumlah_vokal

def main():
    print("Program Penghitung Jumlah Huruf Vokal")
    teks = input("Masukkan teks: ")
    jumlah_vokal = hitung_vokal(teks)
    print(f"Jumlah huruf vokal dalam teks: {jumlah_vokal}")

if __name__ == "__main__":
    main()
