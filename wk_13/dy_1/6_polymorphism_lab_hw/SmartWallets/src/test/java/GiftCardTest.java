import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class GiftCardTest {

    GiftCard giftCard;

    @Before
    public void setUp() {
        giftCard = new GiftCard(50.00);
    }

    @Test
    public void canCheckBalance() {
        assertEquals(50.00, giftCard.getBalance(), 0.01);
    }

    @Test
    public void canMakeCharge() {
        giftCard.charge(5.00);
        assertEquals(45.00, giftCard.getBalance(), 0.01);
    }
}
