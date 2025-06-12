class Atm:
    def __init__(self) :
        self.pin=""
        self.balance=0
        print(id(self))
        self.menu()

    def menu(self):
        while(True): 
            user_input=input("""
                        Hello,how u like to procced
                         1.enter 1 to crete pin
                         2.enter 2 to deposit
                         3.enter 4 to check balance
                         5.enter 5 to exit
                         """
                         )
            if user_input=='1':
                self.create_pin()
            elif user_input=='2':
                self.deposit()
            elif user_input=='3':
                self.withdraw()
            elif user_input=="4":
                self.check_balace()
            else:
                print("bye")

    def create_pin(self):
        self.pin=input("enter ur pin")
        print("pin set successfilly")

    def deposit(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=input("enter the amount")
            self.balance=self.balance+amount
            print("deposit successful")
        else:
            print("invalid pin")

    def withdraw(self):

        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter the amount"))
            if amount<self.pin:
                self.balance=self.balance-amount
                print("operational successful")
            else:
                print("insufficiet funds")
        else:
            print("invalid pin")

    def check_balace(self):
        temp=input("enter your pin")
        if temp==self.pin:
            print(self.balance)
        else:
            print("invalid pin")          
Atm()






        






