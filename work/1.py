class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(6)
print("\nCircle:")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())