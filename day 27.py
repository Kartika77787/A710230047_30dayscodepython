def hitung_kata(teks):
    # Memisahkan teks menjadi kata-kata berdasarkan spasi
    kata_list = teks.split()
    # Menghitung jumlah kata
    jumlah_kata = len(kata_list)
    return jumlah_kata

def main():
    print("Program Penghitung Jumlah Kata")
    teks = input("Masukkan teks: ")
    jumlah_kata = hitung_kata(teks)
    print(f"Jumlah kata dalam teks: {jumlah_kata}")

if __name__ == "__main__":
    main()
