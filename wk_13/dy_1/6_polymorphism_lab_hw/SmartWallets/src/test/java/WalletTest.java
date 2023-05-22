import org.junit.Before;
import org.junit.Test;

import java.sql.Date;

import static org.junit.Assert.assertEquals;

public class WalletTest {

    Wallet wallet;

    GiftCard giftCard;
    CreditCard creditCard;
    DebitCard debitCard;

    @Before
    public void setUp(){
        wallet = new Wallet();

        giftCard = new GiftCard(60);
        creditCard = new CreditCard(1020, 12345678, Date.valueOf("2020-3-10"), 543, 0.05, 4000);
        debitCard = new DebitCard(400, 12345678, Date.valueOf("2022-05-01"), 1234, 4567);

        wallet.addChargeable(giftCard);
        wallet.addChargeable(creditCard);
        wallet.addChargeable(debitCard);
    }


    @Test
    public void thereAreThreeChargeables() {
        assertEquals(3, wallet.getNumChargeables());
    }

    @Test
    public void setChargeGiftCard() {
        wallet.selectActiveChargeable(giftCard);

        assertEquals(60, giftCard.getBalance(), 0.01);
        wallet.chargeWithActive(10);
        assertEquals(50, giftCard.getBalance(), 0.01);
    }

    @Test
    public void setChargeDebitCard() {
        wallet.selectActiveChargeable(debitCard);
        assertEquals(400, debitCard.getBalance(), 0.01);
        wallet.chargeWithActive(50);
        assertEquals(350, debitCard.getBalance(), 0.01);
        assertEquals(1, debitCard.getNumTransactions());


    }

    @Test
    public void setChargeCreditCard() {
        wallet.selectActiveChargeable(creditCard);
        assertEquals(1020, creditCard.getBalance(), 0.01);
        wallet.chargeWithActive(100);
        assertEquals(915, creditCard.getBalance(), 0.01);

    }

}
