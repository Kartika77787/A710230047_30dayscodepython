import math

def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

def hitung_keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

# Meminta input dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung luas dan keliling lingkaran
luas = hitung_luas_lingkaran(jari_jari)
keliling = hitung_keliling_lingkaran(jari_jari)

# Menampilkan hasil
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah {keliling:.2f}")
