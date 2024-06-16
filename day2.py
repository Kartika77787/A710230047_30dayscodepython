class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Membuat instance dari class Person
person1 = Person("Kartika", 18)

person1.greet()  # Output: Hello, my name is Kartika and I am 18 years old.

