import json

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {}

        with open('resources.json', 'r') as data_file:
            data = json.load(data_file)
            self.resources = data['resources']

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def exit_machine(self):
        old_data = {}

        with open('resources.json', 'r') as data_file:
            old_data = json.load(data_file)
            print(old_data)
            old_data.update({"resources": self.resources})
            print(old_data)

        with open('resources.json', 'w') as data_file:
            json.dump(old_data, data_file, indent=4)
