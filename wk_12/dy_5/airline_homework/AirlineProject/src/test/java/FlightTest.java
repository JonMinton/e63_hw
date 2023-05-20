import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class FlightTest {

    Flight flight;
    Pilot pilot1;

    CabinCrewMember crew3;

    Passenger pass1;

    @Before
    public void setUp() {

        pilot1 = new Pilot("AA", CrewRanks.CAPTAIN, "AA11");
        Pilot pilot2 = new Pilot("AB", CrewRanks.CAPTAIN, "AB11");
        ArrayList<Pilot> pilots = new ArrayList<>();
        pilots.add(pilot1);
        pilots.add(pilot2);


        CabinCrewMember crew1 = new CabinCrewMember("AAA", CrewRanks.FIRST_OFFICER);
        CabinCrewMember crew2 = new CabinCrewMember("AAB", CrewRanks.FLIGHT_ATTENDANT);
        crew3 = new CabinCrewMember("AAC", CrewRanks.PURSER);
        ArrayList<CabinCrewMember> crew = new ArrayList<>();
        crew.add(crew1);
        crew.add(crew2);
        crew.add(crew3);

        Plane plane = new Plane(PlaneTypes.ATR_72);

        flight = new Flight(pilots, crew, plane, "Blah001", AirportLocation.EDI, AirportLocation.DUB, "2018-04-20");

    }

    @Test
    public void canReturnNumberOfSeats() {
        assertEquals(PlaneTypes.ATR_72.getCapacity(), flight.returnSeatsAvailable());
    }

    @Test
    public void canBookPassengers() {
        pass1 = new Passenger("LL", 10);
        Passenger pass2 = new Passenger("JJ", 5);

        flight.addPassenger(pass1);
        flight.addPassenger(pass2);

        assertEquals(PlaneTypes.ATR_72.getCapacity() - 2, flight.returnSeatsAvailable());

    }

    @Test
    public void pilotCanFlyPlaneOnFlight() {
        String message = pilot1.flyPlane(flight);
        System.out.println(message);
        assertEquals("I'm a pilot on plane ATR_72 so I guess I'll fly it from EDI to DUB", message);
    }

    @Test
    public void pilotCannotFlyPlaneTheyAreNotOn() {
        Pilot pilot3 = new Pilot("Jojo", CrewRanks.CAPTAIN, "MON53");

        assertEquals("I'm not a pilot on this plane so can't fly it", pilot3.flyPlane(flight));
    }


    @Test
    public void crewMemberOnFlightCanSendMessagesToPassengers() {
        pass1 = new Passenger("LL", 10);
        assertEquals(0, pass1.getNumMessages());
        flight.addPassenger(pass1);
        crew3.sendMessage("Hold onto your purses as I'm a purser", flight);
        assertEquals(1, pass1.getNumMessages());

    }

    @Test
    public void passengerDoesNotReceiveMessageIfNotOnFlight() {
        pass1 = new Passenger("LL", 10);
        assertEquals(0, pass1.getNumMessages());
        crew3.sendMessage("Hold onto your purses as I'm a purser", flight);
        assertEquals(0, pass1.getNumMessages());

    }



}
