print(f'Welcome to split wise Calculator !!!')
total = float(input(f'Enter the Overall Spent Amount :'))
people = int(input(f'Enter the number of people :'))
splitmethod = input(f'Enter the split method equal/shares/percentages?')
splitmethod = splitmethod.lower()
individualprice = 0
if splitmethod == 'equal':
    result = round(total / people, 2)
elif splitmethod == 'shares':
    share = int(input(f'Enter your share'))
    result = round((total / people) * share, 2)
else:
    percentage = float(input(f'Enter your percentage !!'))
    result = round((total * percentage) / 100, 2)
print(f'You should pay Rs.{result}')
