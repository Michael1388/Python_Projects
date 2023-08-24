# Combining previous exercises File: Arguments_Parameters changing print to return and File: Return Values


def greet(lang) : # "lang" in this case is the Alias which will refer to the first "parameter" 
    if lang =='es' :
        return 'Hola'
    elif lang == 'fr' :
        return 'Bonjour'
    elif lang =='it' :
        return 'Ciao'
    else:
        return 'Hello'

print(greet('en'), 'Josh')     # add parameter
print(greet('es'), 'Ethan') 
print(greet('fr'), 'Holly') 
print(greet('it'), 'Allie') 

