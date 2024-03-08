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
money = 0

is_on = True

# Check resources sufficient? 
def is_resource_sufficient(choice):
    for item in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Process coins.
def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total
    
# Check transaction successful?
def is_transaction_successful(money_received, cost):
    if money_received >= cost:
        change = round(money_received - cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
# Make Coffee.
def make_coffee(choice, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")

# Prompt user by asking “​What would you like? (espresso/latte/cappuccino):
while is_on: 
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Turn off the Coffee Machine by entering “​off​” to the prompt. 
    if choice == "off":
        is_on = False
    # Print report
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        resource = is_resource_sufficient(choice)
        if resource:
            # Process coins.
            transaction = process_coins()
            # Check transaction successful?
            if is_transaction_successful(transaction, MENU[choice]["cost"]):
                # Make Coffee.
                make_coffee(choice, MENU[choice]["ingredients"])

            