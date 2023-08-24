#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. Desired Output = B
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

score = input("Enter Score between 0.0 and 1.0: ")
scre = float(score)
if scre > 1.0 :
    print ('Value out of range, please Enter Score between 0.0 and 1.0')   
elif scre >= 0.9 :
    print('A')
elif scre >= 0.8 :
    print('B')
elif scre >= 0.7 :
    print('C')
elif scre >= 0.6 :
    print('D')
elif scre < 0.6 :
    print('F')
else :
    print('Value out of range, please Enter Score between 0.0 and 1.0')




