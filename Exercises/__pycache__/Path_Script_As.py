

import os


#listdir() method from the OS module to iterate 
# through all files within a specific directory.
directoryPath = 'C:\\P\\'

os.listdir(path=directoryPath)
for file in (os.listdir(path=directoryPath)):
    if (file.find(".txt") != -1):
        print(file, os.path.getmtime(directoryPath + file))
    
    
    #if '.txt' in iterate:
       # print(iterate)
    # print(os.listdir(path='C:\\P\\'))


# return getmtime() for files in path to find the latest 
# date that each text file has been created or modified.

