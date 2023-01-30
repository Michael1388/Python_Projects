# Python 3.10.9
#
# Michael LaRocca
# 
# Steps 249 Args 250 Kwargs
# 
# Short for Arguments *args the * represents any number of 
# arguments in tuple form. allows you to add to your current parameters 
# even if you didn't have any defined. 


def myFun(*args):
    for arg in args:
        print(arg)

myFun('This is an example of args', 'string', 'and then an integer', 5)


# Kwargs(short for "keyword arguments") 
# is also a special syntax, just like *args. 
# 
# written as **kwargs where the asterisks ** represent a key value pair
# It acts as a dictionary, mapping out the value to its corresponding 
# variable key.

# You’ll see the use of **args used by some programmers, which is another way
#  of writing kwargs

def myFuns(**kwargs):
    print("kwargs", kwargs)

myFuns(first = "1", second = "2", third = "3")

