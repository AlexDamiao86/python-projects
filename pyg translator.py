
"""O objetivo é criar um tradutor em que você digita uma unica palavra
e tira a primeira letra da palavra e a coloca no final da palavra original
depois coloca duas letras ay no final da palavra"""

pyg = 'ay'

original = input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:len(original)] + first + pyg
    print(new_word)
else:
    print('empty')
