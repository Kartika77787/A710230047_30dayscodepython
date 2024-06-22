# List dan Looping
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
for fruit in fruits:
    print(fruit)

# Dictionary
student = {"name": "Alice", "age": 25}
student["age"] = 26
print(student)

# Fungsi
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Pemrograman Berorientasi Objek (OOP)
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())

# Proyek Kecil (Manajemen Kontak)
contacts = []

def add_contact(name, phone):
    contacts.append({"name": name, "phone": phone})

def display_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")

add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
display_contacts()
