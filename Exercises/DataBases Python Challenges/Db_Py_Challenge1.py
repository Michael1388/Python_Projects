# Python 3.10.9
# 
# Michael La Rocca
# 
# Python Course:
# DATABASES AND PYTHON CHALLENGE
# Step 305 
# 
# 1. Create a database table in RAM named Roster that includes the fields ‘Name’, ‘Species’ and ‘IQ.’
# 2. Populate your new table with the following values:

# 1 Jean-Baptiste Zorg, Human, 122
# 2 Korben Dallas, Meat Popsicle, 100
# 3 Ak'not, Mangalore, -5
# 
# 3. Update the Species of Korben Dallas to be Human.
# 4. Display the names and IQs of everyone in the table who is classified as Human.
# 
# 
# 
#

import sqlite3
connection = sqlite3.connect(':memory:')

peopleValues = (('Jean-Baptiste Zorg', 'Human', '122'), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak not', 'Mangalore', -5))

with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)") 
    c.executemany("INSERT INTO Roster VALUES(?,?,?)", peopleValues) 

# Update the Species of Korben Dallas to be Human.
with sqlite3.connect(':memory:') as connection:
   #c = connection.cursor()
    c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",('Human', 'Korben Dallas', 100))


#  Display the names and IQs of everyone in the table who is classified as Human.
    c.execute("SELECT Name, IQ FROM Roster WHERE Species= 'Human'")
    # old code: for row in c.fetchall():
        # old code: print (row)
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
