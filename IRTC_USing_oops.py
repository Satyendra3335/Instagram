users = {
    "satyendra": {
        "password": "2022",
        "dob": "01-01-2002",
        "email": "satyendra@example.com",
        "wallet":15000
       },
    "himanshu": {
        "password": "2022",
        "dob": "15-03-2001",
        "email": "riya@example.com",
        "wallet":3000
       },
    "avnish": {
        "password": "2022",
        "dob": "22-05-2002",
        "email": "avnish@example.com",
        "wallet":2000

       },
    "prem": {
        "password": "2022",
        "dob": "10-12-2000",
        "email": "prem@example.com",
        "wallet":1234
    },
    "ram": {
        "password": "2022",
        "dob": "30-09-2001",
        "email": "ram@example.com",
        "wallet":4022
    }
}

class IRTC:
    def __init__(self):
        self.user = input("enter your username: ").strip().lower()  
        if self.user not in users:
            print("\n Invalid username.\n")
            exit()  
        passw = input("enter your password: ").strip()
        if self.user in users and users[self.user]["password"] == passw:
            print(f"\n Login Successful! Welcome, {self.user}\n")
            self.calculate_fare()
        else:
            print("\n Invalid username or password.\n")
            exit() 

    def calculate_fare(self):
        stations = {
            "A": 0,
            "B": 5,
            "C": 10,
            "D": 15,
            "E": 20,
            "F": 25
        }
        print("Available station")
        for i in stations:
            print(stations)  
        start = input("enter starting station").upper().strip()
        end = input("enter the ending station ").upper().strip()
        if start not in stations or end not in stations: 
            print("Invalid Stations")
            return

        dist = abs(stations[start] - stations[end])
        rate_per_km = 50
        fare = dist * rate_per_km

        print(f"distance from {start} and {end}")
        print(f"fare amount {fare}")

        wallet_balance = users[self.user]["wallet"]  
        rest_money = wallet_balance - fare
        print(f"Remaining balance after fare: {rest_money if rest_money >= 0 else 'Insufficient Balance'}")


IRTC()
