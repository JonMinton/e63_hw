import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.Assert.assertEquals;

public class FlightManagerTest {

    Flight flight;
    FlightManager flightManager;

    @Before
    public void setUp() {
        Passenger pass1 = new Passenger("Bob", 5);
        Passenger pass2 = new Passenger("Alice", 6);
        Plane plane = new Plane(PlaneTypes.ATR_72);

        flight = new Flight(null, null, plane, "", null, null, null);
        flight.addPassenger(pass1);
        flight.addPassenger(pass2);

        flightManager = new FlightManager(flight);
    }
    @Test
    public void canCalculateBaggagePerPassenger() {
        ArrayList<Integer> bags = flightManager.getReservedWeightPerPassenger();
        assertEquals(
          new ArrayList<>(Arrays.asList(5, 6)), bags
        );
    }

    @Test
    public void canCalculateTotalBagWeight() {
        assertEquals(new Integer(11), flightManager.getTotalBagWeight());
    }

    @Test
    public void canCalculateRemainingWeightAllowance() {
        Integer remainingWeightAllowance = flightManager.getRemainingWeightAllowance();
        assertEquals(new Integer(61), remainingWeightAllowance);

    }

}
