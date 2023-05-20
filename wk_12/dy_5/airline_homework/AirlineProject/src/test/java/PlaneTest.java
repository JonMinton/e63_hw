import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PlaneTest {

    Plane plane;

    @Before
    public void setUp() {
        plane = new Plane(PlaneTypes.BOEING_737);
    }

    @Test
    public void planeHasType() {
        assertEquals(PlaneTypes.BOEING_737, plane.getType());
    }

    @Test
    public void planeHasCapacity() {
        assertEquals(189, plane.getCapacity());
    }

    @Test
    public void planeHasWeight() {
        assertEquals(79015, plane.getWeight());
    }
//
//    A Plane has:
//
//    an plane type (e.g. BOEING747) which stores capacity and total weight
}
