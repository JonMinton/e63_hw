import org.junit.Before;
import org.junit.Test;

import java.sql.Date;

import static org.junit.Assert.assertEquals;

public class CreditCardTest {

    CreditCard creditCard;
    @Before
    public void setUp() {
        creditCard = new CreditCard(1020, 12345678, Date.valueOf("2020-3-10"), 543, 0.05, 4000);
    }
    @Test
    public void makingPurchaseReducesBalance() {
        assertEquals(1020, creditCard.getBalance(), 0.01);

        creditCard.charge(50);
        assertEquals(967.50, creditCard.getBalance(), 0.01);

    }

    @Test
    public void cannotMakePurchaseAboveBalance() {
        creditCard.charge(1500);
        assertEquals(1020, creditCard.getBalance(), 0.01);
    }
}
