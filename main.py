import art
import time
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "money": 0,
}
next_customer = True
def resource_reporter(water_ml,milk_ml,coffee_g,money):
    print(f"Water: {water_ml}ml")
    print(f"Milk: {milk_ml}ml")
    print(f"Coffee: {coffee_g}g")
    print(f"Money: ${money}")

def resource_checker(coffee_request):
    global MENU,resources
    required_resources = MENU[coffee_request]['ingredients']
    insufficient_resources = []
    insufficient_resources.extend(key for key in required_resources if required_resources[key] > resources[key])
    if len(insufficient_resources) > 0:
        text = "".join((i + ", " if i != insufficient_resources[-1] else "and " + i) for i in insufficient_resources)
        print("Sorry there is not enough " + text + ".")
        return False
    return True

def checkout_processor(coffee_request,quarter_number,dime_number,nickle_number,penny_number):
    global MENU,resources
    coffee_cost = MENU[coffee_request]['cost']
    total_payment = .25 * quarter_number + .1 * dime_number + .05 * nickle_number + .01 * penny_number
    if total_payment > coffee_cost:
        refund_amount = total_payment-coffee_cost
        resources['money'] += coffee_cost
        print(f"Here is ${refund_amount:.2f} dollars in change.")
        return True
    else:
        print("Sorry, the payment is not enough. Money refunded.")
        return False

def make_coffee(coffee_request):
    global MENU,resources
    required_resources = MENU[coffee_request]['ingredients']
    for i in required_resources:
        resources[i] -= required_resources[i]
    print(f"Here is your {coffee_request}. Enjoy!")


while True:
    if next_customer:
        print(art.logo)
        next_customer = False
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if request == "off":
        break
    if request != "espresso" and request != "latte" and request != "cappuccino" and request != "report":
        print("Wrong request, please try again!")
        continue

    water_amount,milk_amount,coffee_amount,money_amount = resources.values()
    if request == "report":
        resource_reporter(water_amount,milk_amount,coffee_amount,money_amount)
        continue

    sufficient = resource_checker(request)
    if not sufficient:
        continue
    else:
        print("Please insert coins.")
        quarters = input("How many quarters?: ")
        if quarters == "off":
            break
        dimes = input("How many dimes?: ")
        if dimes == "off":
            break
        nickles = input("How many nickles?: ")
        if nickles == "off":
            break
        pennies = input("How many pennies?: ")
        if nickles == "off":
            break
        payment_successful = checkout_processor(request,int(quarters),int(dimes),int(nickles),int(pennies))
        if not payment_successful:
            continue
        else:
            make_coffee(request)
            time.sleep(3)
            next_customer = True










