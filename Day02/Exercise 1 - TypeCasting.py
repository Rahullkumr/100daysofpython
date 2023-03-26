'''
Write a program that adds the digits in a 2 digit number. 
e.g. if the input was 35, then the output should be 3 + 5 = 8

'''

two_digit_number = input("Type a two digit number: ")

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

print(first_digit+second_digit)