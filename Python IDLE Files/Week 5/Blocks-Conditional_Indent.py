x = 5
if x > 2 :
    #Begin Conditional Block indent
    print('Bigger than 2') #conditional code
    print('Still bigger')
#End block and de-indent 
print('Done with 2') #sequential code

#Blank lines don't affect code
#for is a loop
for i in range (5) :
    #Begin Conditional Block indent
    print(i)
    if i > 2 :
        #nested code_ block within a block
        print('Bigger than 2')
    print ('Done with i', i)
    #End block and de-indent 
print('All Done')
 