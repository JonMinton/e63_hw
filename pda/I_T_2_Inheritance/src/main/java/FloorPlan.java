public class FloorPlan {

    private double length;
    private double width;

    public FloorPlan(double length, double width){
        this.length = length;
        this.width = width;
    }

    public double getArea() {
        return length * width;
    }
}
