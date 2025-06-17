class user:
    def login(self):
        print("login")
    def register(self):
        print("register")
class student(user):
    def enroll(self):
        print("Enroll")
    def rewiew(self):
        print("Review")
stu1=student()

stu1.enroll()
stu1.login()
stu1.register()
stu1.rewiew()