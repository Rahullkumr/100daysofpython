# Leap Year program
'''
a year divisible by 4 ==> leap year
Problem waise years me hoga jub unit aur tenth digit 
me 00 hoga, tub leap year will be = year divisible by all three
also

year not divisible by 100

'''

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
