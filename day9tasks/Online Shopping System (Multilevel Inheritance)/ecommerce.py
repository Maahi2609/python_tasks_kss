'''An e-commerce company organizes products using multiple levels. Create classes
Product → ElectronicProduct → MobilePhone using multilevel inheritance and
display product details.'''

class Product :
    def __init__(self, name):
        self.name = name

class ElectronicProduct(Product) :
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

class MobilePhone(ElectronicProduct) :
    def __init__(self, name, brand, price):
        super().__init__(name, brand)
        self.price = price

    def display(self):
        print("name : ",self.name)
        print("brand : ",self.brand)
        print("price : ",self.price)

mobile = MobilePhone("IOS", "Iphone", 89000)
mobile.display()    