def hitung_kecepatan(jarak, waktu):
    """
    Fungsi untuk menghitung kecepatan.
    
    :param jarak: Jarak yang ditempuh (dalam kilometer)
    :param waktu: Waktu yang diperlukan (dalam jam)
    :return: Kecepatan (dalam kilometer per jam)
    """
    if waktu <= 0:
        return "Waktu harus lebih besar dari nol"
    
    kecepatan = jarak / waktu
    return kecepatan

# Contoh penggunaan fungsi
jarak = 100  # kilometer
waktu = 2  # jam

kecepatan = hitung_kecepatan(jarak, waktu)
print(f"Kecepatan: {kecepatan} km/jam")
