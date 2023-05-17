import java.util.ArrayList;
import java.util.HashMap;

public class Library {

    private ArrayList<Book> stock;
    private int stockLimit;

    private HashMap<String, Integer> genreHashmap;

    public Library(int stockLimit) {
        this.stockLimit = stockLimit;
        this.stock = new ArrayList<Book>();
        this.genreHashmap = new HashMap<String, Integer>();
    }

    public void addBook(Book book){
        if (this.stock.size() < this.stockLimit) {
            this.stock.add(book);
            addToGenreHashmap(book);
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

    public void addToGenreHashmap(Book book){

        String genre = book.getGenre();
        System.out.println(genre);
        System.out.println(this.genreHashmap);

        //if the genre already exists in the hashmap, extract the existing count and assign it to the variable 'counter'
        if(this.genreHashmap.containsKey(genre)){
            int counter = this.genreHashmap.get(genre);

            // add one to the counter
            counter++;

            //put the key and new value back into the hashmap
            this.genreHashmap.put(genre, counter);

        } else {

            this.genreHashmap.put(genre, 1);
        }
    }

    public Integer checkGenreFrequency(String genre) {
        Integer returnedValue = this.genreHashmap.get(genre);
        System.out.println(returnedValue);
        return this.genreHashmap.get(genre);
    }

}
