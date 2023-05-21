import java.util.ArrayList;

public class Passenger extends Person{

    private int numBags;
    private ArrayList<String> messages;
    private Flight flight;
    private int seatCode;

    public Passenger(String name, int numBags){
        super(name);
        this.numBags = numBags;
        this.messages = new ArrayList<>();
        this.flight = null;
    }

    public int getNumBags() {
        return this.numBags;
    }

    public void receiveMessage(String message){
        this.messages.add(message);
    }

    public int getNumMessages(){
        return this.messages.size();
    }

    public void addToFlight(Flight flight){
        this.flight = flight;
        this.seatCode = flight.getPlane().assignSeatNumber();
    }

    public Flight getPassengerFlight() {
        return this.flight;
    }

    public int getSeatCode() {
        return this.seatCode;
    }
}
