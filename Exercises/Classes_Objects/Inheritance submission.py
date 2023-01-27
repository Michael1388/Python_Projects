# Python 3.10.9
#
# Michael LaRocca
# 
# Step 238
# 
# INHERITANCE SUBMISSION ASSIGNMENT:
# Create two classes that inherit from another class.
# Ensure each child has at least two of their own attributes.
# Add comments throughout your Python explaining your code.

#Create class
class User: 
    name = 'Provide Name'
    password = '12!!34abCD'
    email = ''
    phone = '123-456-7890'
    
#create child classes of User class
class Student(User): 
    course = "name of enrolled study" # additional attributes
    gpa = ''

class Client(User):
    id = ''     # additional attributes
    project_name = "name"
    