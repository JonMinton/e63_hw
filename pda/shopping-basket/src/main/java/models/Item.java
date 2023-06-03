package models;

public class Item {

    private String name;

    private double price;

    private boolean bogof;

    public Item(String name, double price, boolean bogof) {
        this.name = name;
        this.price = price;
        this.bogof = bogof;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public boolean isBogof() {
        return bogof;
    }

    public void setBogof(boolean bogof) {
        this.bogof = bogof;
    }
}
