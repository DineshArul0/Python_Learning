print(f'Welvome to the roller Coaster !!!')
height = int(input(f'Enter you Height in cms'))
if height >= 120:
    print(f'You are eligible for the roller coaster Ride Hurreyyyyyyyyy!')
    age = int(input(f'Please Enter your age !!!'))
    if age >= 18:
        print(f'Adult roller Coaster Cost is $12')
        bill = 12
    elif 12 <= age < 18:
        print(f'Youth roller coaster Ride Cost is $7')
        bill = 7
    else:
        print(f'Child Roller Coaster Ride Cost is $5')
        bill = 5
    photo = input(f'Do you want Photo ? Yes/No').lower()
    if photo == 'yes': bill += 3
    print(f'Your Overall Cose is ${bill}')
else:
    print(f'Sorry !! you are not eligible for a ride!!')

"""Modulo Operator
It returns the remainder of the division"""
print(10 % 3)
"""Verify the odd or Even"""
print('Welcome to odd number verification!!!')
condition = True
while condition:
    number = int(input(f'Please Enter the Number You Want to Verify!:'))
    if number % 2 == 0:
        print(f'The given Number is Even')
    else:
        print(f'The given Number is Odd')
    str = input(f'Do you Wish to Continue ? Yes/No').lower()
    if str == 'yes':
        condition = True
    else:
        condition = False

"""Pizza Order Challenge"""
print(f'Welcome to Deekay Pizza Company !!! Happy to take your Order !!')
bill = 0
size = input(f'Enter the size of the pizza you want S - Small M - Medium L - Large').upper()
pep = input(f'Do you want to add pepperoni yes/No').lower()
cheese = input(f'Do you want to add the Cheese yes/No').lower()
if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
elif size == 'L':
    bill = 25
if pep == 'yes':
    if size == 'S':
        bill += 2
    elif size == 'M' or 'L':
        bill += 3
if cheese == 'yes': bill += 1
print(f'your pizza cost is ${bill}')
"""Logical operators
and or not"""
# if True and False:
#     print(True)
# else:
#     print(False)
# if True or False:
#     print(True)
# else:
#     print(False)
# if not True:
#     print(True)
# else:
#     print(False)
