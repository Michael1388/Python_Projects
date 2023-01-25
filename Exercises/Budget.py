
 # called from "myQuiz.py"  
def calcBills():
    myBills = {'Electric': 120.00, 'Rent': 1200.00, 'Water_Sewer': 60.00, 'Car Insurance': 75.00, 'phone': 65.00}
    total = 0
    for value in myBills:
        total += myBills[value]

    owed = 'The total owed for bills this month is: ${}'.format(total)
    return owed

# print(calcBills()) # called from "myQuiz.py" 