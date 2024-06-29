from datetime import date

class Person:
    def __init__(self, name, birthdate):
        self.__name = name
        self.__birthdate = birthdate
    
    # Getter untuk mendapatkan nama
    @property
    def name(self):
        return self.__name
    
    # Setter untuk mengubah nama
    @name.setter
    def name(self, name):
        self.__name = name
    
    # Method untuk menghitung umur
    def calculate_age(self):
        today = date.today()
        age = today.year - self.__birthdate.year
        
        if today.month < self.__birthdate.month or (today.month == self.__birthdate.month and today.day < self.__birthdate.day):
            age -= 1
        
        return age
    
    # Method untuk mendapatkan informasi lengkap
    def get_info(self):
        return f'Name: {self.__name}, Age: {self.calculate_age()}'

# Contoh penggunaan
person = Person("Kartika", date(2005, 9, 15))
print(person.get_info())

# Mengubah nama
person.name = "Kartika"
print(person.get_info())
