public class CoffeeMachine {
    private int water = 1000; // ml
    private int beans = 500;  // grams

    public void makeCoffee(String coffeeType) {
        if (coffeeType.equals("espresso")) {
            useWater(30);
            useBeans(20);
            System.out.println("Espresso is ready!");
        } else if (coffeeType.equals("latte")) {
            useWater(200);
            useBeans(20);
            System.out.println("Latte is ready!");
        } else {
            System.out.println("Unknown coffee type.");
        }
    }

    private void useWater(int amount) {
        if (water >= amount) {
            water -= amount;
        } else {
            System.out.println("Not enough water.");
        }
    }

    private void useBeans(int amount) {
        if (beans >= amount) {
            beans -= amount;
        } else {
            System.out.println("Not enough beans.");
        }
    }
    
    public static void main(String[] args) {
        CoffeeMachine machine = new CoffeeMachine();
        machine.makeCoffee("espresso");
    }
}
