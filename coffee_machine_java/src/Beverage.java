// src/Beverage.java
public abstract class Beverage {
    protected String name;
    protected int water;
    protected int beans;
    protected int milk;

    public Beverage(String name, int water, int beans, int milk) {
        this.name = name;
        this.water = water;
        this.beans = beans;
        this.milk = milk;
    }

    public String getName() {
        return name;
    }

    public int getWater() {
        return water;
    }

    public int getBeans() {
        return beans;
    }

    public int getMilk() {
        return milk;
    }
}
