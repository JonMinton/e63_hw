import org.junit.Before;
import org.junit.Test;
import techStaff.Developer;

import static org.junit.Assert.assertEquals;

public class DeveloperTest {

    Developer developer;

    @Before
    public void setUp() {
        developer = new Developer("Dinesh", "PK-101", 65000);
    }

    @Test
    public void hasName() {
        assertEquals("Dinesh", developer.getName());
    }

    @Test
    public void hasNi() {
        assertEquals("PK-101", developer.getNiNumber());
    }

    @Test
    public void hasSalary() {
        assertEquals(65000, developer.getSalary(), 0.01);
    }

    @Test
    public void canRaiseSalary() {
        assertEquals(65000, developer.getSalary(), 0.01);
        developer.raiseSalary(5000);
        assertEquals(70000, developer.getSalary(), 0.01);

    }

    @Test
    public void canPayBonus() {
        assertEquals(650, developer.payBonus(), 0.01);
    }

    @Test
    public void canChangeNameIfNotNull() {
        developer.changeName("Super Dinesh");
        assertEquals("Super Dinesh", developer.getName());
    }

    @Test
    public void cannotChangeNameIfNull() {
        developer.changeName("");
        assertEquals("Dinesh", developer.getName());
    }

}
