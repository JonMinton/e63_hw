import java.util.ArrayList;

public class FlightManager {


    private ArrayList<Integer> reservedWeightsNeeded;

    private Flight flight;
    public FlightManager(Flight flight){
        this.flight = flight;
        this.reservedWeightsNeeded = new ArrayList<>();
        for (Passenger passenger : this.flight.getPassengers()){
            this.reservedWeightsNeeded.add(passenger.getNumBags());
        }
    }

    public ArrayList<Integer> getReservedWeightPerPassenger() {
        return reservedWeightsNeeded;
    }

    public Integer getTotalBagWeight() {
        Integer totalBags = 0;
        for (Integer bagWeight : this.reservedWeightsNeeded){
            totalBags += bagWeight;
        }
        return totalBags;
    }

    public Integer getRemainingWeightAllowance() {
//        Need to know total allowance of plane
//        And number of passengers
//        And number of bags
//        Let's assume each passenger weights as much as three bags


        return (Integer) flight.getPlane().getCapacity() -
                3 * flight.getNumPassengers() -
                getTotalBagWeight();
    }

}
