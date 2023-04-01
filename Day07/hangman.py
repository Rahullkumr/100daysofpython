"""
#Step 1
# --------------------------------------------------

import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if guess == letter:
        print("present")
    else:
        print("not present")

# Step 2
# ---------------------------------------------------

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
length_chosen_word = len(chosen_word)

for _ in range(length_chosen_word):
    display.append("_")

print(display)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for index in range(0, length_chosen_word):
    if chosen_word[index] == guess:
        display[index] = guess

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)

#Step 3
# ----------------------------------------------------

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
length_chosen_word = len(chosen_word)

# create blanks
display = []
for _ in range(length_chosen_word):
    display.append("_")
    
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()   
    # check guessed letter
    for index in range(length_chosen_word):
        if chosen_word[index] == guess:
            display[index] = guess
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")

#Step 4
# ----------------------------------------------------------

import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
length_chosen_word = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

# create blanks
display = []
for _ in range(length_chosen_word):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # check guessed letter
    for index in range(length_chosen_word):
        if chosen_word[index] == guess:
            display[index] = guess

    #TODO-2: - If guess is not a letter in the chosen_word, then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose.")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
"""

#Step5
# -------------------------------------------------------------------------------------
from replit import clear
import random
import hangman_words
from hangman_art import logo, stages

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
length_chosen_word = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# create blanks
display = []
for _ in range(length_chosen_word):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}\n")
    # check guessed letter
    for index in range(length_chosen_word):
        if chosen_word[index] == guess:
            display[index] = guess

#Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word
        print(
            f"You guessed {guess}, that's not in the word.\nYou lose a life.\n")
        lives -= 1
    if lives == 0:
        end_of_game = True
        clear()
        print('''
                       _                
 _   _  ___  _   _    | | ___  ___  ___ 
| | | |/ _ \| | | |   | |/ _ \\/ __|/ _ \\
| |_| | (_) | |_| |   | | (_) \\__ \\  __/
 \__, |\___/ \__,_|   |_|\\___/|___/\\___|
 |___/                                 
''')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print('''
                                 _         
                                (_)        
  _   _  ___  _   _  __      __  _   _ __  
 | | | |/ _ \\| | | | \\ \\ /\\ / / | | | '_ \\ 
 | |_| | (_) | |_| |  \ V  V /  | | | | | |
  \\__, |\\___/ \\__,_|   \\_/\\_/   |_| |_| |_|
   __/ |                                   
  |___/                                    

''')

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
