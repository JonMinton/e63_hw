import org.junit.Before;
import org.junit.Test;
import techStaff.DatabaseAdmin;
import techStaff.Developer;

import static org.junit.Assert.assertEquals;

public class DatabaseAdminTest {

    DatabaseAdmin databaseAdmin;

    @Before
    public void setUp() {
        databaseAdmin = new DatabaseAdmin("Gilfoyle", "CAN-105", 64966.60);
    }

    @Test
    public void hasName() {
        assertEquals("Gilfoyle", databaseAdmin.getName());
    }

    @Test
    public void hasNi() {
        assertEquals("CAN-105", databaseAdmin.getNiNumber());
    }

    @Test
    public void hasSalary() {
        assertEquals(64966.60, databaseAdmin.getSalary(), 0.01);
    }

    @Test
    public void canRaiseSalary() {
        assertEquals(64966.60, databaseAdmin.getSalary(), 0.01);
        databaseAdmin.raiseSalary(0.40);
        assertEquals(64967.00, databaseAdmin.getSalary(), 0.01);

    }

    @Test
    public void canPayBonus() {
        assertEquals(649.666, databaseAdmin.payBonus(), 0.01);
    }

}