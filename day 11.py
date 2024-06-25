class Tabungan:
    def __init__(self, pemilik, saldo_awal):
        self.__pemilik = pemilik       # Attribute private
        self.__saldo = saldo_awal      # Attribute private

    # Getter untuk pemilik
    def get_pemilik(self):
        return self.__pemilik

    # Setter untuk pemilik
    def set_pemilik(self, pemilik):
        self.__pemilik = pemilik

    # Getter untuk saldo
    def get_saldo(self):
        return self.__saldo

    # Metode untuk menabung
    def menabung(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil menabung {jumlah}. Saldo baru: {self.__saldo}")
        else:
            print("Jumlah tabungan harus lebih dari 0.")

    # Metode untuk menarik uang
    def menarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Berhasil menarik {jumlah}. Saldo baru: {self.__saldo}")
        else:
            print("Penarikan gagal. Jumlah tidak valid atau saldo tidak mencukupi.")

# Membuat objek Tabungan
tabungan1 = Tabungan("Kartika", 1000)

# Mengakses dan mengubah data menggunakan metode getter dan setter
print(f"Pemilik Tabungan: {tabungan1.get_pemilik()}")
print(f"Saldo Awal: {tabungan1.get_saldo()}")

# Mengubah nama pemilik tabungan
tabungan1.set_pemilik("Tika")
print(f"Pemilik Tabungan baru: {tabungan1.get_pemilik()}")

# Menabung dan menarik uang
tabungan1.menabung(500)
tabungan1.menarik(200)
tabungan1.menarik(2000)  # Gagal karena saldo tidak mencukupi
