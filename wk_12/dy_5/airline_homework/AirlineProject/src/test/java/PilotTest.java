import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PilotTest {

    Pilot pilot;
    @Before
    public void setUp() {
        pilot = new Pilot("Hankson", CrewRanks.CAPTAIN, "T0M001");

    }

    @Test
    public void pilotHasName() {
        assertEquals("Hankson", pilot.getName());
    }

    @Test
    public void pilotHasRank() {
        assertEquals(CrewRanks.CAPTAIN, pilot.getRank());
    }

    @Test
    public void pilotHasLicence() {
        assertEquals("TOM001", pilot.getLicenceNumber());
    }



//    A Pilot should be able to:
//
//    fly the plane (a simple method which returns a String is sufficient)

//    A Pilot has:
//
//    a name
//    a rank
//    a pilot licence number (you can use a String for this)

}
