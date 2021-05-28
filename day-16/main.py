from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    user_order = input(f"What yould you like? ({menu.get_items()[:-1]}): ").lower()
    if user_order == "off":
        break
    if user_order == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    drink = menu.find_drink(user_order)
    if drink != None:
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)
