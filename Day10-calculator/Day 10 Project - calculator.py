from replit import clear
from art import logo

print("\033[31m",logo,"\033[0m")

def add(num1, num2):
	return num1 + num2
def subtract(num1, num2):
	return num1 - num2
def multiply(num1, num2):
	return num1 * num2
def divide(num1, num2):
	return num1 / num2


operations = {
	"+" : add,
	"-" : subtract,
	"*" : multiply,
	"/" : divide,
}

def calculator():
	continue_it = True	
	num1 = float(input("What's the first number? "))
	for symbol in operations :
		print(symbol)
	
	while continue_it:
		operation_symbol = input("Pick an operation: ")
		num2 = float(input("What's the next number? "))	
		calculation_fn = operations[operation_symbol]
		answer = calculation_fn(num1,num2)	
		print(f"{num1} {operation_symbol} {num2} = {answer}")	
		if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: \n") == "y":
			num1 = answer
		else:
			continue_it = False
			clear()
			print("\033[31m")
			print(logo)
			print("\033[0m")
			calculator()

calculator()