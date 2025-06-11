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

def login():
    user = input("Enter your username: ").strip().lower()
    passw = input("Enter your password: ").strip()

    if user in users and users[user]["password"] == passw:
        print(f"\n Login Successful! Welcome, {user}\n")
        show_menu(user)
    else:
        print("\n Invalid username or password.\n")

def show_menu(user):
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
            show_profile(user)
        elif choice == "post":
            show_posts(user)
        elif choice == "likes":
            show_likes(user)
        elif choice == "comments":
            show_comments(user)
        elif choice == "analytics":
            show_analytics(user)
        elif choice == "update":
            update_profile_or_post(user)
        elif choice == "exit":
            print(" Logged out. Goodbye!")
            break
        else:
            print(" Invalid option. Try again.")

def show_profile(user):
    profile = users[user]
    print("\n Profile Information:")
    print(f"Username : {user}")
    print(f"DOB      : {profile['dob']}")
    print(f"Email    : {profile['email']}")
    print(f"Location : {profile['location']}")
    print(f"Phone    : {profile['phone']}")

def show_posts(user):
    posts = users[user]['posts']
    if posts:
        print("\n Posts:")
        for i in range(len(posts)):
            print(f"  {i+1}. {posts[i]}")
    else:
        print("\nNo posts yet.")

def show_likes(user):
    print(f"\n  Total Likes: {users[user]['likes']}")

def show_comments(user):
    comments = users[user]['comments']
    if comments:
        print("\n Comments:")
        for i in range(len(comments)):
            print(f"  {i+1}. {comments[i]}")
    else:
        print("\nNo comments yet.")

def show_analytics(user):
    profile = users[user]
    print("\n Analytics Summary")
    print(f"Posts    : {len(profile['posts'])}")
    print(f"Likes    : {profile['likes']}")
    print(f"Comments : {len(profile['comments'])}")

def update_profile_or_post(user):
    print("\n update profile or post")
    print("1. profile")
    print("2. post")
    choice = input("Type your choice: ").strip().lower()
#     updated_data =[{
#     "password": "new_password",
#     "dob": "new_dob",
#     "email": "new_mail",
#     "location": "new_location",
#     "phone": "new_no",
#     "posts": ["new_post"],
#     "likes": "new_likes",
#     "comments": ["new_comment"]
# }]
    
    
#     users[user].update(updated_data)
#     print(updated_data)
    


    

    if choice == "profile":

        new_data={
        "new_dob":input("enter new doib ").strip(),
        "new_email":input("new email ").strip(),
        "new_phone":input("new phone no ").strip()
        }

        old_data={
        "dob":users[user]['dob'],
        "email":users[user]['email'],
        "phone":users[user]['phone']
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
       "likes":users[user]['likes'],
       "comment":users[user]['comments'],
        "location":users[user]['location'] ,
        
        }
        print("updated post")
        for key in new_data:
            if old_data.get(key)!=new_data.get(key):
                print(new_data[key])



login()

