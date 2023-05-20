import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PassengerTest {

    Passenger pass1;
    Passenger pass2;
    Passenger pass3;
    @Before
    public void setUp() {
        pass1 = new Passenger("Anne", 3);
        pass2 = new Passenger("Brenda", 5);
        pass3 = new Passenger("Charlie", 2);
    }

    @Test
    public void passengerHasName() {
        assertEquals("Anne", pass1.getName());
    }

    @Test
    public void passengerHasBags() {
        assertEquals(2, pass3.getNumBags());
    }

    @Test
    public void passengerCanReceiveMessages() {
        assertEquals(0, pass1.getNumMessages());
        pass1.receiveMessage("It's 9.13AM so let's have a drink...");
        assertEquals(1, pass1.getNumMessages());



    }
//    A Passenger has:
//
//    a name
//    a number of bags
}
