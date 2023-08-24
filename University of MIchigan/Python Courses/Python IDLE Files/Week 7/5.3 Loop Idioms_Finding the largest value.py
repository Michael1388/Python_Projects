# Finding the largest value
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