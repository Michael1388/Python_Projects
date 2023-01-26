import os

fName = 'Hello.txt'

fpath = 'C:\\A\\'

abPath = os.path.join(fpath, fName)
print(abPath)