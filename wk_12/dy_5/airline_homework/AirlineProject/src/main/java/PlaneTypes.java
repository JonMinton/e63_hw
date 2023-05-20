public enum PlaneTypes {
    AIRBUS_A321(93500, 220),
    BOEING_737(79015, 189),
    EMBRAER_E190(50800, 114),
    BOMBARDIER_CRJ700(38912, 70),
    ATR_72(22900, 78);

    private int weight;
    private int capacity;

    PlaneTypes(int weight, int capacity) {
        this.weight = weight;
        this.capacity = capacity;
    }

    public int getWeight() {
        return weight;
    }

    public int getCapacity() {
        return capacity;
    }


}
