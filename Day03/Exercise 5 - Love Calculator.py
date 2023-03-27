'''
    A program that tests the compatibility between two people.

To work out the love score between two people:
    Take both people's names and check for the number of times the letters in the word TRUE occurs. 
    Then check for the number of times the letters in the word LOVE occurs. 
    Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
    "Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
    "Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
    "Your score is **z**."

e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"

T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
TotalTRUE = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
TotalLOVE = 3

Love Score = 53(i.e TotalTRUETotalLOVE)

'''

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Write your code below this line 👇
combined_string = name1 + name2
lowercase_string = combined_string.lower()

# check for the number of times the letters in the word TRUE occurs in both names. 
t = lowercase_string.count('t')
r = lowercase_string.count('r')
u = lowercase_string.count('u')
e = lowercase_string.count('e')
true = t + r + u + e

# check for the number of times the letters in the word LOVE occurs.
l = lowercase_string.count('l')
o = lowercase_string.count('o')
v = lowercase_string.count('v')
e = lowercase_string.count('e')
love = l + o + v + e

# combine true_count and love_count to form 2 digit number
truelove = str(true) + str(love)
love_score = int(truelove)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score < 50 and love_score > 40:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

