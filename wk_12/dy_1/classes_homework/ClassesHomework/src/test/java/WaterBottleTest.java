import org.example.WaterBottle;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class WaterBottleTest {

    private WaterBottle waterBottle;
    @Before
    public void setUp() {
        waterBottle = new WaterBottle();
    }

    @Test
    public void initiallyHas100Volume() {
        assertEquals(100, waterBottle.getVolume());
    }

    @Test
    public void drinkingTwiceTakes20FromVolume(){
        assertEquals(100, waterBottle.getVolume());
        waterBottle.drink();
        waterBottle.drink();
        assertEquals(80, waterBottle.getVolume());
    }

    @Test
    public void emptyingWaterBottleReducesItsVolumneTo0(){
        assertEquals(100, waterBottle.getVolume());
        waterBottle.empty();
        assertEquals(0, waterBottle.getVolume());
    }

    @Test
    public void fillingWaterBottleBringsItsVolumeTo100(){
        assertEquals(100, waterBottle.getVolume());
        waterBottle.drink();
        waterBottle.drink();
        waterBottle.drink();
        assertEquals(70, waterBottle.getVolume());
        waterBottle.fill();
        assertEquals(100, waterBottle.getVolume());
    }
}


//    Water Bottle
//    Create a water bottle class with a volume property.
//        The volume should start at 100.
//        Add a drink function that takes 10 from the volume each time it is called.
//        Create an empty function that brings the volume down to 0.
//        Create a fill function that fills the volume back to 100.