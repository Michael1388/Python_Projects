Name = input('Name: ')
print('Hello ' + Name +
      '! Find out how long you\'ve been alive')
Age = int(input('Enter Age '))
print('You are ' + str(Age) + ' years old.')
Months = Age * 12
Days = Age *365
Minutes = Age * 365 * 24 * 60
Seconds = Age * 365 *24 * 60 * 60
print(Name + ' has been alive for about: ' +
      str(Months) + ' months or ' + str(Days) + ' days or '
      + str(Minutes) + ' minutes or ' + str(Seconds) + ' seconds!')



      
