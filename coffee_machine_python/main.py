# main.py
from coffee_machine import CoffeeMachine

def main():
    machine = CoffeeMachine()
    while True:
        print("\n--- Coffee Machine ---")
        print("1. Make Espresso")
        print("2. Make Latte")
        print("3. Refill Ingredients")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            machine.make_coffee('espresso')
        elif choice == '2':
            machine.make_coffee('latte')
        elif choice == '3':
            water = int(input("How much water to add (ml): "))
            beans = int(input("How much beans to add (grams): "))
            milk = int(input("How much milk to add (ml): "))
            machine.ingredients.refill_ingredients(water, beans, milk)
        elif choice == '4':
            print("Shutting down the machine.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
