class Car:
    def __init__(self, merek, model, tahun, warna):
        self.merek = merek  # brand
        self.model = model  # model
        self.tahun = tahun  # year
        self.warna = warna  # color
        self.mesin_menyala = False  # engine_running

    def start_engine(self):
        self.mesin_menyala = True
        return f"Mesin {self.warna} {self.merek} {self.model} sekarang menyala."  # The engine of the {color} {brand} {model} is now running.

    def stop_engine(self):
        self.mesin_menyala = False
        return f"Mesin {self.warna} {self.merek} {self.model} sekarang mati."  # The engine of the {color} {brand} {model} is now off.

    def get_status(self):
        status = "menyala" if self.mesin_menyala else "mati"  # running if engine_running else off
        return f"{self.warna} {self.merek} {self.model} ({self.tahun}) saat ini {status}."  # The {color} {brand} {model} ({year}) is currently {status}.

# Membuat satu instance dari kelas Car
mobil_saya = Car("Toyota", "Corolla", 2020, "merah")

# Menggunakan metode dari instance tersebut
print(mobil_saya.start_engine())  # Mesin merah Toyota Corolla sekarang menyala.
print(mobil_saya.get_status())    # Merah Toyota Corolla (2020) saat ini menyala.
print(mobil_saya.stop_engine())   # Mesin merah Toyota Corolla sekarang mati.
print(mobil_saya.get_status())    # Merah Toyota Corolla (2020) saat ini mati.
