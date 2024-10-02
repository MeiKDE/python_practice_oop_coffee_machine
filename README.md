# Coffee Machine Simulator

This project is a coffee machine simulator written in Python. It allows a user to interact with the coffee machine, selecting from a menu of drinks, processing payments, and checking the machine's resources. The simulation runs until the user decides to turn the machine off.

## Features

- **Menu Selection**: Users can choose from a list of drinks.
- **Resource Management**: The coffee machine checks if there are enough ingredients available for the selected drink.
- **Payment System**: Users can insert money, and the machine will only make the drink if enough money is provided.
- **Report**: The machine can provide a report of the current resources and total money earned.

## How to Run

To run this program, simply execute the `coffee_machine.py` script (or the file where this code is written). Make sure you have the required classes (`CoffeeMaker`, `MenuItem`, `Menu`, and `MoneyMachine`) in separate modules:

1. **CoffeeMaker**: Manages the resources and checks if the machine has enough ingredients to make a drink.
2. **Menu**: Contains the available drinks and their information.
3. **MenuItem**: Represents each individual drink and its associated properties.
4. **MoneyMachine**: Handles the monetary transactions, ensuring the correct amount of money is received for each drink.

```python
from coffee_maker import CoffeeMaker
from menu import MenuItem, Menu
from money_machine import MoneyMachine

# Initialize objects
money_machine_obj = MoneyMachine()
coffee_maker_obj = CoffeeMaker()
menu_obj = Menu()

is_on = True

# Main loop
while is_on:
    options = menu_obj.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker_obj.report()
        money_machine_obj.report()
    else:
        drink = menu_obj.find_drink(choice)
        if coffee_maker_obj.is_resource_sufficient(drink) and money_machine_obj.make_payment(drink.cost):
            coffee_maker_obj.make_coffee(drink)
