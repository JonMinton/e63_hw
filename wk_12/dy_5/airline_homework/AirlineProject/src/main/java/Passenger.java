import java.util.ArrayList;

public class Passenger extends Person{

    private int numBags;
    private ArrayList<String> messages;

    public Passenger(String name, int numBags){
        super(name);
        this.numBags = numBags;
        this.messages = new ArrayList<>();
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
}
