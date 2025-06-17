class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        print("first")
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
        print("Inside smartphone constructor")
s= SmartPhone(2000,"samsung",12,"Android",2)
print(s.os)
print(s.brand)