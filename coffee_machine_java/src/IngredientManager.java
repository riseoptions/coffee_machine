// src/IngredientManager.java
public class IngredientManager {
    private int water;
    private int beans;
    private int milk;

    public IngredientManager() {
        this.water = 1000;  // 1000 ml vett
        this.beans = 500;   // 500 g ube
        this.milk = 500;    // 500 ml piima
    }

    public boolean hasIngredients(Beverage beverage) {
        return water >= beverage.getWater() && beans >= beverage.getBeans() && milk >= beverage.getMilk();
    }

    public void useIngredients(Beverage beverage) {
        water -= beverage.getWater();
        beans -= beverage.getBeans();
        milk -= beverage.getMilk();
    }

    public void refillIngredients(int water, int beans, int milk) {
        this.water += water;
        this.beans += beans;
        this.milk += milk;
    }
}
