public class Runner {
    public static void main(String[] args) {
        Planet mars = new Planet("Mars", 908973);

        System.out.println(mars.getName() + " has size " + mars.getSize());

        mars.explode();


    }
}
