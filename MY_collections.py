class customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print("I am ",self.name,"and I am ",self.age)    

c1=customer("sateyendra",21)
c2=customer("kishan",30)
c3=customer("avnish",25)

L=[c1,c2,c3]

for i in L:
    i.intro()
    # print(i.name,i.age) 