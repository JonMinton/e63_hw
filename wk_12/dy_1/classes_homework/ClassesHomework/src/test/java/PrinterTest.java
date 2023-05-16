import org.example.Printer;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PrinterTest {
    
    private Printer printer;
    
    @Before
    public void setUp(){
        printer = new Printer(200, 1000);
    }
    
    @Test
    public void canReturnNumberOfSheets() {
        assertEquals(200, printer.getNumSheets());
    }

    @Test
    public void canPrintManyCopies(){
        assertEquals(200, printer.getNumSheets());
        printer.print(10, 5);
        assertEquals(150, printer.getNumSheets());

    }

    @Test
    public void cannotPrintIfNotEnoughPaper(){
        assertEquals(200, printer.getNumSheets());
        printer.print(100, 3);
        assertEquals(200, printer.getNumSheets());
    }

    @Test
    public void tonerReducesWithNumberOfPagesPrinted() {
        assertEquals(1000, printer.getToner());
        printer.print(10, 10);
        assertEquals(900, printer.getToner());
    }
    
}


//Printer
//        Create a Printer class that has a property for number of sheets of paper left.
//        Add a method to print that takes in a number of pages and number of copies.
//        The print method will only run if the printer has enough paper. If it runs it will reduce the value of the paper left by number of copies * number of pages.
//        Add a toner volume property to the class.
//        Modify the printer so that it reduces the toner by 1 for each page printed.