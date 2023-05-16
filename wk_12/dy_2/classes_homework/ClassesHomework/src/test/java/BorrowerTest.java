import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;



public class BorrowerTest {


    Book book1;
    Book book2;
    Book book3;
    Book book4;

    Library library;
    Borrower borrower;
    @Before
    public void setUp() {
        book1 = new Book("To Kill a Mockingbird", "Harper Lee", "Historical Fiction");
        book2 = new Book("1984", "George Orwell", "Dystopian Fiction");
        book3 = new Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction/Humour");
        book4 = new Book("The Great Gatsby", "F. Scott Fitzgerald", "Literary Fiction");

        library = new Library(3);
        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);

        borrower = new Borrower("Bob");
    }

    @Test
    public void borrowerHasName() {
        assertEquals("Bob", borrower.getName());
    }

    @Test
    public void borrowerStartsWithNoBooks() {
        assertEquals(0, borrower.getCollectionSize());
    }

    @Test
    public void borrowerCanBorrowBookInLibrary() {
        borrower.borrowFromLibrary(book2, library);
        assertEquals(1, borrower.getCollectionSize());
        assertEquals(2, library.getStockSize());
    }

    @Test
    public void borrowerCannotBorrowBookNotInLibrary() {
        borrower.borrowFromLibrary(book4, library);
        assertEquals(0, borrower.getCollectionSize());
        assertEquals(3, library.getStockSize());

    }

}


//    Add a third class which interacts with the other two. E.g. you could add a Borrower with a method that takes a Book and moves to the Borrower's collection.