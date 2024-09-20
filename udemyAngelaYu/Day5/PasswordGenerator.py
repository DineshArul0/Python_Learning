import random

small_alphabets = list(map(chr, range(97, 123)))
capital_alphabets = [char.upper() for char in small_alphabets]
numbers = [number for number in range(0, 10)]
special_characters = ['!', '@', '$', '#', '%', '&', '*', '.']
print(small_alphabets, capital_alphabets)
Total_Number = int(input(f'How many characters do you want ?'))
alphabet = int(input(f'How many alphabets?'))
num = int(input(f'How many Numbers?'))
special = int(input(f'How many special Characters?'))
temp = []
num += alphabet
special += num
for index in range(0, Total_Number):
    if index < alphabet:
        temp.append(random.choice(small_alphabets))
    elif index <= num:
        temp.append(random.choice(numbers))
    elif index <= special:
        temp.append(random.choice(special_characters))
    else:
        temp.append(random.choice(capital_alphabets))
random.shuffle(temp)
password = ''
for charac in temp:
    password = f'{password}{charac}'
print(f'Your password is :{password}')
