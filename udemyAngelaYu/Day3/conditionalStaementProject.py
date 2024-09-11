print(f'Welcome to the treassure Hunt Game !!!')
str = input(f'Hi Which direction do you want to move left/right/up/down?').lower()
if str == 'left' or str == 'right' or str == 'up':
    str = input(f'Hi Which direction do you want to move left/right/up/down?').lower()
    if str == 'left' or str == 'right' or str == 'down':
        str = input(f'Do you want to swim of wait swim/wait?').lower()
        if str == 'swim':
            print('game over')
        else:
            str = input(f'Do you want to dig of wait dig/wait?').lower()
            if str == 'dig':
                str = input(f'Do you want to dig of wait dig/wait?').lower()
                if str == 'wait':
                    print("You Won")
                else:
                    print('Game Over')
            else:
                print('Game Over')
    else:
        print("Game Over")
else:
    print('Game Over')
