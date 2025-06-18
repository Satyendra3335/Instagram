users = {
    "satyendra": {
        "password": "2022",
        "dob": "01-01-2002",
        "email": "satyendra@example.com"
       },
    "himanshu": {
        "password": "2022",
        "dob": "15-03-2001",
        "email": "riya@example.com"
       },
    "avnish": {
        "password": "2022",
        "dob": "22-05-2002",
        "email": "avnish@example.com"
       },
    "prem": {
        "password": "2022",
        "dob": "10-12-2000",
        "email": "prem@example.com"
    },
    "ram": {
        "password": "2022",
        "dob": "30-09-2001",
        "email": "ram@example.com"
    }
}
def login():
    user = input("enter your username: ").strip().lower()
    passw = input("enter your password: ").strip()

    if user in users and users[user]["password"] == passw:
        print(f"\n Login Successful! Welcome, {user}\n")
        calculate_fare()
    else:
        print("\n Invalid username or password.\n")
def calculate_fare():
    stations={
                "A":0,
                "B":5,
                "C":10,
                "D":15,
                "E":20,
                "F":25
                }
    print("Available station")
    for i in stations:
      print(stations )
    start=input("enter starting station").upper().strip()
    end=input("enter the ending station ").upper().strip()
    if start not in stations and end not in stations:
        print("Invalid Stations")
        return
    dist=abs(stations[start]-stations[end])
    rate_per_km=50
    fare=dist*rate_per_km
    print(f"distance from {start} and {end}")
    print(f"fare amount {fare}")
   
              
login()