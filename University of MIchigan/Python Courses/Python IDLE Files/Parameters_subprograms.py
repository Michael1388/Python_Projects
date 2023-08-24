
# Example of parameters but does not look like Python
#Here, the name of the subprogram is “AddTwo.”
# The parameters of the subprogram are two numbers called x and y.
#The subprogram will return the sum of those two numbers.

#To clarify: when a subprogram is defined, any data items it will need
#are called parameters.
#When the subprogram is actually used, the actual data passed to it
#at that time is called arguments.


subprogram AddTwo(x, y)

{ return x + y }



classSizePE1 = 25 # 25 is the assigned argument as is 43 on the next line.

classSizePE2 = 43

totalSize = AddTwo(classSizePE1, classSizePE2)

print(“The total number of students in the PE classes is: ” + totalSize)



    
    
    
    
    
