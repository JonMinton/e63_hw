public class Room extends FloorPlan{

    private double length;
    private double width;
    private double height;

    public Room(double length, double width, double height){
        super(length, width);
        this.height = height;
    }

    public double getVolume(){
        return getArea() * height;
    }

}
