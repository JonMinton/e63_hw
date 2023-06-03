package models;

public class Customer {

    private String name;

    private boolean hasLoyaltyCard;

    public Customer(String name, boolean hasLoyaltyCard) {
        this.name = name;
        this.hasLoyaltyCard = hasLoyaltyCard;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public boolean isHasLoyaltyCard() {
        return hasLoyaltyCard;
    }

    public void setHasLoyaltyCard(boolean hasLoyaltyCard) {
        this.hasLoyaltyCard = hasLoyaltyCard;
    }
}
