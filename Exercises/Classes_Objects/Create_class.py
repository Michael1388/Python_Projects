
# Python 3.10.9
#
# Michael LaRocca 
#
#steps 235, 236
# Create a Class of "User" which will act as our blueprint for future 
# objects created from it.

class User:
    
    #Define the attributes of the class
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0

    # Define the methods of the class
    def login(self): # the self keyword represents an instance of the class. 
        # and so we can call the elements using self.element
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page")
# Outside of the class you would create an instance of the User class 
#as 'new_user = User()'
#Call the login method using the new object as 'new_user.login()'

#code Josh helped me with to understand above
michaelAccount = User()

def updateUsername(myAccount: User, username: str):
    myAccount.name = username

updateUsername(michaelAccount, "Michael")


# Create Class with Arguments - at the time the object is created this is called
# this is called initialization and can easily be set up. It just requires 
# utilizing a dunder method (__init__ ) to attach the arguments for creating 
# the object to the attributes of that object.  

def __init__(self, name, email, password, account):
    self.name = name
    self.email = email
    self.password = password
    self.account = account

new_user = User("John Doe", "jdoe@outlook.com", "p@ssw0rd", 1234)




# Class inheritance

