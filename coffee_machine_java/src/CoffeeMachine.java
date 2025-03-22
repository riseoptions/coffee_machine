// src/CoffeeMachine.java
public class CoffeeMachine {
    private IngredientManager ingredients;

    public CoffeeMachine() {
        ingredients = new IngredientManager();
    }

    public void makeCoffee(String coffeeType) {
        Beverage coffee;
        switch (coffeeType.toLowerCase()) {
            case "espresso":
                coffee = new Espresso();
                break;
            case "latte":
                coffee = new Latte();
                break;
            default:
                System.out.println("Unknown coffee type.");
                return;
        }
        brewCoffee(coffee);
    }

    private void brewCoffee(Beverage coffee) {
        if (ingredients.hasIngredients(coffee)) {
            ingredients.useIngredients(coffee);
            System.out.println(coffee.getName() + " is ready!");
        } else {
            System.out.println("Not enough ingredients for " + coffee.getName() + ".");
        }
    }

    // Getter method to access the IngredientManager
    public IngredientManager getIngredients() {
        return ingredients;
    }
}
