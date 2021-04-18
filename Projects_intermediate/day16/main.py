from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_list = Menu()
money = MoneyMachine()
final_coffee = CoffeeMaker()
while True:

    user_choice = input(f"What would you like? {coffee_list.get_items()}: ")

    if user_choice == "report":
        final_coffee.report()
        money.report()
    elif user_choice == "off":
        break
    else:
        exact_coffee = coffee_list.find_drink(user_choice)
        if final_coffee.is_resource_sufficient(exact_coffee) and money.make_payment(exact_coffee.cost) :
            final_coffee.make_coffee(exact_coffee)


