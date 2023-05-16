import java.util.ArrayList;

public class Library {

    private ArrayList<Book> stock;
    private int stockLimit;

    public Library(int stockLimit) {
        this.stockLimit = stockLimit;
        this.stock = new ArrayList<Book>();
    }

    public void addBook(Book book){
        if (this.stock.size() < this.stockLimit) {
            this.stock.add(book);

        }
    }

    public void removeBook(Book book){
        if (this.stock.contains(book)){
            this.stock.remove(book);
        }
    }

    public int getStockSize() {
        return this.stock.size();
    }

    public boolean checkBookInStock(Book book) {
        return this.stock.contains(book);
    }

}
