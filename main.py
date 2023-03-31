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

bank = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_enough_resource(ingredients_list):
    """Check if there are enough resources to make the drink and return True or False."""
    for item in ingredients_list:
        if ingredients_list[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Return the total money from coins"""
    print("Insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(payment, drink_cost ):
    """Check if the user has enough money to buy a drink"""

    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is your ${change} dollars in change.")
        global bank
        bank += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the ingredients resources when a drink is made"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your coffe ☕ {drink_name}")


is_machine_on = True
while is_machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_machine_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Bank: ${bank}")
    else:
        drink_cost = MENU[order]
        if is_enough_resource(drink_cost["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink_cost['cost']):
                make_coffee(order, drink_cost['ingredients'])
