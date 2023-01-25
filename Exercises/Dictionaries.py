dict_A = {'index':1,'index2':2, 'index3':377}
print(dict_A)

print(dict_A['index3'])

dict_users = {'em_1001': {'fname': 'John', 'lname': 'Glen', 'phone': '123-456-7890'},
'em_1002': {'fname': 'Jane', 'lname': 'Deer', 'phone': '234-456-7990'} }

print(dict_users['em_1002'])

print(dict_users['em_1002']['phone'])

print('User: {} {} \nPhone: {}'.format(dict_users['em_1002']['fname'],dict_users['em_1002']['lname'],dict_users['em_1002']['phone'],))




