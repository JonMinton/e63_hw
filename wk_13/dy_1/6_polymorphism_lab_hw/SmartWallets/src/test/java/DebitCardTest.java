import org.junit.Before;
import org.junit.Test;

import java.sql.Date;

import static org.junit.Assert.assertEquals;

public class DebitCardTest {

    DebitCard debitCard;
    @Before
    public void setUp() {
        debitCard = new DebitCard(400, 12345678, Date.valueOf("2022-05-01"), 1234, 4567);
    }

    @Test
    public void canMakeTransaction(){
        assertEquals(400, debitCard.getBalance(), 0.01);
        debitCard.charge(50);
        assertEquals(350, debitCard.getBalance(), 0.01);

    }

    @Test
    public void transactionsLoggedAfterCharge() {
        assertEquals(0, debitCard.getNumTransactions());
        debitCard.charge(70);
        assertEquals(1, debitCard.getNumTransactions());
    }
}
