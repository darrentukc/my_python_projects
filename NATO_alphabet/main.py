# TODO create a dictionary in this format: {'A': 'Alpha', 'B': 'Bravo', ... }
# create a list of from a user input list

import pandas as pd


# with open('nato_phonetic_alphabet.csv') as file:
#     file = file.readlines()
# letter_list = [letter.strip('\n') for letter in file]
# letter_dict = {word.split(',')[0]: word.split(',')[1] for word in letter_list if word != 'letter,code'}
#
# name = input('Input name to convert\n')
# name_dict = {letter.upper(): letter_dict[letter.upper()] for letter in name}
# print(name_dict)

df = pd.read_csv('nato_phonetic_alphabet.csv')
letter_dict = {row.letter: row.code for (index, row) in df.iterrows()}

processing = True
while processing:
    name = input('Input name to convert\n').upper()
    try:
        name_list = [letter_dict[letter] for letter in name]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
    else:
        print(name_list)
        processing = False