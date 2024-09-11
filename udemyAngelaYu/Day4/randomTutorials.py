import math
import random

randomnumber = random.random() * 10
print(randomnumber)
print(int(round(randomnumber)))
print(math.ceil(randomnumber))
print(math.floor(randomnumber))
randomnumber = random.uniform(1, 2)
print(randomnumber)
coins = ['head', 'tail']
print(random.choice(coins))
randomnumber = random.randint(2, 5)
print(randomnumber)
fruits = ['apple', 'orange', 'pappaya', 'liche', 'mango']
print(fruits[2], fruits[-4], fruits[3])
fruits[2] = 'grape'
fruits.append('pappaya')
print(fruits)
print(random.choice(fruits))
print(fruits[random.randint(0, len(fruits) - 1)])
