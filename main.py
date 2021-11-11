from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()




is_on = True

while is_on:
    option = menu.get_items()
    user_command = input(f"What would you like? {option}:")
    if user_command == "off":
        is_on = False
    elif user_command == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_command)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)












