public class CabinCrewMember extends Person{

    private CrewRanks rank;

    public CabinCrewMember(String name, CrewRanks rank){
        super(name);
        this.rank = rank;
    }

    public CrewRanks getRank() {
        return this.rank;
    }

    public void sendMessage(String message, Flight flight) {
        if (flight != null && flight.getCrew().contains(this)) {
            flight.broadcastMessage(message);
        }
    }
}
