#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

bill = input("What was the total bill? ")
percent = input("What percent tip would you like to give? 10, 12, or 15? ")

totalPeople = input("How many people to split the bill? ")

percentValue = float(bill) * int(percent) / 100
payEachOne = (float(bill) + percentValue) / int(totalPeople)

print(f"\nEach person should pay: {round(payEachOne,2)}")