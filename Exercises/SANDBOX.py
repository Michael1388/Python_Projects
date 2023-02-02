myList = ('Pink', 'Black', 'Green', 'Teal', 'Red', 'Blue')
for color in myList:
    if color == 'Black':
        print('The chosen color is Green.')


num1 = 3
num2 = 1
answer = "The answer is {}.".format(num1 + num2)
print(answer)



import datetime
import pytz


# prints the now time on my machine
#x = datetime.datetime.now()
#print(x)

if dt_euro_lon.strftime("%Y:%m:%d %H:%M:%S %Z %z") > 09:00 

else: 
    print('closed')

    ("%Y:%m:%d %H:%M:%S %Z %z")

>= 9 == 9
> 9 == 10

<= 5 == 5
< 5 == 4 

    if londonHour >= 9:
    if londonHour <= 5:
        print("open")

if londonHour >= 9:
    print("open")
elif londonHour <= 5:
    print("open")

            for i in source_files:
            # checks source file time stamp
            fileStamp = os.path.getmtime(source + '/' + i)
            #print(fileStamp)
            #print(datetime.datetime.fromtimestamp(fileStamp).strftime("%H:%M %S")) #testing my code
            fileStampDate = datetime.datetime.fromtimestamp(fileStamp)
            current = datetime.datetime.now()
            #print("Now: " +  str(current.strftime("%H:%M %S"))) #testing code
            yesterday = current - timedelta(days = 1)
            if (fileStampDate >= yesterday):
                # moves each file from the source to the destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')
            #added extra feature to see files that were not transferred to validate differences
            # but can see where in a folder of hundreds of files this would not be desirable 
            else:
                print(i + ' was not transfered') 