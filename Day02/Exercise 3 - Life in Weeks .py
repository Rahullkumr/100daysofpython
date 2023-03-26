"""
Create a program using maths and f-Strings that tells us 
how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a 
message with our time left in this format:

You have x days, y weeks, and z months left.
"""
age = input("What is your current age? ")

remYears = 90 - int(age)
rMonths = remYears * 12
rWeeks = remYears * 52
rDays = remYears * 365

print(f"You have {rDays} days, {rWeeks} weeks, and {rMonths} months left.")