import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.Random;

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

    @Test
    public void thereAreAsManySeatNumbersAsSeats() {
        assertEquals(plane.getType().getCapacity(), plane.getSeatNumbers().size());
    }

    @Test
    public void firstFewSeatNumbersAreAsExpectedFromSeed() {

        ArrayList<Integer> seatNumbers = plane.getSeatNumbers();

        int seed = 12; // Make sure to use the same seed value in tests
        Random random = new Random(seed);

        ArrayList<Integer> randomValues = new ArrayList<>();
        for (int i = 0; i < plane.getCapacity(); i++) {
            randomValues.add(
                random.nextInt(plane.type.getCapacity() + 1)
            );
        }

        for (int i = 0; i < plane.getCapacity(); i++){
            assertEquals(randomValues.get(i), seatNumbers.get(i));
        }
    }

    @Test
    public void currentSeatIndexRemainsZeroUnlessCustomerAdded() {
        assertEquals(0, plane.getCurrentSeatIndex());
    }
//
//    A Plane has:
//
//    an plane type (e.g. BOEING747) which stores capacity and total weight
}
