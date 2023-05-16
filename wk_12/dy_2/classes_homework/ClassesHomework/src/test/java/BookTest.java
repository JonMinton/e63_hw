import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;


public class BookTest {

    Book book;
    @Before
    public void setUp() {
        book = new Book("Catch 22", "Joseph Heller", "Satire");
    }

//    Books should have title, author and genre.

    @Test
    public void bookHasTitle() {
        assertEquals("Catch 22", book.getTitle());
    }

    @Test
    public void bookHasAuthor() {
        assertEquals("Joseph Heller", book.getAuthor());
    }
    @Test
    public void bookHasGenre() {
        assertEquals("Satire", book.getGenre());
    }

}
