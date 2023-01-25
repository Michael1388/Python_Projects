
#### While Loop ####
# With the while loop we can execute a set of statements as 
# long as a condition is true.

i = 0
while i < 10:
    print("{} iteration through the WHILE loop.".format(i))
    i += 1

# With the break statement we can stop the loop 
# even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# With the continue statement we can stop the 
# current iteration, and continue with the next:
  d = 0
while d < 6:
  d += 1
  if d == 3:
    continue
  print(d)

# With the else statement we can run a block of code once 
# when the condition no longer is true:
v = 1
while v < 6:
  print(v)
  v += 1
else:
  print("v is no longer less than 6")



#####  For Loop #####
# A for loop is used for iterating over a sequence 
# (that is either a list, a tuple, a dictionary, a set, or a string).

#This is less like the for keyword in other programming languages, and works more
# like an iterator method as found in other object-orientated programming languages.

#With the for loop we can execute a set of statements, once for each item in a 
# list, tuple, set etc.

i = 0
for i in range(10):
    print("{} iteration through the FOR loop.".format(i))
    i += 1

# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Even strings are iterable objects, they contain a sequence of characters:
#Example Loop through the letters in the word "banana":

for y in "banana":
    print(y)


# With the break statement we can stop the loop before it has 
# looped through all the items:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


#With the continue statement we can stop the current iteration of 
# the loop, and continue with the next:
# Example Do not print banana:

fruits = ["apple", "banana", "cherry"]
for u in fruits:
  if u == "banana":
    continue
  print(u + " no banana") 

  # To loop through a set of code a specified number of times, we can use 
  # the range() function,
# The range() function returns a sequence of numbers, starting from 0 by 
# default, and increments by 1 (by default), and ends at a specified number.
# Using the range() function:

for t in range(6):
  print(t)


# The else keyword in a for loop specifies a block of code to be 
# executed when the loop is finished:
#Ex.Print all numbers from 0 to 5, and print a message when the loop has ended:

for c in range(6):
  print(c + 4)
else:
  print("Finally finished!")



