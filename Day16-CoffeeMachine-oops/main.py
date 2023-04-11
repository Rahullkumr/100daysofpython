from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()      # objects are declared in small letters and class have capital letters
coffee_maker = CoffeeMaker()        # objects are declared in small letters and class have capital letters
menu = Menu()                       # objects are declared in small letters and class have capital letters
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"\nWhat would you like?: {options}")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
