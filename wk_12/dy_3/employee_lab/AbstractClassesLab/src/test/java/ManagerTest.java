import management.Manager;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ManagerTest {

    Manager manager;

    @Before
    public void setUp() {
        manager = new Manager("Poindexter Hairboss", "PHB-666", 800000, "Ministry of Insufficient Light");
    }

    @Test
    public void hasName() {
        assertEquals("Poindexter Hairboss", manager.getName());
    }

    @Test
    public void hasNi() {
        assertEquals("PHB-666", manager.getNiNumber());
    }

    @Test
    public void hasSalary() {
        assertEquals(800000, manager.getSalary(), 0.01);
    }

    @Test
    public void hasDept() {
        assertEquals("Ministry of Insufficient Light", manager.getDeptName());
    }

    @Test
    public void canRaiseSalary() {
        assertEquals(800000, manager.getSalary(), 0.01);
        manager.raiseSalary(2);
        assertEquals(800002, manager.getSalary(), 0.01);

    }

    @Test
    public void canPayBonus() {
        assertEquals(8000, manager.payBonus(), 0.01);
    }
}
