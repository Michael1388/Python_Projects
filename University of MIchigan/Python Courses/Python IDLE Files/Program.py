
def start():
    people_dictionary = {'michael' : ['Male' , 'Weight 175'],
                         'holly' : ['Female' , 'Weight 125'],
                         'patrick' : ['Male' , 'Weight 195'],
                         'briar' : ['Female' , 'Weight 115'],
                         'adam' : ['Male' , 'Weight 215']}
    #print(people_dictionary)
    Name = input('Please type in a name: ').lower()
    print('You entered ' + Name.capitalize())
    try:                
        Persons_data = people_dictionary[Name]
        print('Name: ' + Name.capitalize())
        print('Sex: ' + Persons_data[0])
        print('Weight: ' + Persons_data[1])
        more()
    except:                 
        print('That name (as written) was not found in the dictionary.')
        more()
def more():
    x = input('Would you like to search for another name? ')
    if x == 'No': 
        quit()
    if x == 'Yes':
        start()
    else:
        print('Please enter Yes or No(case semsitive).')
        more()
start()
    


    
