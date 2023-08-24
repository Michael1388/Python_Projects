#Now it’s time to put some of what you’ve learned to use!
#Create a program on your own that contains the following:
#Multiplies a number to the power of another number,
#An if, elif and else statement,
#A for loop,
#A while loop, and
#A dictionary.

 
import time
X = 100
print(X)
time.sleep(.5)
print(X ** 10)
number = 15
if number >= 100:
    print("100 or greater")
elif number <=50:
    print("number entered is 50 or less")
else:
    print("more than 50 but less than 100")
time.sleep(1.0)
print(number)
time.sleep(1.0)
#
for counter in range(1,10):
    print(counter)
    time.sleep(.25)
while counter < 22:
    print(counter + 2)
    counter = counter + 4
    time.sleep(.5)
print("Dictionary time")

time.sleep(1.0)


dictionary = {'Sedan' : 'Auto', 'Twin' : 'Plane', 'Broccoli' : 'Vegetable'}
print(dictionary)

print("Done")

    

