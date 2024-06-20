# Kelas dasar atau superclass
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Kelas turunan atau subclass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Kelas turunan lainnya
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Penggunaan kelas-kelas tersebut
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!

cat = Cat("Whiskers")
print(cat.speak())  # Output: Whiskers says Meow!
