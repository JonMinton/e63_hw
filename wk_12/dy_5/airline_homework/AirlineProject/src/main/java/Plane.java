import java.lang.reflect.Array;
import java.util.ArrayList;

import java.util.Random;

public class Plane {

    public PlaneTypes type;
    public ArrayList<Integer> seatNumbers;
    public int currentSeatIndex;

    public Plane(PlaneTypes type){
        this.type = type;
        this.seatNumbers = new ArrayList<Integer>();
        this.currentSeatIndex = 0;

        int seed = 12; // Make sure to use the same seed value in tests
        Random random = new Random(seed);

        for (int i = 0; i < getCapacity(); i++) {
            seatNumbers.add(random.nextInt(getCapacity() + 1));
        }


    }

    public PlaneTypes getType() {
        return this.type;
    }

    public int getCapacity() {
        return this.type.getCapacity();
    }

    public int getWeight() {
        return this.type.getWeight();
    }

    public int assignSeatNumber() {
        int out = this.seatNumbers.get(this.currentSeatIndex);
        this.currentSeatIndex++;
        return out;
    }

    public ArrayList<Integer> getSeatNumbers() {
        return this.seatNumbers;
    }

    public int getCurrentSeatIndex() {
        return this.currentSeatIndex;
    }
}
