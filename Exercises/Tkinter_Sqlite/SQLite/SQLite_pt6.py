# Python 3.10.9
# 
# SQLite Assignemnt Pt 6
# 
# 
# 
# 
#

import sqlite3


# get personal data from user AND insert into a tuple
firstName = input("Enter your First Name: ")
lastName = input("Enter your Last Name: ")
age = int(input("Enter your Age: "))
personData = (firstName, lastName, age)

# execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES (?,?,?)", personData)

# Can also update an entry Age
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("UPDATE People SET Age=? WHERE firstName=? AND lastName=?",(74, 'Johe', 'Walsh'))

# or update a name
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("UPDATE People SET firstName=? WHERE firstName=? AND lastName=?",('Joe', 'Johe', 'Walsh'))