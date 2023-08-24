def computepay(hrs, rte):
    return xpay

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

xpay = computepay(10, 20)
print("Pay", xpay)


