import random
from states import states
import sys

print('type !exit to exit the game')
words = list(open('words.txt','r').readlines())

def guess():
    tries = 6 #initialize guesses
    word = random.choice(words).rstrip() #remove trailing whitespaces from the chosen word
    full = "_"*len(word) #create the fancy blanks
    full_bank = list(full) #turn the blanks into a list for index editing
    while tries > 0: # intialize while loop for the try counter
        print(states(tries-1)) #print the state of hangman (hangmans body)
        print(''.join(full_bank))
        if ''.join(full_bank) == word: #if the full set of chosen words eqals the word picked, then ask for restart
            win()
        print(f'tries: {tries}')
        letter = input('letter: ')
        if letter in word: #initialize some logic if the letter is in the chosen word
            for x in range(0,len(list(word))): #make a variable x that goes through the list according to it's index
                if letter == list(word)[x]: # if the chosen letter equals the index x, then fullbank with index length x, gets changed to the letter
                    full_bank[x] = letter
        else:
            tries -=1 #if the letter is not in the word, then our try count decreases by 1.

        if tries == 0 or letter=="!exit":
            print(f'The correct word was {word}')
            again()
        if letter == word:
            full_bank = word
            

def win():
    print('You won')
    inp = input('Do you want to play again Y/N: ').lower()
    if inp == "y":
        play()
    elif inp == "n":
        sys.exit('Exited Game')
    else:
        sys.exit(0)
        
def again():
    inp = input('would you like to play again? Y/N: ').lower()
    if inp == "y":
        play()
    elif inp == "n":
        sys.exit('Exited Game')
    else:
        sys.exit(0)
def play():
    guess()

play()
