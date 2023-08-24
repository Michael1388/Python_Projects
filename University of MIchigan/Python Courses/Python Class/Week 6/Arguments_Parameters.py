# Argument - is a value we pass into the "function" as its "input" when we call the function.
# big = max('Hello world') # Hellow world is the argument here
#Parameter is a variable we use in the function "definition"

def greet(lang) : # "lang" in this case is the Alias which will refer to the first parameter 
    if lang =='es' :
        print('Hola') 
    elif lang == 'fr' :
        print('Bonjour')
    elif lang =='it' :
        print('Ciao')
    else:
        print('Hello')

greet('en') #invoke each "greet"
greet('es')
greet('fr')
greet('it')
