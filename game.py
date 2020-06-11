import random
from states import states

print('type !exit to exit the game')
words = list(open('words.txt','r').readlines())

def guess():
    tries = 6
    word = random.choice(words).rstrip()
    full = "_"*len(word)
    full_bank = list(full)
    while tries > 0:
        print(states(tries-1))
        if ''.join(full_bank) == word:
            print('You won')
            inp = input('Do you want to play again Y/N').lower()
            if inp == "y":
                play()
            elif inp == "n":
                break
        print(''.join(full_bank))
        print(f'tries: {tries}')
        letter = input('letter: ')
        if letter in [i for i in word]:
            for x in range(0,len(list(word))):
                if letter == list(word)[x]:
                    full_bank[x] = letter
        else:
            tries -=1

        if tries == 0 or letter=="!exit":
            print(f'The correct word was {word}')
            break

def play():
    guess()

play()