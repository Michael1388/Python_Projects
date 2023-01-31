# Python 3.10.9
# 
# SQLite Assignemnt Pt 7
# 
# 
# 
# 
#

import sqlite3

peopleValues = (('Luigi', 'Vercotti', '43'), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    #c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues) 
# select all first and last names from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    for row in c.fetchall():
        print (row)
