# Python 3.10.9
#
# Michael LaRocca  
#
# The Tech Academy - Python course, creating our first game together.
# Demonstrating how to pass variables from function to function while 
# producing a functional game. 
#
# Remember, function_name(variable) _means that we pass in the variable.
# return variable _means that we are returning the variable back to the 
# calling function

def start():
    print(get_number())


def get_number():
    number = 12
    return number

if __name__ == "__main__":
    start()   

###

def start():
    print(get_name())


def get_name():
    name = input("What is your name? ")
    return name

if __name__ == "__main__":
    start()   

######

def start():
    print("Hello {}!".format(get_name()))


def get_name():
    name = input("What is your name? ")
    return name

if __name__ == "__main__":
    start()   

#####
def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "female"
    get_info(f_name,l_name,age,gender)
    

def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I'm a {} yearold {} terminator.".format(f_name,l_name,age,gender))


###### This always rides at the bottom 

if __name__ == "__main__":
    start()    