// src/Main.java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        CoffeeMachine machine = new CoffeeMachine();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n--- Coffee Machine ---");
            System.out.println("1. Make Espresso");
            System.out.println("2. Make Latte");
            System.out.println("3. Refill Ingredients");
            System.out.println("4. Exit");

            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    machine.makeCoffee("espresso");
                    break;
                case "2":
                    machine.makeCoffee("latte");
                    break;
                case "3":
                    System.out.print("How much water to add (ml): ");
                    int water = Integer.parseInt(scanner.nextLine());
                    System.out.print("How much beans to add (grams): ");
                    int beans = Integer.parseInt(scanner.nextLine());
                    System.out.print("How much milk to add (ml): ");
                    int milk = Integer.parseInt(scanner.nextLine());
                    // Use the getIngredients() method to access IngredientManager
                    machine.getIngredients().refillIngredients(water, beans, milk);
                    break;
                case "4":
                    System.out.println("Shutting down the machine.");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
