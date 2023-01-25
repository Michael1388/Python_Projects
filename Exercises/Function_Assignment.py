# PYTHON VARIABLES

# In Python, variables can be used to store all kinds of information. 
# Typically that information is small and simple, but variables are 
# not limited to simple strings or numbers. They can also be used to 
# store entire dictionaries of information, an extensive list of items, 
# or even functions.

#In the example below, we have defined a function with instructions
#  to get the sum of two numbers being added together and then print 
# that number. We call on this function using its name followed by an 
# open and closed parenthesis, then passing in the required arguments.

def getSum(num1,num2):
    answer = num1 + num2
    print("The answer is {}.".format(answer))
getSum(2,4)

#We can store the entire block of code from the getSum() function and 
# store all of those instructions inside of the new variable "myAdd" 
# for use later on within the program.

myAdd = getSum

#Later we can call on that function's block of code by simply referring 
# to the new variable with open and closed parenthesis, then passing in 
# the required arguments. Voilà! All of the original steps from the 
# getSum() function have been recreated.

myAdd(3, 6)

