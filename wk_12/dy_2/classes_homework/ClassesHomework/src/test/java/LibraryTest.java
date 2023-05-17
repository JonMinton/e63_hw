import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;



public class LibraryTest {

    Book book1;
    Book book2;
    Book book3;
    Book book4;

    Library library;
    @Before
    public void setUp() {
        book1 = new Book("To Kill a Mockingbird", "Harper Lee", "Historical Fiction");
        book2 = new Book("1984", "George Orwell", "Dystopian Fiction");
        book3 = new Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction/Humour");
        book4 = new Book("The Great Gatsby", "F. Scott Fitzgerald", "Literary Fiction");

        library = new Library(3);
//
    }

    @Test
    public void canCountBooksInLibraryWhenEmpty(){
        assertEquals(0, library.getStockSize());
    }

    @Test
    public void canAddBooks() {
        assertEquals(0, library.getStockSize());
        library.addBook(book1);
        assertEquals(1, library.getStockSize());

    }

    @Test
    public void cannotAddBooksWhenAboveLimit() {
        assertEquals(0, library.getStockSize());
        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);
        assertEquals(3, library.getStockSize());
        library.addBook(book4);
        assertEquals(3, library.getStockSize());
    }

    @Test
    public void canCheckIfBookInStock() {
        library.addBook(book1);
        library.addBook(book2);
        assertEquals(true, library.checkBookInStock(book1));
        assertEquals(false, library.checkBookInStock(book3));

    }

    @Test
    public void canRemoveBookIfInStock() {
        library.addBook(book1);
        library.addBook(book2);
        assertEquals(2, library.getStockSize());
        library.removeBook(book1);
        assertEquals(1, library.getStockSize());
    }

    @Test
    public void cannotRemoveBookIfNotInStock() {
        library.addBook(book1);
        library.addBook(book2);
        assertEquals(2, library.getStockSize());
        library.removeBook(book3);
        assertEquals(2, library.getStockSize());
    }

    @Test
    public void canSeeGenreFrequencyIsCorrect() {
        System.out.println(book1.getGenre());
        library.addBook(book1);
        Integer thisGenreFrequency = library.checkGenreFrequency("Historical Frequency");
        System.out.println(thisGenreFrequency);

    }


}

//    Write a method to count the number of books in the library.
//        Write a method to add a book to the library stock.
//        Add a capacity to the library and write a method to check if stock is full before adding a book.

//The library wants to keep track of its number of books by genre. Using a HashMap, store the genre of each book as the key - and a count of how many books of that genre as the value.