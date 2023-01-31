# Python 3.10.9
# 
# SQLite Assignemnt Pt 8
# 
# If we wanted to loop over our result rows one at a time instead of fetching them 
# all at once, we would usually use a loop such as the following (modify your code 
# from exercise 7 to use this method of processing the results of the SQL query).
# 
# 
#

import sqlite3

peopleValues = (('Luigi', 'Vercotti', '43'), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    # table already exists so remove: c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)") 
    # alreay exists: c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues) 
# select all first and last names from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    # old code: for row in c.fetchall():
        # old code: print (row)
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
