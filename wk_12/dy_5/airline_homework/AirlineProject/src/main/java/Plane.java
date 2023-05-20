public class Plane {

    public PlaneTypes type;

    public Plane(PlaneTypes type){
        this.type = type;
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

}
