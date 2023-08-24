#Functions - Sequential, conditional, iterations and store and reuse
# THis is store and reuse
# D_R_Y dont repeat yourself
def thing() :           #DEF - start the definition of a function / define function ends in a colon :
                        # you get to name the 'thing' FUNCTION you're "storing" - we named it "thing" here lol
                        # There are some optional parameters that can be put in the parentesis but we're using none at this point
    print('Hello')      # Indent to define function 
    print('Fun') 
                        # Space NOT EXECUTED or outputted UNITL IT IS CALLED or INVOKE
thing()                 # This is CALLING the "thing" FUNCTION - print Hello print FUN - this is D_R_Y
print ('Zip')
thing()                 # Call Again - THUS - D_R_Y