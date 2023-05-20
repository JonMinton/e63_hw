import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CabinCrewMemberTest {

    CabinCrewMember crew;

    @Before
    public void setUp() {
        crew = new CabinCrewMember("Delia", CrewRanks.PURSER);
    }

    @Test
    public void crewHasName() {
        assertEquals("Delia", crew.getName());
    }

    @Test
    public void crewHasRank() {
        assertEquals(CrewRanks.PURSER, crew.getRank());
    }
}
//    A CabinCrewMember has:
//
//    a name
//    a rank (e.g Captain/First Officer/Purser, Flight Attendant)
//}
