def main():
    try:
        # Meminta input dari pengguna
        number = float(input("Masukkan sebuah bilangan: "))

        # Mencoba untuk melakukan pembagian
        result = 10 / number

        # Menampilkan hasil pembagian
        print(f"Hasil dari 10 dibagi dengan {number} adalah {result}")

    except ZeroDivisionError:
        # Menangani pembagian dengan nol
        print("Kesalahan: Tidak dapat membagi dengan nol!")

    except ValueError:
        # Menangani input yang tidak valid
        print("Kesalahan: Masukkan sebuah bilangan yang valid!")

    except Exception as e:
        # Menangani kesalahan lainnya
        print(f"Kesalahan yang tidak terduga terjadi: {e}")

if __name__ == "__main__":
    main()
