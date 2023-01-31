# Python 3.10.9
# 
# Michael La Rocca
# 
# Python Course:
# Python range( ) function
# Step 306, challenge 307
# 
# 
# Exercise
#my_list = ['one', 'two', 'three', 'four', 'five']
#my_list_len = len(my_list)
#for i in range(0, my_list_len):
#    print(my_list[i])

# Challenge 
# 1. use the Python range( ) function with one parameter to display the following:
# 0 1 2 3
#
# 2. Use the Python range( ) function with 3 parameters to display the following:
# 3 2 1 0
#
# 3. Use the Python range( ) function with 3 parameters to display the following:
# 8 6 4 2

# 1
x = range(4)
for n in x:
  print(n)

# 2
x = range(3,-1,-1)
for n in x:
  print(n)

# 3
x = range(8,1,-2)
for n in x:
  print(n)