from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# my_screen.exitonclick()

# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

#Excercise

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_Maker = CoffeeMaker()
money_Machine = MoneyMachine()
menu = Menu()

in_service = True

while in_service:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        print("Turning off the machine")
        in_service = False
    elif choice == "report":
        coffee_Maker.report()
        money_Machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_Maker.is_resource_sufficient(drink) and money_Machine.make_payment(drink.cost):
            coffee_Maker.make_coffee(drink)