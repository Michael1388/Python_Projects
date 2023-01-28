# Python 3.10.9
#
# Michael LaRocca
# 
# Steps 242 OOP and Class Challenge
# 
# 1.	Create a class.
# 2.	Create an object.
# 3.	Assign values to object properties using the __init__() function.
# 4.	Create a method in a class.


class Stock():
    ticker = 'symbol'
    price = 0
    cap = "size"

    def __init__(self, ticker, price, cap): 
        self.ticker = ticker
        self.price = price
        self.cap = cap

    def information(self):
        msg = "Symbol: {}\nPrice: ${}\nCap Size: {}".format(self.ticker, self.price, self.cap) 
        return msg

    
# Step 243 INHERITANCE CHALLENGE 
# Create a child class that inherits functionality from a parent class.

class Nasdaq(Stock):
    ticker = 'symbol'
    price = 0
    cap = "size"
    
if __name__ == "__main__":

    BRCHF = Stock('BRCHF',10,'Small')
    print(BRCHF.information())

    INTC = Nasdaq('INTC', 28, 'Large')
    print(INTC.information())