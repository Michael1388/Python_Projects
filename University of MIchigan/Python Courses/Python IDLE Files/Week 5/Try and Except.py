#Eliminate or Catch a traceback - an "insurance policy" agaist a blowup, if it does blow up it has an alternative code / pathway to continue
# surround a dangerous section of code with "try" and "except"
#if the code in the "try" works - the "except" is skipped
# if the code in the try fails - it jumps to the "except" section


astr = 'Hello Bob'
try:
    istr - int(astr)        #NOt going to work so goto "except"
except:
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)       #Works so print Second 123
except:
    istr = -1

print('Second', istr)


