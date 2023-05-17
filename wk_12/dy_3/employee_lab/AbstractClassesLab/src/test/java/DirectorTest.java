import management.Director;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class DirectorTest {

    Director director;

    @Before
    public void setUp() {
        director = new Director("Jess Bozos", "BOS-5000", 100_000_000, "BoxCorp", 900 );
    }

    @Test
    public void canGetBudget() {
        assertEquals(900, director.getBudget(), 0.01);
    }

    @Test
    public void canGetPositiveRaise() {
        director.raiseSalary(5.00);
        assertEquals(100_000_005, director.getSalary(), 0.01);
    }

    @Test
    public void cannotGivePositiveRaise() {
        director.raiseSalary(-25.3);
        assertEquals(100_000_000, director.getSalary(), 0.01);

    }

    @Test
    public void directorGets2pcBonus() {
        assertEquals(2000000.0, director.payBonus(), 0.01);
    }

//    Other tests omitted for reasons of tedium


}
