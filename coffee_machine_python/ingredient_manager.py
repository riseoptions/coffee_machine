# ingredient_manager.py
class IngredientManager:
    def __init__(self):
        self.water = 1000  # ml
        self.beans = 500  # grams
        self.milk = 500  # ml

    def has_ingredients(self, coffee):
        return (self.water >= coffee.water and
                self.beans >= coffee.beans and
                self.milk >= coffee.milk)

    def use_ingredients(self, coffee):
        self.water -= coffee.water
        self.beans -= coffee.beans
        self.milk -= coffee.milk

    def refill_ingredients(self, water=0, beans=0, milk=0):
        self.water += water
        self.beans += beans
        self.milk += milk
