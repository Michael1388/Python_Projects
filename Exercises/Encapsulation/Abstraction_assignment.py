# python 3.10.9
# Python course, step 281
#
# Assignment Submission: 
# Create a class that utilizes the concept of abstraction.
#  
# Your class should contain at least one abstract method and one regular method.  
# Create a child class that defines the implementation of its parents abstract method.
# Create an object utilizing both the parent and child methods.
# Comment your code
# 
# 

# import the "abstractmethod" from the 'Abstract Base Class' module.  
from abc import ABC, abstractmethod

# regular method - 
class card(ABC):  # Parent Class 'card'
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
    
#abstract method -  this function is telling us to pass in an argument, but we will not  
# define how or what kind of data it will be, it will be 'abstracted'.

    @abstractmethod 
    def payment(self, amount):
        pass

# Child Class of 'card' Class

class CreditCardPayment(card): 
# here we've defined how to implement the payment function from its parent paySlip.
    def payment(self,amount): 
        print('Your purchase amount of {} has been charged to your payment method. '.format(amount))

obj = CreditCardPayment()
obj.paySlip("$50") 
obj.payment("$50")
