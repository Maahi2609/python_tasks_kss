'''A transport company manages different vehicles. Create a base class Vehicle with
attributes like brand and speed. Create derived classes Car and Bike that inherit from
Vehicle and display their details'''

class Vehicle :
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
class Car(Vehicle) :
    def display(self):
        print("brand : ",self.brand)
        print("speed : ",self.speed) 
class Bike(Vehicle) :
    def display(self):
        print("brand : ",self.brand)
        print("speed : ",self.speed)

c = Car("Ferrari", 220)
c.display()

b = Bike("RoyalEnfield", 130)
b.display()
