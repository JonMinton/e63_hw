import java.util.ArrayList;
import java.util.Date;

public class CreditCard extends PaymentCard implements IChargeable{

    private ArrayList<Double> transactions;
    private double percentageRate;
    private double creditLimit;


    public CreditCard(double balance, int cardNumber, Date expiryDate, int securityNumber, double percentageRate, double creditLimit){
        super(balance, cardNumber, expiryDate, securityNumber);
        this.creditLimit = creditLimit;
        this.percentageRate = percentageRate;
        this.transactions = new ArrayList<>();
    }

    public void charge(double purchaseAmount){
        if (purchaseAmount * (1 + percentageRate) <= getBalance()){
            transactions.add(purchaseAmount * (1 + percentageRate));
            super.reduceBalance(purchaseAmount * (1 + percentageRate));
        }
    }

    public double getBalance() {
        return super.getBalance();
    }

}