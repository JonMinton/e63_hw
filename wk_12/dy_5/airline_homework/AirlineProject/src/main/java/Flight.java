import java.sql.Array;
import java.time.LocalDateTime;
import java.util.ArrayList;

public class Flight {

    private ArrayList<Pilot> pilots;
    private ArrayList<CabinCrewMember> crew;
    private ArrayList<Passenger> passengers;
    private Plane plane;
    private String flightNumber;
    private AirportLocation destination;
    private AirportLocation departure;
    private LocalDateTime departureTime;




    public Flight(ArrayList<Pilot> pilots, ArrayList<CabinCrewMember> crew, Plane plane, String flightNumber, AirportLocation departure, AirportLocation destination, LocalDateTime departureTime){
        this.pilots = pilots;
        this.crew = crew;
        this.plane = plane;
        this.flightNumber = flightNumber;
        this.departure = departure;
        this.destination = destination;
        this.departureTime = departureTime;
        this.passengers = new ArrayList<>();

    }

    public int getCapacity() {
        return this.plane.getCapacity();
    }



    public void addPassenger(Passenger passenger){

        this.passengers.add(passenger);
        passenger.addToFlight(this);
        ;
    }


    public Plane getPlane() {
        return this.plane;
    }

    public int getNumPassengers() {
        return this.passengers.size();
    }

    public ArrayList<Passenger> getPassengers() {
        return this.passengers;
    }

    public ArrayList<Pilot> getPilots() {
        return this.pilots;
    }

    public ArrayList<CabinCrewMember> getCrew() {
        return this.crew;
    }

    public AirportLocation getDestination() {
        return this.destination;
    }

    public AirportLocation getDeparture() {
        return this.departure;
    }

    public int getTotalBaggageWeight() {

        int totalNumBags = this.passengers
                .stream()
                .map(x -> x.getNumBags())
                .reduce(0, (sum, num) -> sum += num);
        return totalNumBags;

    }


    public int returnSeatsAvailable() {
        return this.getCapacity() - passengers.size();
    }

    public void broadcastMessage(String message){
        for (Passenger pass : this.passengers) {
            pass.receiveMessage(message);
        }
    }
}
