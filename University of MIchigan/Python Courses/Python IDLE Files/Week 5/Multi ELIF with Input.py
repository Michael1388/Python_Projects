from typing import Literal


x = 0       #this is the variable filed which determines which of the three functions will print
            # I would think you could use the "input" filed here to create a user enter function 
            #which we wiill try here lol
x = input("Enter Size:")
x = int(x)
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('Large')
print('All done')
7