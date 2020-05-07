import random

lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'
geussed_word_correctly = False

def update_clue(geussed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if geussed_letter == secret_word(index):
            clue[index] = geussed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print('Lives Left: ' + heart_symbol * lives)
    geuss = input('Geuss a letter or the whole word: ')

    if geuss == secret_word:
        geussed_word_correctly = True
        break

    if geuss in secret_word:
        update_clue(geuss, secret_word, clue)
    else:
        print('Incorrect. You lose a life')
        lives = lives - 1
if geussed_word_correctly:
    print('You won! The secret word was ' \
    + secret_word)

else:
    print('You lost! The secret word was ' \
    + secret_word)
