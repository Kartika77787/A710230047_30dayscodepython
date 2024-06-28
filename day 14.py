import math

# Fungsi untuk menghitung keliling dan luas segitiga sama sisi
def keliling_segitiga_sama_sisi(sisi):
    return 3 * sisi

def luas_segitiga_sama_sisi(sisi):
    return (math.sqrt(3) / 4) * (sisi ** 2)

# Fungsi untuk menghitung keliling dan luas trapesium
def keliling_trapesium(sisi_a, sisi_b, sisi_c, sisi_d):
    return sisi_a + sisi_b + sisi_c + sisi_d

def luas_trapesium(sisi_a, sisi_b, tinggi):
    return ((sisi_a + sisi_b) / 2) * tinggi

# Fungsi untuk menghitung keliling dan luas elips
def keliling_elips(sumbu_pendek, sumbu_panjang):
    return math.pi * (3*(sumbu_pendek + sumbu_panjang) - math.sqrt((3*sumbu_pendek + sumbu_panjang) * (sumbu_pendek + 3*sumbu_panjang)))

def luas_elips(sumbu_pendek, sumbu_panjang):
    return math.pi * sumbu_pendek * sumbu_panjang

# Contoh penggunaan:
sisi_segitiga = 6
sisi_a_trapesium = 8
sisi_b_trapesium = 6
sisi_c_trapesium = 5
sisi_d_trapesium = 7
tinggi_trapesium = 4
sumbu_pendek_elips = 5
sumbu_panjang_elips = 10

print(f"Keliling segitiga sama sisi dengan sisi {sisi_segitiga} adalah {keliling_segitiga_sama_sisi(sisi_segitiga)}")
print(f"Luas segitiga sama sisi dengan sisi {sisi_segitiga} adalah {luas_segitiga_sama_sisi(sisi_segitiga)}")

print(f"Keliling trapesium dengan sisi {sisi_a_trapesium}, {sisi_b_trapesium}, {sisi_c_trapesium}, dan {sisi_d_trapesium} adalah {keliling_trapesium(sisi_a_trapesium, sisi_b_trapesium, sisi_c_trapesium, sisi_d_trapesium)}")
print(f"Luas trapesium dengan sisi {sisi_a_trapesium}, {sisi_b_trapesium}, dan tinggi {tinggi_trapesium} adalah {luas_trapesium(sisi_a_trapesium, sisi_b_trapesium, tinggi_trapesium)}")

print(f"Keliling elips dengan sumbu pendek {sumbu_pendek_elips} dan sumbu panjang {sumbu_panjang_elips} adalah {keliling_elips(sumbu_pendek_elips, sumbu_panjang_elips)}")
print(f"Luas elips dengan sumbu pendek {sumbu_pendek_elips} dan sumbu panjang {sumbu_panjang_elips} adalah {luas_elips(sumbu_pendek_elips, sumbu_panjang_elips)}")
