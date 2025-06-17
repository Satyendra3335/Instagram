class Phone:
    def __init__(self, price,brand,camera):
        print("inside phone constructor" )
        self.__price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a phone")
class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        super().buy()
s=SmartPhone(2000,"apple",13)
s.buy()    
