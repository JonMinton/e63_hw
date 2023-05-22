import java.util.ArrayList;
import java.util.Date;

public class DebitCard extends PaymentCard implements IChargeable {

    private ArrayList<Double> transactions;
    private int sortCode;

    public DebitCard(double balance, int cardNumber, Date expiryDate, int securityNumber, int sortCode){
        super(balance, cardNumber, expiryDate, securityNumber);
        this.transactions = new ArrayList<>();
        this.sortCode = sortCode;
    }

    public void charge(double purchaseAmount){
        if (purchaseAmount <= getBalance()){
            transactions.add(purchaseAmount);
            super.reduceBalance(purchaseAmount);
        }
    }

    public int getNumTransactions() {
        return transactions.size();
    }

    public double getBalance() {
        return super.getBalance();
    }

}
