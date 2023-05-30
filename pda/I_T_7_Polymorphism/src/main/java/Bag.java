import java.util.ArrayList;

public class Bag {

    private String name;
    private ArrayList<IThrowable> throwables;

    public Bag(String name) {
        this.name = name;
        this.throwables = new ArrayList<IThrowable>();
    }


    public void addThrowable(IThrowable throwable) {
        this.throwables.add(throwable);
    }

    public void dropThrowable(IThrowable throwable) {
        this.throwables.remove(throwable);
    }

    public void useThrowable(IThrowable throwable) {
        if (this.throwables.contains(throwable)){
            throwable.throwItem();
            this.throwables.remove(throwable);
        }
    }


    public ArrayList<IThrowable> getThrowables() {
        return throwables;
    }

    public void setThrowables(ArrayList<IThrowable> throwables) {
        this.throwables = throwables;
    }
}
