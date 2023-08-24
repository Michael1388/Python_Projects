# Countinhg in a loop
# TO 'count' how many times we execute a loop, we introduce a 'counter' variable that starts with 0'
# and we "add 1 to it each time through the loop.' 
zork = 0        #WHere we start we have seen nothing so we start at )
print('Before', zork)                        # How many have we seen Before? 0
for thing in [9, 41, 12, 3, 74, 15] :       # thing is the Iteration Variable
    zork = zork + 1                         # insert the increment
    print(zork, thing)                      #
print('After', zork)                        #

# Summing in a loop (Total)
# TO 'add up' a vlaue we encounter in a loop, we introduce a '"sum" variable that starts with 0' (SUM vs Counter in example above)
# and we "add the 'value' to the sum each time through the loop.' (We add value"thing" rather than "1")
zork = 0        #WHere we start we have seen nothing so we start at )
print('Before', zork)                        # How many have we seen Before? 0
for thing in [9, 41, 12, 3, 74, 15] :       # thing is the Iteration Variable
    zork = zork + thing                       # insert the increment "THIS IS THE DIFFERENCE from above example, We add thing not 1"
    print(zork, thing)                      #
print('After', zork)     

# Finding the AVERAGE in a Loop
# AN 'average' just combines the 'counting' and the 'sum' patterns and "divides when the loop is done".
count = 0
sum = 0        #
print('Before', count, sum)                        # 
for value in [9, 41, 12, 3, 74, 15] :       # 
    count = count + 1                       # 
    sum = sum + value
    print(count, sum, value)                      #
print('After', count, sum, sum / count)
