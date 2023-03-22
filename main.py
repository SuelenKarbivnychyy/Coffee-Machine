# Check if there are enough resources to make the coffee.
# if it does not display : Sorry there is not enough {the resource's name}.
# if it does ask for coins:

# how many quarters
# how many dimes?
# how many nickles?
# how many pennies?

# Check if the money user inserted is enough for the coffee:
# if it does:
# make the coffee and make sure to update the resources values, and add the money to the bank
# else:
# display: Sorry that's not enough money. Money refunded.


# calculate the total coin the user enters, subtract the coffee price and display back the change.

# make the program ask what coffee you want over and over again always updating the resources


# TODO 1. print the report (report is all the resources that has available to make a coffee and the total money on the
#  bank
# TODO 2. The program starts by asking which coffee the user wants (espresso/latte/cappuccino)
# TODO 3. check resources sufficient
# TODO 4. process coins
# TODO 5. check transaction successful
# TODO 6. make coffee.

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

order = input("What would you like? (Espresso/Latte/Cappuccino):").lower()


def is_resource_enough(coffee_order):
    """Check if it has enough resources to make a coffee and return True or false."""
    # maybe make these resources a dictionary?
    water = 0
    milk = 0
    coffee = 0

    if coffee_order == 'espresso':
        water = MENU["espresso"]["water"]
        coffee = MENU["espresso"]["coffee"]
    elif coffee_order == 'latte':
        water = MENU["latte"]["water"]
        milk = MENU["latte"]["milk"]
        coffee = MENU["latte"]["coffee"]
    else:
        water = MENU["cappuccino"]["water"]
        milk = MENU["cappuccino"]["milk"]
        coffee = MENU["cappuccino"]["coffee"]


def display_report():
    """Display the resources available."""

    print(resources)


def ask_for_coins():
    """Function to return the total money from coins."""

    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }

    total_coins_value = coins["quarters"] * quarters + coins["dimes"] * dimes \
                        + coins["nickles"] * nickles + coins["pennies"] * pennies

    return f"${total_coins_value}"


print(ask_for_coins())

# def selected_coffee():
#     """Return the coffee the user will select."""
#
#     select_a_coffee_type = input("What would you like? (espresso/latte/cappuccino):")
#     return select_a_coffee_type
