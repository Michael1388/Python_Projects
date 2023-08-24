#ELIF ELSE/IF
#Only going to do one function not all three - One will run , the others(2) will not
x = 5         # this is the variable filed which determines which of the three functions will print
               # I would think you could use the "input" filed here to create a user enter function - see new file "Multi ELIF with Input"
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('Large')
print('All done')

# No else
x = 15
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')

print('All done')

#Could do multiple ELIF's 
x = 25 
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
elif x < 20 :
    print('Big')
elif x < 30 :
    print('Bigger')
elif x < 40 :
    print('Large')
elif x < 60 :
    print('Larger')
elif x < 100 :
    print('Largest')
else :
    print('Gigantic')
print('All done')