# We create a new FUNCTION using the 'def' keyword followed by optional paramaters in () 
# We indent the body of the function
# This defines but does not execute the function - you still have to call it
def print_lyrics() :        # "print_lyrics" is the new function defined by the "def" keyword
    print('what you want printed here')
    print('and here and so on')
# But that is just a place holder a "Storage" or "Store" until Print_lyrics is called or invoked
# Next we will Invoke or Call them

x = 5
print('Hello')

def print_lyrics() :                        #this can be anywhere, it does not have to be here. by removing this instance, 
    print('what you want printed here')     #the instance above will execute when the call is executed below regardless of where this is inserted.
    print('and here and so on')

print('Yo')
print_lyrics()
x = x + 2
print(x)
