class Customer:
  def __init__(self,name,gender):
    self.name=name
    self.gender=gender
def greet(customer):
    if customer.gender=="Male":
     print("hello",customer.name,"sir")
    else:
      print("hello",customer.name,"mam") 
cust=Customer("satyendra","Male")
greet(cust) 