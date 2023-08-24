# Type Conversions - 
#Function Call

#print float(99) / 100

i = 42      #string
       #type(i)
f= float(i)         # convert to float
print(f)            # 42.0

        #type(f) float
print(1 + 2 * float(3) / 4 - 5)         #-2.5

# String conversions
sval = '123'
#print(sval + 1)        #blows up TRACEBACK because 123 is a string 
ival = int(sval)        # convert to integer int()
print(ival +1)      # returns 124 
