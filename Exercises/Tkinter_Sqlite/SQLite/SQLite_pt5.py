# Python 3.10.9
# 
# SQLite Assignemnt Pt 5
# 
# 
# 
# 
#

import sqlite3

# get personal data from user
firstName = input("Enter your First Name: ")
lastName = input("Enter your Last Name: ")
age = int(input("Enter your Age: "))

# execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)