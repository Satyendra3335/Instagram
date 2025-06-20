users = {
    "satyendra": {"password": "2022", "wallet": 15000},
    "himanshu": {"password": "2022", "wallet": 3000},
    "avnish": {"password": "2022", "wallet": 2000},
    "prem": {"password": "2022", "wallet": 1234},
    "ram": {"password": "2022", "wallet": 4022}
}

class IRTC:
    def __init__(self):
        self.stations = {
            "A": 0, "B": 5, "C": 10, "D": 15, "E": 20, "F": 25
        }
        self.user = input("Username: ").strip().lower()
        if self.user not in users or input("Password: ").strip() != users[self.user]["password"]:
            print("Invalid credentials.")
            exit()
        self.menu()

    def menu(self):
        while True:
            print("\n1. Show Stations\n2. Book Ticket\n3. Check Wallet Balance\n4. Recharge Wallet\n5. Exit")
            choice = input("Choice: ").strip()
            if choice == "1":
                self.show_stations()
            elif choice == "2":
                self.book_ticket()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                self.recharge_wallet()
            elif choice == "5":
                break
            else:
                print("Invalid choice")

    def show_stations(self):
        for station, km in self.stations.items():
            print(f"{station} ({km} km)", end="  ")
        print()

    def book_ticket(self):
        self.show_stations()
        s = input("From: ").upper().strip()
        e = input("To: ").upper().strip()
        if s in self.stations and e in self.stations and s != e:
            self.start = s
            self.end = e
            fare = abs(self.stations[self.start] - self.stations[self.end]) * 50
            wallet = users[self.user]["wallet"]
            print(f"Fare from {self.start} to {self.end} is: {fare}")
            if wallet >= fare:
                users[self.user]["wallet"] -= fare
                print(f"Ticket booked. Remaining balance: {users[self.user]['wallet']}")
            else:
                print(f"Insufficient balance. Wallet: {wallet}, Fare: {fare}")
                if input("Add money? (yes/no): ").strip().lower() == "yes":
                    self.recharge_wallet()
                    if users[self.user]["wallet"] >= fare:
                        users[self.user]["wallet"] -= fare
                        print(f"Fare deducted. New balance: {users[self.user]['wallet']}")
                    else:
                        print("Still insufficient balance.")
        else:
            print("Invalid station(s)")

    def recharge_wallet(self):
        amount = input("Amount to add: ").strip()
        if amount.isdigit() and int(amount) > 0:
            users[self.user]["wallet"] += int(amount)
            print(f"New wallet balance: {users[self.user]['wallet']}")
        else:
            print("Invalid amount.")

    def check_balance(self):
        print(f"Wallet Remaining balance: {users[self.user]['wallet']}")

IRTC()
