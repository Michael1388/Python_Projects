
J = 50
K = 5
print(J+K)

if J > 25:
    print('J is the winner!')

B = 20
if B == 20:
    print('20 is equal to B')


name = 'Ashley'
print(name.lower())

print(name.upper())

print(name[0])

print(name[2])

listA = ['mother', 'father', '1970', '1965'];
print(listA[3])

tupA = ('brother', 'sister', '1990', '1992', '1993', '1995')
print(tupA[1:4])


date = '03/13/2021'

split_the_date = date.split('/')
print(split_the_date)
['03', '13', '2021']


date = '03/13/2021'

split_the_date = date.split('/')
print(split_the_date)
['03', '13', '2021']

print(split_the_date[0])
03
print(split_the_date[1])
13
print(split_the_date[2])
2021

print("Monthsplit_the_date[0])
      
SyntaxError: unterminated string literal (detected at line 1)
print("Month: "split_the_date[0])
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('Month: ' + split_the_date[0])
      
Month: 03
print('Day: ' + split_the_date[1])
      
Day: 13
print('Year: ' + split_the_date[2])
      
Year: 2021
