'''A graphics application needs to calculate the area of different shapes. Create classes
Circle, Rectangle, and Triangle, each having an area() method. Demonstrate
polymorphism by calling the same method for different objects.'''


class Circle :
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius   

class Rectangle :
        def __init__(self, length, width):
             self.length = length
             self.width = width
        def area(self):
             return self.length * self.width

class Triangle :
    def __init__(self, base, height):
         self.base = base
         self.height = height
    def area(self):
          return 0.5 * self.base * self.height
c = Circle(67)
r = Rectangle(34, 9)
t = Triangle(8, 7)
shapes = [c, r, t]
for shape in shapes:
    print("Area =", shape.area())     