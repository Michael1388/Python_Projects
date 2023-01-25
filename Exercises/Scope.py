


name = "Python" #Global = outside the function or scope

def getName():
    print("I am coding with {}".format(name))

getName()

#Will result in Python being passed into the function as name bc it is Global 
# or "I am coding with Python"

name = "Python" #Global = outside the function or scope

def getName():
    name = "C#" #variable is now local and will override the global variable 
    #in this instance. After this function it will return to being global or 
    # as is seeen here is global in the example above bu local here/
    print("I am coding with {}".format(name))

getName()