# Python 3.10.9
# 
# SQLite Assignemnt Pt 1
# 
# 
# 
# 
#

import sqlite3
connection = sqlite3.connect('test_database.db')

c = connection.cursor()
# c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)" )
connection.commit()


# connection = sqlite3.connect(':memory:')

c.execute("DROP TABLE IF EXISTS People")

connection.close()


with sqlite3.connect('test_database.db') as connection:
    