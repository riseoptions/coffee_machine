// tests/IngredientManagerTest.java
import org.junit.Test;
import static org.junit.Assert.*;

public class IngredientManagerTest {
    @Test
    public void testHasIngredients() {
        IngredientManager manager = new IngredientManager();
        Beverage espresso = new Espresso();
        assertTrue(manager.hasIngredients(espresso));
    }

    @Test
    public void testUseIngredients() {
        IngredientManager manager = new IngredientManager();
        Beverage espresso = new Espresso();
        manager.useIngredients(espresso);
        assertEquals(970, manager.getWater());
        assertEquals(480, manager.getBeans());
    }
}
