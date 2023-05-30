public class Rock implements IThrowable {
    String name;
    String material;
    double weight;
    public Rock(String name, String material, double weight) {
        this.name = name;
        this.material = material;
        this.weight = weight;
    }

    public String throwItem() {
        return "I've thrown a rock of weight " + this.weight;
    }
}
