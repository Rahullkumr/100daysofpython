'''
You are going to write a program that will select
a random name from a list of names. 
The person selected will have to pay for everybody's food bill.


names_string.split(", ") splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
'''

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

size_of_names = len(names)
random_number = random.randint(0,size_of_names-1)

print(names[random_number] + " is going to buy the meal today!")