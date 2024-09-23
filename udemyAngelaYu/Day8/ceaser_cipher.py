import string

ceaser = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          """
cipher = """
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88               """


def encrypt(word1, shift1):
    encrypted_word = ''
    for character in word1:
        index = ord(character)
        shifted_index = index + shift1
        if not shifted_index <= 122:
            shifted_index = shifted_index - 26
        encrypted_word += chr(shifted_index)
    return encrypted_word


def decrypt(word1, shift1):
    decrypted_word = ''
    for character in word1:
        index = ord(character)
        shifted_index = index - shift1
        if shifted_index < 97:
            shifted_index = shifted_index + 26
        decrypted_word += chr(shifted_index)
    return decrypted_word


alphabet = list(string.ascii_lowercase)


def encrypt_udemy(word_original, shift_position):
    output_text = ''
    for letter in word_original:
        shifted_position = alphabet.index(letter) + shift_position
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    return output_text


def decrypt_udemy(word_original, shift_position):
    output_text = ''
    for letter in word_original:
        shifted_position = alphabet.index(letter) - shift_position
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    return output_text


condition = 'yes'
print(f'Welcome to ceaser cipher \n{ceaser} {cipher}')
while condition == 'yes':
    word = input(f'Enter a random worrd')
    shift = int(input(f'Enter the shift !!'))
    flow = input(f'Do you want encode/decode ?').lower()
    if flow == 'encode':
        print(f'The Emcoded value is {encrypt(word, shift)}')
        print(f'The Emcoded value is {encrypt_udemy(word, shift)}')
    else:
        print(f'The Decoded value is {decrypt(word, shift)}')
        print(f'The Decoded value is {decrypt_udemy(word, shift)}')
    condition = input(f'Do you want to continue yes/no?').lower()
