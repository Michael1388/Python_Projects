#Elephant, Mouse, Cat game
def start():
    print('This is my Elephant Mouse Cat game!')
    Player_One = 'Holly'
    Player_Two = 'Michael'

    def choices(Player_One_Choice, Player_Two_Choice):
        if Player_One_Choice == 'elephant' and Player_Two_Choice == 'mouse':
            return('Mouse scares Elephant! ' + Player_Two + ' wins!')
        elif Player_One_Choice == 'mouse' and Player_Two_Choice == 'elephant':
            return('Mouse scares Elephant! ' + Player_One + ' wins!')
        elif Player_One_Choice == 'cat' and Player_Two_Choice == 'mouse':
            return('Cat eats Mouse! ' + Player_One + ' wins')
        elif Player_One_Choice == 'elephant' and Player_Two_Choice == 'cat':
            return('Elephant smashes Cat! ' + Player_One + ' wins!')
        elif Player_One_Choice == 'mouse' and Player_Two_Choice == 'cat':
            return('Cat eats Mouse!' + Player_Two + ' wins!')
        elif Player_One_Choice == 'cat' and Player_Two_Choice == 'elephant':
            return('Elephant smashes Cat! ' + Player_Two + ' wins')
        elif Player_One_Choice == Player_Two_Choice:
            return('Holly and Michael tied!')
        else:
            return('Please type Elephant, Mouse or Cat!')
        
    Player_One_Choose  = input('Does ' + Player_One + ' choose Elephant, Mouse or Cat? ').lower()
    Player_Two_Choose = input('Does ' + Player_Two + ' choose Elephant, Mouse or Cat? ').lower()
    print(choices(Player_One_Choose, Player_Two_Choose))

    def Play_Again ():
        x = input('Would you like to play another game? ').lower()
        if x == 'No'.lower():
            quit()
        if x == 'Yes'.lower():
            start()
        else:
            print('Please enter Yes or No. Thank you!')
            Play_Again()
    Play_Again()
start()

