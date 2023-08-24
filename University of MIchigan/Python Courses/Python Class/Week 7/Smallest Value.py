# Finding the Smallest value
# Making Smart Loops - THe trick is knowing something about the whole loop when you are stuck writing code that only sees one entry at a time.

print('Before')
for thing in [9, 41, 12, 3, 74, 15] :
    print(thing)
print('After')

# What is the largest number?
# Finding the largest Value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41,12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After',largest_so_far)


# BUT FOR SMALLEST VALUE we have to change a few things because -1 doesn't work right....
# NONE TYPE a new keyword 
# Smallest will only be NONE on the first time through the loop, after that it changes to the value

smallest = None                      # None is a FLag value
print('Before')                       
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :           # IF gets it started and setup. IS is more powerful that == IS means is it exactly the same as. FIrst time through the loop smallest is NONE
        smallest = value            # Smallest now becomes the "Value" which the first was 9 bc on the first run and now smallest equals value 9 
    elif value < smallest :         # we changed > to < to find smallest instead of largest and now we added a little more intelligence with ELIF
        smallest = value
    print(smallest, value)

print('After', smallest)

# After thoughts and notes
# Python has an 'is' operator that can be used in logical expressions
# Implies "is the same as"
# Similar to, but stronger than '==' 
# 'is not' is also a logical operator

