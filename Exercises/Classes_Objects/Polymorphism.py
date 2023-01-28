# Python 3.10.9
#
# Michael LaRocca
# 
# Steps 245 Polymorphism

# Parent Class User

class User:
    name = 'Mark'
    email = "mark@gmail.com"
    password = '1234abcd'

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter yoour password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("Password or Email is incorrect, hit the road jack! Or try again: ")

# Child Class Employee
class Employee(User):
    base_pay = 48.10
    department = "IT"
    pin_number = "3980"

# This is the same method in the parent class"User".
# The difference is that, instead of using entry_password, 
# we're using entry_pin.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter yoour pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("Pin or Email is incorrect, hit the road jack! Or try again: ")
# The following code invokes the methods inside each class for User Employee.

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()