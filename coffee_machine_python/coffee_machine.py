# coffee_machine.py
from ingredient_manager import IngredientManager
from beverage import Espresso, Latte

class CoffeeMachine:
    def __init__(self):
        self.ingredients = IngredientManager()

    def make_coffee(self, coffee_type):
        if coffee_type == 'espresso':
            coffee = Espresso()
        elif coffee_type == 'latte':
            coffee = Latte()
        else:
            print("Unknown coffee type.")
            return
        self.brew_coffee(coffee)

    def brew_coffee(self, coffee):
        if self.ingredients.has_ingredients(coffee):
            self.ingredients.use_ingredients(coffee)
            print(f"{coffee.name} is ready!")
        else:
            print(f"Not enough ingredients for {coffee.name}.")

