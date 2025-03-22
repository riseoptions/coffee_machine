import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from coffee_machine import CoffeeMachine  # Import the CoffeeMachine class


# tests/test_coffee_machine.py
import unittest
from coffee_machine import CoffeeMachine

class TestCoffeeMachine(unittest.TestCase):
    def test_make_espresso(self):
        machine = CoffeeMachine()
        machine.make_coffee('espresso')
        self.assertEqual(machine.ingredients.water, 970)
        self.assertEqual(machine.ingredients.beans, 480)

    def test_make_latte(self):
        machine = CoffeeMachine()
        machine.make_coffee('latte')
        self.assertEqual(machine.ingredients.water, 800)
        self.assertEqual(machine.ingredients.beans, 480)
        self.assertEqual(machine.ingredients.milk, 350)

if __name__ == '__main__':
    unittest.main()
