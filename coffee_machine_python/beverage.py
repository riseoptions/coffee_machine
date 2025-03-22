# beverage.py
class Beverage:
    def __init__(self, name, water, beans, milk):
        self.name = name
        self.water = water
        self.beans = beans
        self.milk = milk

class Espresso(Beverage):
    def __init__(self):
        super().__init__('Espresso', 30, 20, 0)

class Latte(Beverage):
    def __init__(self):
        super().__init__('Latte', 200, 20, 150)
