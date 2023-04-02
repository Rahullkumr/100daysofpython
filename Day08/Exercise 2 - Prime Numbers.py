#You need to write a function that checks whether if the number passed into it is a prime number or not.

#Write your code below this line 👇
def prime_checker(number):
    isPrime = True
    if number < 1:
        print("Enter positive number greater than 1")
    if (number == 1) or (number == 2):
        print("It's a prime number.")
    else:
        for i in range(2,number):
            if number % i == 0:
                isPrime = False
        if isPrime == True:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
            

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
