
#create a set
myset = {"one", "green", 'red', 'two'}
print(myset)

# remove an item
myset.remove('red')
print(myset)

myset.add('3')
print(myset)

yourset = {'3', '4'}
print(yourset)

y = yourset.difference(myset)
print(y)

