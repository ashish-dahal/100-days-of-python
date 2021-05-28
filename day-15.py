# Coffee dispenser program

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0.0}
MENU = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "money": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "money": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "money": 3.0},
}

# Print the dispenser resources report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${abs(resources['money']):.2f}")


# Check if the dispenser has enough resources to serve the order
def is_resources_sufficient(order):
    """Returns True when order can be made, False if ingredients are insufficient."""
    check = [
        True if MENU[order][key] <= resources[key] else False
        for key, value in MENU[order].items()
    ]
    return not False in check[:-1]


# Converts the user supplied coin value to dollars
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# Checks if the user supplied enough coins for the purchase
def is_transaction_successful(user_total, user_order):
    change = user_total - MENU[user_order]["money"]
    if change >= 0:
        if change != 0:
            print(f"Here is ${change:.2f} in change.")
        return True
    return False


# Deduct ingredients from the resources to make a coffee
def make_coffee(order):
    global resources, MENU
    for item in resources:
        resources[item] -= MENU[order][item]


# Start the coffee dispenser
def start_machine():
    while True:
        user_order = input("What yould you like? (espresso/latte/cappuccino): ").lower()
        if user_order == "off":
            break
        if user_order == "report":
            print_report()
        elif is_resources_sufficient(user_order):
            if is_transaction_successful(process_coins(), user_order):
                make_coffee(user_order)
                print(f"Here is your {user_order}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry not enough resources.")


if __name__ == "__main__":
    start_machine()
