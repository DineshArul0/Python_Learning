import random

import nltk
from nltk.corpus import brown

list_hangman = [
    '''
        _______
     |/      |
     |      (_)
     |         
     |        
     |         
     |
    _|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \  
     |        
     |         
     |
    _|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \\| 
     |        
     |         
     |
    _|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \\|/
     |        
     |         
     |
    _|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |         
     |
    _|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      /  
     |
    _|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      / \\ 
     |
    _|___
 ''', """  """
]

hangman = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/     """

print(f'Welcome to HangMan Game !! \nYou Have 6 lives Initially !!!\n {hangman}')
characters = int(input(f'Enter the Number of Characters you want to Find ?'))
nltk.download('brown')
valid_words = brown.words()
new_list = [word for word in valid_words if len(word) == characters]
word_to_be_found = random.choice(new_list).lower()
word_to_be_found = 'with'
original_word = word_to_be_found
# print(f'the words is {word_to_be_found} and the length of the word is {len(word_to_be_found)}')
lives = 6
result = ''
for index in range(0, characters):
    result += '_'
print(result)
guessed_letter = ''

while lives > 0:
    answer = input(f'Guess the letter !!!').lower()
    if word_to_be_found.__contains__(answer):
        print(f'Success')
        index = original_word.find(answer)
        result = result[:index] + answer + result[index + 1:]
        word_to_be_found = word_to_be_found.replace(answer, '', 1)
        print(result)
        print(f'You Have {lives} left')
        print(list_hangman[-(lives + 1)])
    else:
        if guessed_letter.__contains__(answer):
            print(f'You have already guessed the letter {answer}')
            continue
        lives -= 1
        print(f'Failed')
        print(list_hangman[-(lives + 1)])
        print(result)
        print(f'You Have {lives} left')
    if len(word_to_be_found) == 0:
        print(f'Great you procted the man and Won the Game !!!!')
        print(f'The word is {result}')
        break
    guessed_letter += answer
if len(word_to_be_found) > 0:
    print(f'You Ran Out of Lives !!! Game Over !! The word is {original_word}')
