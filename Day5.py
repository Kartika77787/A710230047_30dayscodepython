class Person:
    def __init__(self, name, age):
        self.__name = name  # Atribut privat
        self.__age = age    # Atribut privat

    # Getter untuk nama
    def get_name(self):
        return self.__name

    # Setter untuk nama
    def set_name(self, name):
        self.__name = name

    # Getter untuk umur
    def get_age(self):
        return self.__age

    # Setter untuk umur
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age")

    # Metode publik untuk menampilkan informasi
    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

# Contoh penggunaan:
person = Person("Kartika", 18)

# Mengakses atribut melalui metode getter
print(person.get_name())  # Output: Kartika
print(person.get_age())   # Output: 18

