#3.1 External Test 
#Hours 45, Rate 10.50: Hourly x 40 at rate, over 40 at 1.5 rate/ correct answer is 498.75

hrs = input("Enter Hours:")
rte = input("Enter Rate:")
hours = float(hrs)
rate = float(rte)
if hours > 40 :
    reg = hours * rate
    otpay = (hours - 40.0) * (rate * 0.5)
    xpay = reg + otpay
else: 
    xpay = hours * rate 
print(xpay)

#add an Except by 
hrs = input("Enter Hours:")
rte = input("Enter Rate:")
try:
    hours = float(hrs)
    rate = float(rte)
except:
    print('Error, please enter numeric input')
    quit()
if hours > 40 :
    reg = hours * rate
    otpay = (hours - 40.0) * (rate * 0.5)
    xpay = reg + otpay
else: 
    xpay = hours * rate 
print(xpay)






##elif hours > 40 :
  ##  print("Pay:$", hours * rate *1.5)

 # sample    
#if h <= 40:
 #   pay = h*rate
#elif h > 40:
 #   pay = ((h-40)*rate*1.5)+rate*40 
#OR another sample
 
#if h <= 40:
#    print pay

#if h > 40:
#    pay = (40*r)+(h-40)*(1.5*r)
#    print pay