from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import json

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    drink = input(f"What would you like? ({menu.get_items()}): ")

    if drink == "off":
        print("Shutting down...")
        break

    elif drink == "report":
        coffee_maker.report()
        money_machine.report()

    elif menu.find_drink(drink) is not None:
        if coffee_maker.is_resource_sufficient(menu.find_drink(drink)):
            if money_machine.make_payment(menu.find_drink(drink).cost):
                coffee_maker.make_coffee(menu.find_drink(drink))

    else:
        print("Invalid input. Try again.")
        continue

coffee_maker.exit_machine()

exit()
