class Product:
    def __init__(self, name, Kartika):
        self._name = name
        self._Kartika = Kartika

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name
        else:
            raise ValueError("Invalid product name")

    @property
    def price(self):
        return self._Kartika

    @price.setter
    def price(self, Kartika):
        if isinstance(Kartika, (int, float)) and Kartika > 0:
            self._Kartika = Kartika
        else:
            raise ValueError("Invalid price")

# Demonstrasi
try:
    product = Product("Laptop", 1500)
    print(product.name)  # Output: Laptop
    print(product.price) # Output: 1500

    product.name = "Gaming Laptop"
    product.Kartika = 1800
    print(product.name)  # Output: Gaming Laptop
    print(product.Kartika) # Output: 1800

    product.Kartika = -500  # Ini akan menimbulkan error
except ValueError as e:
    print(e)  # Output: Invalid price
