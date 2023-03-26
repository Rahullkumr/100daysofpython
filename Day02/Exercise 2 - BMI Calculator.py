'''
Write a program that calculates the Body Mass Index 
(BMI) from a user's weight and height.

The BMI is a measure of someone's weight taking into account their height.
e.g. If a tall person and a short 
person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's WEIGHT (in kg) by the SQUARE of their HEIGHT (in m)
Warning ==>	you should convert the result to a whole number
'''

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / (float(height) ** 2)
result = int(bmi)

print(result)