public class Brick implements IThrowable{
    private int weight;
    private String colour;
    public Brick(int weight, String colour){
        this.weight = weight;
        this.colour = colour;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public String getColour() {
        return colour;
    }

    public void setColour(String colour) {
        this.colour = colour;
    }

    public String throwItem() {
        return "I've thrown a " + this.colour + " brick of weight " + this.weight;
    }
}
