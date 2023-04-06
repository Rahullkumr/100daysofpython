from art import logo
import random
print("\033[36m",logo,"\033[0m")

answer = random.randint(10,91)
attempts = 0

def choose():
	global attempts
	difficulty = input("\nchoose difficulty. Type 'easy' or 'hard': \n")
	if difficulty == 'easy':
		attempts = 10
		guessfn()
	elif difficulty == 'hard':
		attempts = 5
		guessfn()
	else:
		print("Enter valid word")
		choose()
		
def guessfn():
	global attempts
	global answer
	if attempts == 0:
			print("\033[32mYou've run out of guesses, You lose.\033[0m")
	while attempts:
		print(f"You have \033[31m{attempts}\033[0m attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))
		if guess == answer:			
			attempts = 0
			print("\033[32m")
			print(f"You got it!. The answer was {answer}")
			print("\033[0m")
		elif (answer - 2) < guess < (answer + 2):
			attempts -= 1
			print("\033[32mToo close.\033[0m\nGuess again.\n")
			guessfn()
		elif guess <= answer - 2:
			attempts -= 1
			print("Too low.\nGuess again.\n")
			guessfn()
		else:
			attempts -= 1
			print("Too high.\nGuess again.\n")
			guessfn()

print("Welcome to the Number Geussing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(answer) 
choose()