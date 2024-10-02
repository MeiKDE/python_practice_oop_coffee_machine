from coffee_maker import CoffeeMaker
from menu import MenuItem, Menu
from money_machine import MoneyMachine

# Print report
money_machine_obj = MoneyMachine()
coffee_maker_obj = CoffeeMaker()
menu_obj = Menu()

is_on=True

# Check resources sufficient?
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
        # Process coins and check transaction successful?
        if coffee_maker_obj.is_resource_sufficient(drink) and money_machine_obj.make_payment(drink.cost):
            # Make coffee
            coffee_maker_obj.make_coffee(drink)

