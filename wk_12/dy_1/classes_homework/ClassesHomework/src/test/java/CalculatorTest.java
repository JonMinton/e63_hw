import org.example.Calculator;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CalculatorTest {

    private Calculator calculator;

    @Before
    public void setUp() {
        calculator = new Calculator();
    }

    @Test
    public void canAdd() {
        int value1 = 4;
        int value2 = 7;
        assertEquals(11, calculator.add(value1, value2));
    }

    @Test
    public void canSubtract() {
        int value1 = 8;
        int value2 = 5;
        assertEquals(3, calculator.subtract(value1, value2));
    }

    @Test
    public void canMultiply() {
        int value1 = 4;
        int value2 = 5;
        assertEquals(20, calculator.multiply(value1, value2));
    }

    @Test
    public void canDivide() {
        double value1 = 1.00;
        double value2 = 2.00;
        assertEquals(0.500, calculator.divide(value1, value2), 0.0);
    }

}



//Calculator
//        Create a Calculator class.
//        This should have functions for Add, Subtract, Multiply and Divide.
//        Your methods should take in two ints to perform the calculations on (except the Divide method. This should take two doubles as arguments).
//        HINT: you will need to have an empty constructor function or no constructor function at all!(The compiler automatically provides a public no-argument constructor for any class without constructor)