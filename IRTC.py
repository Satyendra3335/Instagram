users = {
    "satyendra": {
        "password": "2022",
        "dob": "01-01-2002",
        "email": "satyendra@example.com",
        "wallet": 15000
    },
    "himanshu": {
        "password": "2022",
        "dob": "15-03-2001",
        "email": "riya@example.com",
        "wallet": 3000
    },
    "avnish": {
        "password": "2022",
        "dob": "22-05-2002",
        "email": "avnish@example.com",
        "wallet": 2000
    },
    "prem": {
        "password": "2022",
        "dob": "10-12-2000",
        "email": "prem@example.com",
        "wallet": 1234
    },
    "ram": {
        "password": "2022",
        "dob": "30-09-2001",
        "email": "ram@example.com",
        "wallet": 4022
    }
}

class IRTC:
    def __init__(self):
        self.stations = {
            "A": 0,
            "B": 5,
            "C": 10,
            "D": 15,
            "E": 20,
            "F": 25
        }
        self.user = input("Enter your username: ").strip().lower()
        if self.user not in users:
            print("\nInvalid username.\n")
            exit()
        passw = input("Enter your password: ").strip()
        if users[self.user]["password"] == passw:
            print(f"\nLogin Successful! Welcome, {self.user}")
            print(f"Current wallet balance: ₹{users[self.user]['wallet']}\n")
            self.menu() 
        else:
            print("\nInvalid username or password.\n")
            exit()

    def menu(self):
        while True:
            print("\nIRTC MENU")
            print("1. Select Starting Station")
            print("2. Select Ending Station")
            print("3. Show All Available Stations")
            print("4. Calculate Fare")
            print("5. Exit")
            print("6. Add Amount to Wallet")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.select_station("start")
            elif choice == "2":
                self.select_station("end")
            elif choice == "3":
                self.show_all_stations()
            elif choice == "4":
                self.calculate_fare()
            elif choice == "5":
                print("Thank you for using IRTC!")
                break
            elif choice == "6":
                self.add_to_wallet()
            else:
                print("Invalid choice")

    def select_station(self, position):
        print("\nAvailable Stations:")
        for station in self.stations:
            print(station, end="  ")
        print()

        station_input = input("Enter station: ").upper().strip()
        if station_input in self.stations:
            setattr(self, position, station_input)
            print(f"Station set to {station_input}")
        else:
            print("Invalid station. Please try again.")

    def show_all_stations(self):
        print("\nAll Available Stations:")
        for station, distance in self.stations.items():
            print(f"{station} ({distance} km)", end="  ")
        print()

    def calculate_fare(self):
        if self.start is None or self.end is None:
            print("Please select both starting and ending stations first.")
            return

        dist = abs(self.stations[self.start] - self.stations[self.end])
        rate_per_km = 50
        fare = dist * rate_per_km

        print(f"\nDistance from {self.start} to {self.end}: {dist} km")
        print(f"Fare amount: ₹{fare}")

        wallet_balance = users[self.user]["wallet"]
        rest_money = wallet_balance - fare

        if rest_money >= 0:
            users[self.user]["wallet"] = rest_money
            print(f"Remaining wallet balance: ₹{rest_money}")
        else:
            print("Insufficient Balance")

    def add_to_wallet(self):
        amt_input = input("Enter amount to add:").strip()
        if amt_input.isdigit():
            amt = int(amt_input)
            if amt > 0:
                users[self.user]["wallet"] += amt
                print(f"{amt} added successfully!")
                print(f"Updated wallet balance: {users[self.user]['wallet']}")
            else:
                print("Amount must be greater than 0.")
        else:
            print("Invalid input. Please enter a positive number.")

IRTC()
