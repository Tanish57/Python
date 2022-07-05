import os

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def clear():
    command = "clear"
    if os.name in ('nt', 'dos'):
        command = "cls"
    os.system(command)


def format_resources(resourcesleft, money):
    water = resourcesleft["water"]
    milk = resourcesleft["milk"]
    coffee = resourcesleft["coffee"]
    return f"Water : {water} \nMilk : {milk} \nCoffee : {coffee} \nMoney : ${money}"


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.5
    total += int(input("How many penny?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


is_on = True

while is_on:

    # TODO: 1. Prompt user by asking " What would you like? (espresso/latte/cappuccino): "
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the coffee machine by entering "off" to the prompt
    if choice == "off":
        print("Have a great day ahead! GoodBye!")
        is_on = False
        # os.system(exit())
    # TODO: 3. Print report when "report" is enterd in prompt in a proper format
    elif choice == "report":
        print(format_resources(resources, profit))
    # TODO: 4. Check if resources are sufficient for making the drink
    else:
        drink = MENU[choice]
        # TODO: 5. Process the coins
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            # TODO: 6. Check if transaction was successful?
            if is_transaction_successful(payment, drink["cost"]):
                # TODO: 7. Make Coffee
                make_coffee(choice, drink["ingredients"])
