from replit import clear
from game_data import data
import art
import random


def game():
	score = 0
	should_continue = True
	A = random.choice(data)
	B = random.choice(data)

	print("\033[31m", art.logo, "\033[0m")
	while should_continue:
		print(
		 f"Compare A: \033[36m{A['name']}, {A['description']}, {A['country']}\033[0m"
		)
		print(art.vs)
		print(
		 f"Against B: \033[36m{B['name']}, {B['description']}, {B['country']}\033[0m"
		)
		ask = input("\nWho has more followers? Type 'A' or 'B': ").lower()

		if ask == "a":
			if A["follower_count"] > B["follower_count"]:
				score += 1
				clear()
				print("\033[31m", art.logo, "\033[0m")
				A = B
				B = random.choice(data)
				print(f"You're right! Current Score: {score}")
			else:
				should_continue = False
				clear()
				print("\033[31m", art.logo, "\033[0m")
				print(f"Sorry that's wrong. Final Score: {score}")
		elif ask == "b":
			if B["follower_count"] > A["follower_count"]:
				score += 1
				clear()
				print("\033[31m", art.logo, "\033[0m")
				A = B
				B = random.choice(data)
				print(f"You're right! Current Score: {score}")
			else:
				should_continue = False
				clear()
				print("\033[31m", art.logo, "\033[0m")
				print(f"Sorry that's wrong. Final Score: {score}")
		else:
			clear()
			print("\033[31m", art.logo, "\033[0m")
			print(f"Sorry that's invalid choice! Game Over \nFinal Score: {score}")
			should_continue = False


def info():
	print("\033[31m", art.logo, "\033[0m")
	print(
	 "\n\nIt's easy to play. You will be shown two options. \nYou simply have to decide whether the second option has \nhigher followers on Instagram or lower than the first option. \n\nAs you progress, you will be shown a new option. Choose 'A' or 'B' to succeed. \n\nThe objective is to get the most right in a row. If you get one wrong, you lose the game.\n\n\nGood luck!"
	)
	input("\n\nPress enter key to continue ")
	clear()
	game()


info()