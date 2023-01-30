# python 3.10.9
# Python course, step 279
#
# Assignment Submission: 
# Create a class that uses encapsulation, private and protected examples.
#  
# This class should make use of a private attribute or function.
# This class should make use of a protected attribute or function. 
# Create An object that makes use of protected and private.
# Comment your code
# 
# 


# Here is a protected variable denoted by a single underscore prefix

class Student_Protected:
    def __init__(self):
        self._protectedVar = 'Name' # single underscore

obj = Student_Protected() 
obj._protectedVar = 'Michael'
print(obj._protectedVar)

# The output is Michael

# Here is a Private variable denoted with a double underscore prefix

class Private_Student:
    def __init__(self):
        self.__privateName = "Name is" # double underscore 

    def getPrivate(self):
        print(self.__privateName)

    def setPrivate(self, private):
        self.__privateName = private
    
obj = Private_Student()
obj.getPrivate()
obj.setPrivate("Michael") 
obj.getPrivate()


 # The output is Name, Michael