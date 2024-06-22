class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.__nama = nama  # atribut private
        self.__nim = nim    # atribut private
        self.__jurusan = jurusan  # atribut private

    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Setter untuk nama
    def set_nama(self, nama):
        self.__nama = nama

    # Getter untuk nim
    def get_nim(self):
        return self.__nim

    # Setter untuk nim
    def set_nim(self, nim):
        self.__nim = nim

    # Getter untuk jurusan
    def get_jurusan(self):
        return self.__jurusan

    # Setter untuk jurusan
    def set_jurusan(self, jurusan):
        self.__jurusan = jurusan

# Membuat objek dari class Mahasiswa
mhs = Mahasiswa("Kartika", "A710230047", "Pendidikan Teknik Informatika")

# Mengakses atribut melalui metode getter
print(f"Nama: {mhs.get_nama()}")
print(f"NIM: {mhs.get_nim()}")
print(f"Jurusan: {mhs.get_jurusan()}")
