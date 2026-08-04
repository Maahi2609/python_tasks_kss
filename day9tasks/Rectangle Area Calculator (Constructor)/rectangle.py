'''A geometry application needs to calculate the area of rectangles. Create a Rectangle
class that uses a constructor to initialize length and width. Add a method to calculate
and display the area.'''

class Rectangle :
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def display_area(self):
        area = self.length * self.width
        print("length : ",self.length)
        print("width : ",self.width)
        print("area of rectangle : ", area)
rect = Rectangle(23, 45)
rect.display_area()        
        