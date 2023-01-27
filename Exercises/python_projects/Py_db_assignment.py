

"""Assignment step 223: Write a script that creates a database and adds 
new data into that database. That also reads through that list and finds 
only those files that end with .txt, adds those files to your db 
and prints them out """

import sqlite3 # import sqlite3 module 

#create and name a new db
dbconx = sqlite3.connect("file_list.db") #connect to db

# Create table in db with 1 additional text column
with dbconx: #open db
    cur = dbconx.cursor() # create cursor to control the actions we want to command in 
    # have the cursor execute the creation of the named table and column with the set parameters of integer and text 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            col_file TEXT)")
    dbconx.commit()    # commit changes to db
dbconx.close()  # close db


dbconx = sqlite3.connect("file_list.db") # connect to db again
# Insert assignment fileList
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
# create a loop to check for the desired files and print them
for item in fileList: #create a variable called item and search the fileList
    if item.endswith('.txt'): #specify the file type we want to find
        with dbconx: # open db
            cur = dbconx.cursor() 
            cur.execute("INSERT INTO tbl_file(col_file) \
        VALUES (?)", ([item,]))
        print(item) # print the results
  
    dbconx.commit() #commit to db 
dbconx.close() #close db

    






    