from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

cofee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_on:
    options = menu.get_items()
    choice = input(f"What Would You Like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        cofee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingridents = cofee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_payment_successful and is_enough_ingridents:
            cofee_maker.make_coffee(drink)
