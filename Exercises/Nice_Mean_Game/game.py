# Python 3.10.9
#
# Michael LaRocca  
#
# The Tech Academy - Python course, creating our first game together.
# Demonstrating how to pass variables from function to function while 
# producing a functional game. 
#
# Remember, function_name(variable) _means that we pass in the variable.
# return variable _means that we are returning the variable back to the 
# calling function.


# declare and define the function - start
def start(nice=0,mean=0,name=""): #by default, values will be numeric, numeric, string. 
    #get user's name
    name = describe_game(name) #variable called name = function called describe game and pass in name
    nice,mean,name = nice_mean(nice,mean,name) # 3 variables = function called nice_mean gets 3 values passed into it.

#declare and define the function - describe_game
def describe_game(name):
    """
    check if this is a new game or not.
    If it is new, get the user's name.
    If it i snot a new game, thank the player for playing again 
    and continue with the game.
    """
    # meaning, if we do not already have this user's name,
    # then they are a new player and we need to get thier name
    if name != "":
        print("\nThank you for playing again, {}!".format(name)) # \ = escape n = new line \n
    else:
        stop = True
        while stop: # while stop is true
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your choices.")
                    stop = False #switches true to false ends the while loop
    return name

# define nice_mean function 
def nice_mean(nice,mean,name):
    stop = True
    while stop: # .. is true
        show_score(nice,mean,name) #call new function "show_score"
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger stares at you, \n turns, and somberly walks away...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the new function - score() 


# define - show_score() function
def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


# define  - score
def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)  

# define - win and call new function - again
def win(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call new "again" function and pass in our variables
    again(nice,mean,name)
    

#define lose function
def lose(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("\nAhhh your fate is sealed, game over! \n{}, you're doomed to live in a dirty beat-up \nvan, down by the river, wretched and alone!".format(name))
     # call "again" function and pass in our variables
    again(nice,mean,name)



# define again call new function - reset
def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False # stops the loop
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False # stops the loop
            quit() # built in Python function
        else: # did you understand the question...lol.. here let me ask again
            print("\nEnter ( Y ) for 'YES' ( N ) for 'NO':\n>>> ") # repeats the loop with the y or n provided to activate the next step

#define reset
def reset(nice,mean,name):
    nice = 0 # resets the value
    mean = 0
    # Notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)




if __name__ == "__main__":
    start()    