class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 10
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self, cost):
        """Returns the total calculated from coins inserted."""
        print(f"Please insert {self.CURRENCY}{cost}")
        for coin in self.COIN_VALUES:
            # self.money_received += input(f"How many {coin}?: ") * self.COIN_VALUES[coin]
            money_received_temp = input(f"How many {coin}?: ")

            if money_received_temp == '':
                money_received_temp = 0

            else:
                self.money_received += int(money_received_temp) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins(cost)
        if self.money_received == cost:
            self.profit += cost
            self.money_received = 0
            return True
        elif self.money_received > cost:
            change = round(self.money_received - cost, 2)
            self.profit += self.money_received
            self.profit -= change
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.money_received = 0
            return True

        elif self.money_received == 0:
            print("Sorry, no money received. Redirecting to drink choice page.")
            return False

        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
