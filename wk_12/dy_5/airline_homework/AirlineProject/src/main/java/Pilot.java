import java.util.ArrayList;

public class Pilot extends Person{

    private CrewRanks rank;
    private String licenceNumber;

    public Pilot(String name, CrewRanks rank, String licenceNumber){
        super(name);
        this.rank = rank;
        this.licenceNumber = licenceNumber;
    }

    public String getLicenceNumber() {
        return this.licenceNumber;
    }

    public CrewRanks getRank() {
        return this.rank;
    }

    public String flyPlane(Flight flight){
        ArrayList<Pilot> pilots = flight.getPilots();
        String message = null;
        if (pilots.contains(this)){
            message = "I'm a pilot on plane " + flight.getPlane().getType().name() +
            " so I guess I'll fly it from " + flight.getDeparture() +
            " to " + flight.getDestination();
        } else {
            message = "I'm not a pilot on this plane so can't fly it";
        }
        return message;
    }
}
