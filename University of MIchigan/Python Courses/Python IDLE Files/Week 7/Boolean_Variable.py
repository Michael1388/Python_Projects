# Boolean, a Variable, is either True or False, that is all.
# If we just want to search and 'know if a value was found', we use a 'variable' that starts at False and is set ti True as soon as we 'find' what we are looking for.

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3:
        found = True
       # break        #could put a "Break" in here and it would quit becasue it was true and not run the rest of the loop becuse it will now alsways be true once it finds 3
    print(found, value)
print('After', found)

 