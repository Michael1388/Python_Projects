# Python 3.10.9
# 
# Michael La Rocca
# 
# Python Course:
# DATETIME CHALLENGE
# Step 308
# 
# 1.Import the datetime module and any others to aid in time zone 
# calculations.
#  
# 2.Create a script that will find out the current times in the 
# Portland HQ and NYC and London branches. Then, compare that time 
# with each branch's hours to see if they are open or closed.
#  
# 3.Print out to the screen the three branches and whether they are 
# open or closed.
#  


import datetime
import pytz

"""import pytz

print('Timezones')
for timeZone in pytz.all_timezones:
    print(timeZone)"""

# ("%Y:%m:%d %H:%M:%S %Z %z")
# UTC timezone Datetime
dt_local = datetime.datetime.now(pytz.utc)
# print("UTC DateTime:", dt_local.strftime("%Y:%m:%d %H:%M %p"))

# convert UTC timezone to 'US/Pacific'
dt_us_pacific = dt_local.astimezone(pytz.timezone('US/Pacific'))
print("\nUS Portland Branch HQ hours are 9am to 5pm: \nCurrent time is:", dt_us_pacific.strftime("%I:%M %p")) # prints local time

portlandHour = int(dt_us_pacific.strftime("%H"))

if portlandHour >= 9 and portlandHour <= 17:
    print("Portland HQ Branch is OPEN\n")
else: 
    print('Portland HQ Branch is CLOSED\n')

# Convert 'US/Pacific' timezone to US/Eastern (America/New_York)
dt_us_eastern = dt_us_pacific.astimezone(pytz.timezone('America/New_York'))
print("US New York Branch hours are 9am to 5pm: \nCurrent time is:", dt_us_eastern.strftime("%I:%M %p"))

newyorkHour = int(dt_us_eastern.strftime("%H"))

if newyorkHour >= 9 and newyorkHour <= 17:
    print("New York Branch is OPEN\n")
else: 
    print("New York Branch is CLOSED\n")

# Convert US/Eastern timezone to London (Europe/London) timezone
dt_euro_lon = dt_us_eastern.astimezone(pytz.timezone('Europe/London'))
print("UK London Branch hours are 9am to 5pm: \nCurrent time is:", dt_euro_lon.strftime("%I:%M %p"))

londonHour = int(dt_euro_lon.strftime("%H"))

if londonHour >= 9 and londonHour <= 17:
    print("London Branch is OPEN\n")
else: 
    print('London Branch is CLOSED\n')

