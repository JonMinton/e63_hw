public class GiftCard implements IChargeable {

    private double balance;

    public GiftCard(double balance) {
        this.balance =  balance;
    }


    public void charge(double amount) {
        if (amount <= getBalance()) {
            this.balance -= amount;
        }
    }

    public double getBalance() {
        return this.balance;
    }

}
