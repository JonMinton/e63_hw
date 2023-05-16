import java.util.ArrayList;

public class Borrower {

    private String name;

    private ArrayList<Book> collection;

    public Borrower(String name){
        this.name = name;
        collection = new ArrayList<Book>();
    }

    public String getName() {
        return this.name;
    }

    public int getCollectionSize() {
        return collection.size();
    }

    public void borrowFromLibrary(Book book, Library library){
        if (library.checkBookInStock(book)){
            collection.add(book);
            library.removeBook(book);
        }
    }


}
