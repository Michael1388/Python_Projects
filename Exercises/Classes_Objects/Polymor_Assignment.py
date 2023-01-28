# Python 3.10.9
#
# Michael LaRocca
# 
# Steps 246 Polymorphism Submission


# Create Parent Class User
class User:
    name = 'Name not provided' 
    email = 'Not Provided'
    password = 'abCD1234'
    #create a method
    def getLoginInfo(self): 
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter yoour password: ")
        #use if statement to determine if user has entered the correct info and print result
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("Password or Email is incorrect!")

# Child Class 1
class Employee(User):
    department = "IT"
    access_code = "0712" # polymorphism of password
    
# Child Class 2
class Student(User):
    course = "Software Development"
    access_code = "1895" # polymorphism of password

# Polymorphism used here is instead of using entry_password like the parent class, 
# we're using access_code with the child classes.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        access_code = input("Enter yoour access id: ")
        if (entry_email == self.email and access_code == self.access_code):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("Pin or Email is incorrect, hit the road jack! Or try again: ")
# The following code invokes the methods inside each class for Employee and Student.

if __name__ == "__main__":
    john = Employee()
    print(john.getLoginInfo())

    michael = Student()
    print(michael.getLoginInfo())