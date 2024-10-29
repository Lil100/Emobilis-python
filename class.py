class Fruits:
    def __init__(self, price, shape, name):
        self.price = price
        self.shape = shape
        self.name = name
    def display(self):
        print(f"favourite fruit is {self.name} its {self.shape} in shape and price is {self.price}")


myFruits=Fruits("KES 250","oval", "Bananas")
myFruits.display()