
from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
turn_off = False

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while not turn_off:
    request = input(f"What would you like? ({menu.get_items()}report): ")
    if request == "off":
        turn_off = True
        print("Machine is stopped")
        continue
    if request != "espresso" and request != "latte" and request != "cappuccino" and request != "report":
        print("Wrong request, please try again.")
        continue
    if request == "report":
        coffe_maker.report()
        money_machine.report()
        continue
    requested_coffee = menu.find_drink(request)
    is_sufficient = coffe_maker.is_resource_sufficient(requested_coffee)
    if not is_sufficient:
        print("Sorry the required resources to make this coffee is not enough.")
        continue
    coffe_maker.report()
    money_machine.report()
    is_payment = money_machine.make_payment(requested_coffee.cost)
    if not is_payment:
        continue

    coffe_maker.make_coffee(requested_coffee)














