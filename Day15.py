# Coffee Machine Project

# Define the menu with ingredients and cost for each coffee type
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

# Define the initial resources available in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

print("\nWelcome to the Coffee Machine!")
is_active = True

# Function to check if there are enough resources to make the selected coffee
def check_resources(order):
    for item in order:
        if resources[item] < order[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# Function to process the coins inserted by the user
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies

# Function to check if the transaction is successful
def check_transaction(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

# Function to make the coffee and deduct the resources used
def make_coffee(order):
    for item in order:
        resources[item] -= order[item]
    print("Here is your coffee. Enjoy!")

# Main loop to keep the coffee machine running
while is_active:
    choice = input("Here are the available options: espresso, latte, cappuccino. Choose One: \n").lower()

    if choice == 'off':
        print("The coffee machine is shutting down.")
        is_active = False
    elif choice == 'report':
        # Print the current resources available in the coffee machine
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")
    elif choice in MENU:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if check_transaction(payment, drink['cost']):
                resources['money'] += drink['cost']
                make_coffee(drink['ingredients'])
    else:
        print("Invalid choice. Please try again.")
