import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ingredient_manager import IngredientManager  # Import the IngredientManager class


# tests/test_ingredient_manager.py
import unittest
from ingredient_manager import IngredientManager
from beverage import Espresso

class TestIngredientManager(unittest.TestCase):
    def test_has_ingredients(self):
        manager = IngredientManager()
        espresso = Espresso()
        self.assertTrue(manager.has_ingredients(espresso))

    def test_use_ingredients(self):
        manager = IngredientManager()
        espresso = Espresso()
        manager.use_ingredients(espresso)
        self.assertEqual(manager.water, 970)
        self.assertEqual(manager.beans, 480)

if __name__ == '__main__':
    unittest.main()
