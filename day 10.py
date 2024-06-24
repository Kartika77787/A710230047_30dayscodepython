# Kelas induk (superclass)
class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

# Kelas anak (subclass) Rectangle
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Kelas anak (subclass) Circle
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Penggunaan kelas-kelas
if __name__ == "__main__":
    # Membuat objek dari kelas Rectangle
    rect = Rectangle("blue", 5, 10)
    print(f"Rectangle color: {rect.get_color()}")
    print(f"Rectangle area: {rect.area()}")

    # Membuat objek dari kelas Circle
    circle = Circle("red", 7)
    print(f"Circle color: {circle.get_color()}")
    print(f"Circle area: {circle.area()}")
