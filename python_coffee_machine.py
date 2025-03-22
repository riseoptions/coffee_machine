class CoffeeMachine:
    def __init__(self):
        self.water = 1000  # ml
        self.beans = 500  # grams

    def make_coffee(self, coffee_type):
        if coffee_type == 'espresso':
            self.use_water(30)
            self.use_beans(20)
            print("Espresso is ready!")
        elif coffee_type == 'latte':
            self.use_water(200)
            self.use_beans(20)
            print("Latte is ready!")
        else:
            print("Unknown coffee type.")

    def use_water(self, amount):
        if self.water >= amount:
            self.water -= amount
        else:
            print("Not enough water.")

    def use_beans(self, amount):
        if self.beans >= amount:
            self.beans -= amount
        else:
            print("Not enough beans.")

machine = CoffeeMachine()
machine.make_coffee('espresso')
