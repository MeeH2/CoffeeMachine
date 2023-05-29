from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    coffee_choice = input(f"What would you like? {options}").lower()
    if coffee_choice == "off":
        is_on = False
    elif coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)