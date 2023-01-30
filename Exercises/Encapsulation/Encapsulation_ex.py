# Python 3.10.9

"""Encapsulate means to enclose. Encapsulation is an important aspect to Object-Oriented programming. 
The purpose is to wrap your code in one single unit that restricts access from functions and variables
from being directly changed or modified by accident within a class.

Encapsulation is implemented by creating a protected (also called non-public) or private method or property.

Protected is prefixed with a single underscore. It doesn’t actually change the behavior of anything though. 
You could still modify your methods and properties within a class. It acts more as a warning to other developers
and basically states that “this is protected - don't use outside of this class” without the need for commenting 
or making it harder to modify your objects.

Here is an example of a protected variable: """

class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)

# The output is 34

# Private is denoted with a double underscore prefix. It’s harder to access but can still be done.

class Private:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
    
obj = Private()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()


"""
Above, Obj gets the data of the private variable, but then we also set the privateVar a new value. 
We then ask for that to be retrieved. It takes a bit more coding, but this ensures that private can not
 be changed unless it is on purpose. The output for this code is: 
 
"""

 # The output is 12 23