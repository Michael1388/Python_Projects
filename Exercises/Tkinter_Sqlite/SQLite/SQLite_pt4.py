# Python 3.10.9
# 
# SQLite Assignemnt Pt 4
# 
# 
# 
# 
#

import sqlite3
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
   # c.executescript("""CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
   #                 INSERT INTO People VALUES('Ron', 'Obvious', 42)""")
    #Tuples 
    peopleValues = (('Luigi', 'Vercotti', '43'), ('Arthur', 'Belling', 28))
    c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues) 
    # ??? = placeholders for tuple values in peopleValues

