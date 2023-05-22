import java.util.Date;

public abstract class PaymentCard {

    private double balance;
    private int cardNumber;
    private Date expiryDate;
    private int securityNumber;

    public int getCardNumber() {
        return cardNumber;
    }

    public Date getExpiryDate() {
        return expiryDate;
    }

    public int getSecurityNumber() {
        return securityNumber;
    }

    public PaymentCard(double balance, int cardNumber, Date expiryDate, int securityNumber) {
        this.balance = balance;
        this.cardNumber = cardNumber;
        this.expiryDate = expiryDate;
        this.securityNumber = securityNumber;
    }

    public double getBalance() {
        return this.balance;
    }

    public void reduceBalance(double amount) {
        this.balance -= amount;
    }

}
