
#creat a dictionary

car_dict1 = {
    'brand': 'Infiniti',
    'model': 'G35',
    'year': '2004'
}
print(car_dict1)

# Use get() method
r = car_dict1.get('model')
print(r)

#3.	Change a value 

car_dict1['year'] = 2023
print(car_dict1)

#4.	Add an item 
car_dict1['color'] = 'champange'
print(car_dict1)

#5. Create a nested dictionary
car_dict2 = {
    'car_1': {
    'make': 'Infiniti',
    'model': 'G35',
    'year': '2004',
    'color': 'champange'
    },
    'car_2': { 
    'make': 'Infiniti',
    'model': 'G35',
    'year': '2023',
    'color': 'red'
}
}

print(car_dict2)

#6.	Use the fromkeys() method 

x= dict.fromkeys('model')
print(x)

