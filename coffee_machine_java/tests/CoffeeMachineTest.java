// tests/CoffeeMachineTest.java
import org.junit.Test;
import static org.junit.Assert.*;

public class CoffeeMachineTest {
    @Test
    public void testMakeEspresso() {
        CoffeeMachine machine = new CoffeeMachine();
        machine.makeCoffee("espresso");
        assertEquals(970, machine.ingredients.getWater());  // Kontrollime, kas vett on järele jäänud 970 ml
        assertEquals(480, machine.ingredients.getBeans());  // Kontrollime, kas ube on 480 g
    }

    @Test
    public void testMakeLatte() {
        CoffeeMachine machine = new CoffeeMachine();
        machine.makeCoffee("latte");
        assertEquals(800, machine.ingredients.getWater());
        assertEquals(480, machine.ingredients.getBeans());
        assertEquals(350, machine.ingredients.getMilk());
    }
}
