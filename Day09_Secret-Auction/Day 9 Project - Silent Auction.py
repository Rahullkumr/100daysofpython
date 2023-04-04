from replit import clear
from art import logo

print(logo)
print("Welcome to the Secret Auction Program.")

bid_record = {}


def calculate_highest():
	highest_bid = 0
	winner = ""
	for bidder in bid_record:
		if bid_record[bidder] > highest_bid:
			highest_bid = bid_record[bidder]
			winner = bidder
	print(f"\n\nThe winner is {winner} with a bid of RS {highest_bid}.\n\n")


should_continue = True
while should_continue:
	name = input("What is your name?: ")
	amount = int(input("What's your bid?: Rs"))

	bid_record[name] = amount #vvvvviiiiiiii

	choice = input("\nAre there any other bidders? Type 'yes' or 'no'\n")
	if choice == 'yes':
		clear()
	else:
		should_continue = False
		clear()
		calculate_highest()
