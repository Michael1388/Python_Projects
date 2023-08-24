# Definite loops, "For" instead of "WHile", they are finite and more predictable.
# SImple Definite Loop
for i in [5, 4, 3, 2, 1] :  
    print(i)
print('Blastoff!')

# Definite Loop with Strings

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :                 # Python does not know the fdifference between friend and friends as in plural values, 
                                        # it is a variable that is just that, except here "friend" is "iteration variable" of the "FOR" statement - friend could be i or z of whatever you name it 
    print('Happy New Year:', friend)
print('Done!')

# Definite loops (for loops) have explicit iteration variables that change each time through a loop. 
# These iteration variables move through the sequence or set.

# all this logic is constructed by using the "for" statement.
# the IN keyword - it basically says for each of these values [5,4,3,2,1] or [Joseph, Glenn, Sally] have i or firend take on the successive value and run that loop one time

#Looking at IN
# THe iteration variable "iterates" through the sequence (ordered set)
# THe Block (body) of code is executed once for each value in the sequence
# THe iteration variable moves through all of the values IN the sequence

#Definite loops are for lists or lines in a file or charachters in a string and they iterate through members of a set.