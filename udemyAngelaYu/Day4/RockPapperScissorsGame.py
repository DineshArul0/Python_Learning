import random

print(f'Welcome to Rock papper Scissors Game !!')
condition = True
choices = ['rock', 'paper', 'scissor']
rockandrock = """    _______           _______
---'   ____)         (____   '---
      (_____)       (_____)
      (_____)       (_____)
      (____)         (____)
---.__(___)           (___)__.---
           Rock VS Rock"""
rockvsscissor = """ 
   _______           _______
---'   ____)       (_____________   '---
      (_____)       (__________)
      (_____)            (____)
      (____)              (____)
---.__(___)                (___)__.---
           Rock VS Scissor
"""
rockandpaper = """      _______           _______
---'   ____)        (_____________   '---
      (_____)      (__________)
      (_____)      (________)
      (____)       (________)
---.__(___)         (________)__.---
           Rock VS Paper"""

paperandpaper = """         _______           _______
---'   ________)        (________   '---
      (__________)     (__________)
      (_________)       (_________)
      (________)         (________)
---.__(_______)           (_______)__.---
           Paper VS Paper"""
paperandscissor = """        _______           _______
---'   ________)        (_____________   '---
      (__________)     (__________)
      (_________)            (____)
      (________)             (____)
---.__(_______)               (___)__.---
           Paper VS Scissor"""

scissorandscissor = """          _______           _______
---'   _____________)        (_____________   '---
      (__________)          (__________)
      (____)                      (____)
      (____)                      (____)
---.__(___)                        (___)__.---
           Scissor VS Scissor"""
human_Score = 0
computer_Score = 0
maximum_Point = int(input(f'What should be the maximum Score 3/5/10 ?'))
while condition:
    human = input(f'Whats your choice? rock  papper   scissor').lower()
    computer = random.choice(choices)
    if human == computer and human == 'rock':
        print(rockandrock)
        print(f'Draw')
        print(f'Score Human - {human_Score}  || Computer - {computer_Score}')
    elif human == computer and human == 'scissor':
        print(scissorandscissor)
        print(f'Draw')
        print(f'Score Human - {human_Score}  || Computer - {computer_Score}')
    elif human == computer and human == 'paper':
        print(paperandpaper)
        print(f'Score Human - {human_Score}  || Computer - {computer_Score}')
    elif human == 'rock' and computer == 'scissor':
        print(rockvsscissor)
        human_Score += 1
        print(f'You Win !!!')
        print(f'Score Human - {human_Score}  || Computer - {computer_Score}')
    elif human == 'rock' and computer == 'paper':
        print(rockandpaper)
        computer_Score += 1
        print(f'You Lose !!!')
        print(f'Score Human - {human_Score}  || Computer - {computer_Score}')
    elif human == 'paper' and computer == 'rock':
        print(rockandpaper)
        human_Score += 1
        print(f'You Win !!!')
        print(f'Score Human - {human_Score}  || Computer - {computer_Score}')
    elif human == 'paper' and computer == 'scissor':
        print(paperandscissor)
        computer_Score += 1
        print(f'You Lose !!!')
        print(f'Score  Human - {human_Score}  || Computer - {computer_Score}')
    elif human == 'scissor' and computer == 'rock':
        print(rockvsscissor)
        computer_Score += 1
        print(f'You Lose !!!')
        print(f'Score  Human - {human_Score}  || Computer - {computer_Score}')
    elif human == 'scissor' and computer == 'paper':
        print(paperandscissor)
        human_Score += 1
        print(f'You Win !!!')
        print(f'Score  Human - {human_Score}  || Computer - {computer_Score}')
    else:
        print(f'Please Enter Valid Data!!!')
    if human_Score == maximum_Point or computer_Score == maximum_Point:
        condition = False
        print(f'Game Over You Won !!!! Congratulations!!') if human_Score == maximum_Point else print(f'Game Over ! Computer Wins!! Better Luck Next Time !!')
