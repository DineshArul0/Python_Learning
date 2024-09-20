import random

names = ['Dinesh', 'vel', 'ajith', 'sangs', 'bharathima']
for name in names:
    print(name)
Marks_Of_Students = [int(random.randint(35, 100)) for index in range(0, 100)]
Highest_Mark = 0
for mark in Marks_Of_Students:
    if mark > Highest_Mark:
        Highest_Mark = mark
print(Highest_Mark)
Marks_Of_Students.sort()
print(Marks_Of_Students[-1])
print(max(Marks_Of_Students))
for number in range(1, 11):
    print(number)
total = 0
for number in range(1, 101):
    total += number
print(total)
