import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class BagTest {

    Brick brick1;
    Brick brick2 ;
    Rock rock1;
    Rock rock2;
    Bag bag;

    @Before
    public void setUp() {
        brick1 = new Brick(4, "red");
        brick2 = new Brick(3, "grey");
        rock1 = new Rock("The", "dry", 3.2);
        rock2 = new Rock("Boldy", "granite", 5.3);
        bag = new Bag("Little Bag");
    }

    @Test
    public void canPutThrowablesInBagsAndThrow() {
        assertEquals(0, bag.getThrowables().size());
        bag.addThrowable(brick1);
        bag.addThrowable(rock1);
        bag.addThrowable(rock2);
        assertEquals(3, bag.getThrowables().size());
    }

    @Test
    public void brickIsThrowable() {
        assertTrue(brick1 instanceof IThrowable);
    }

    @Test
    public void rockIsThrowable() {
        assertTrue(rock1 instanceof IThrowable);
    }

    @Test
    public void rockHasCorrectThrowMethod() {
        assertEquals("I've thrown a rock of weight 3.2", rock1.throwItem());
    }

    @Test
    public void brickHasCorrectThrowMethod() {
        assertEquals("I've thrown a red brick of weight 4", brick1.throwItem());
    }

    @Test
    public void canAddBothTypesToBag() {
        assertEquals(0, bag.getThrowables().size());
        bag.addThrowable(rock1);
        bag.addThrowable(brick1);
        assertEquals(2, bag.getThrowables().size());


    }


}
