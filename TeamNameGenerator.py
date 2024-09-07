import random

print(f'Welcome to the team name Generator !!!!!')
cricketer = input('Enter your favourite cricketer Name !!')
number_answer = input('Do you want to input Number ? Yes/No:')
number_answer = number_answer.lower()
number = 0
if number_answer == 'yes':
    number = int(input('Enter the Number of players'))
list = ['spartans', 'pullaingos', 'devils', 'masters']
name = input('Enter Your Name !')
middle = random.choice(list)
result = f'{cricketer} {middle}'
if number > 0:
    result += " " + str(number)
print(f'Hello {name}: Your Team Name is {result}')
