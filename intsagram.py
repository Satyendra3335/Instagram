users = {
    "satyendra": {
        "password": "2022",
        "dob": "01-01-2002",
        "email": "satyendra@example.com",
        "location": "Gonda",
        "phone": "9876543210",
        "posts": ["Working on an exciting project!", "Just joined Skill Eliters!"],
        "likes": 23,
        "comments": ["Nice post!", "Great job!", "Keep it up!"]
    },
    "riya": {
        "password": "2022",
        "dob": "15-03-2001",
        "email": "riya@example.com",
        "location": "Delhi",
        "phone": "9876543211",
        "posts": ["Loving the new UI design I made."],
        "likes": 15,
        "comments": ["Awesome!", "Very creative!"]
    },
    "avnish": {
        "password": "2022",
        "dob": "22-05-2002",
        "email": "avnish@example.com",
        "location": "Noida",
        "phone": "9876543212",
        "posts": ["Learning Python!", "Debugging is fun!"],
        "likes": 30,
        "comments": ["Cool!", "You're doing great!"]
    },
    "prem": {
        "password": "2022",
        "dob": "10-12-2000",
        "email": "prem@example.com",
        "location": "Ghaziabad",
        "phone": "9876543213",
        "posts": ["Started my internship today."],
        "likes": 10,
        "comments": ["Congrats!", "Good luck!"]
    },
    "ram": {
        "password": "2022",
        "dob": "30-09-2001",
        "email": "ram@example.com",
        "location": "Lucknow",
        "phone": "9876543214",
        "posts": [],
        "likes": 0,
        "comments": []
    }
}
class INSTAGRAM:
    def __init__(self):
        user = input("Enter your username: ").strip().lower()
        passw = input("Enter your password: ").strip()
        if user in users and users[user]["password"] == passw:
            print(f"\n Login Successful! Welcome, {user}\n")
            self.show_menu()
        else:
            print("\n Invalid username or password.\n")

    def show_menu(self):
        while True:
            print("\n Select an option:")
            print("1. profile")
            print("2. post")
            print("3. likes")
            print("4. comments")
            print("5. analytics")
            print("6. exit")
            print("7. update")
            choice = input("Type your choice: ").strip()
            if choice == "profile":
                self.show_profile
            elif choice == "post":
                self.show_posts
            elif choice == "likes":
                self.show_likes
            elif choice == "comments":
                self.show_comments
            elif choice == "analytics":
                self.show_analytics
            elif choice == "update":
                self.update_profile_or_post
            elif choice == "exit":
                print(" Logged out. Goodbye!")
                break
            else:
                print(" Invalid option. Try again.")

    def show_profile(self):
        profile = users[self]
        print("\n Profile Information:")  
        print(f"Username : {self}")
        print(f"DOB      : {profile['dob']}")
        print(f"Email    : {profile['email']}")
        print(f"Location : {profile['location']}")
        print(f"Phone    : {profile['phone']}")

    def show_posts(self):
        posts = users[self]['posts']
        if posts:
            print("\n Posts:")
        for i in range(len(posts)):
            print(f"  {i+1}. {posts[i]}")
        else:
            print("\nNo posts yet.")

    def show_likes(self):
        print(f"\n  Total Likes: {users[self]['likes']}")

    def show_comments(self):
        comments = users[self]['comments']
        if comments:
            print("\n Comments:")
        for i in range(len(comments)):
            print(f"  {i+1}. {comments[i]}")
        else:
            print("\nNo comments yet.")

    def show_analytics(self):
        profile = users[self]
        print("\n Analytics Summary")
        print(f"Posts    : {len(profile['posts'])}")
        print(f"Likes    : {profile['likes']}")
        print(f"Comments : {len(profile['comments'])}")

    def update_profile_or_post(self):
        print("\n update profile or post")
        print("1. profile")
        print("2. post")
        choice = input("Type your choice: ").strip().lower()
        if choice == "profile":
            new_data={
                "new_dob":input("enter new doib ").strip(),
                "new_email":input("new email ").strip(),
                "new_phone":input("new phone no ").strip()
                }

            old_data={
                "dob":users[self]['dob'],
                "email":users[self]['email'],
                "phone":users[self]['phone']
                }
            print("updated profile")
            for key in new_data:
                if old_data.get(key)!=new_data.get(key):
                    print(new_data[key])

    
    
        if choice=="post":
            new_data={
                "new_like":int(input("new likes")).strip(),
                "new_comment":input("new comment").strip(),
                "new_location" : input("new loc").strip()
                }
            old_data={
                "likes":users[self]['likes'],
                "comment":users[self]['comments'],
                "location":users[self]['location'] ,
                }
            print("updated post")
        for key in new_data:
            if old_data.get(key)!=new_data.get(key):
                print(new_data[key])



INSTAGRAM()

