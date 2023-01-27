# Python 3.10.9
# 
# Michael LaRocca
# 
# Step 237 Calss Inheritance 

class User:
    name = 'No name provided'
    email = ''
    password = '1234abcd'
    account_number = 0

# child classes 
class Employee(User):
    base_pay = 48.10
    department = 'IT'

class Customer(User):
    mailing_address = ''
    mailing_list = True

