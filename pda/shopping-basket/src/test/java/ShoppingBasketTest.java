import models.Customer;
import models.Item;
import models.ShoppingBasket;
import org.junit.Before;
import org.junit.Test;

import java.util.HashMap;

import static org.junit.Assert.assertEquals;

public class ShoppingBasketTest {

    Item egg;
    Item cheese;
    Item pomegranate;
    Item bread;
    Item wine;
    Item donuts;

    Customer loyalCustomer;
    Customer unloyalCustomer;

    ShoppingBasket loyalBasket;
    ShoppingBasket unloyalBasket;

    @Before
    public void setUp() {
        egg = new Item("eggs", 1.5, false);
        cheese = new Item("cheese", 4.20, true);
        pomegranate = new Item("pomegranate", 2.80, false);
        bread = new Item("bread", 1.20, false);
        wine = new Item("wine", 10.00, false);
        donuts = new Item("donuts", 5.10, true);

        loyalCustomer = new Customer("Loyal Susan", true);
        unloyalCustomer = new Customer("Occasional Eric", false);

        loyalBasket = new ShoppingBasket(loyalCustomer);
        unloyalBasket = new ShoppingBasket(unloyalCustomer);

    }

    @Test
    public void basketsStartEmpty() {
        assertEquals(0, loyalBasket.getItems().size());
        assertEquals(0, unloyalBasket.getItems().size());

    }

    @Test
    public void canAddItemsToBasket() {
        loyalBasket.addItem(cheese);
        loyalBasket.addItem(cheese);

        assertEquals(2, loyalBasket.getItems().size());
    }

    @Test
    public void canRemoveAddedItems() {
        loyalBasket.addItem(egg);
        loyalBasket.addItem(cheese);
        assertEquals(2, loyalBasket.getItems().size());
        loyalBasket.removeItem(cheese);
        assertEquals(1, loyalBasket.getItems().size());
    }

    @Test
    public void canEmptyBasket() {
        loyalBasket.addItem(egg);
        loyalBasket.addItem(cheese);
        assertEquals(2, loyalBasket.getItems().size());
        loyalBasket.emptyBasket();
        assertEquals(0, loyalBasket.getItems().size());
    }

    @Test
    public void canCountNumbersOfSameItem() {
        loyalBasket.addItem(egg);
        loyalBasket.addItem(egg);
        loyalBasket.addItem(cheese);
        loyalBasket.addItem(cheese);
        loyalBasket.addItem(cheese);

        System.out.println(loyalBasket.calcNumItemsOfEachType());
        assertEquals(2, loyalBasket.calcNumItemsOfEachType().size());
    }


    @Test
    public void canReturnBogofStatusAsHashmap() {
        loyalBasket.addItem(egg);
        loyalBasket.addItem(egg);
        loyalBasket.addItem(cheese);
        loyalBasket.addItem(cheese);
        loyalBasket.addItem(pomegranate);

        HashMap<String, Boolean> bogofHash = loyalBasket.getBogofStatusOfItems();
        assertEquals(true, bogofHash.get("cheese"));
        assertEquals(false, bogofHash.get("eggs"));

    }

    @Test
    public void canReturnPricesAsHashmap() {
        loyalBasket.addItem(egg);
        loyalBasket.addItem(egg);
        loyalBasket.addItem(cheese);
        loyalBasket.addItem(bread);
        loyalBasket.addItem(pomegranate);

        HashMap<String, Double> priceHash = loyalBasket.getPriceOfItems();
        System.out.println(priceHash);
        assertEquals(1.20, priceHash.get("bread"), 0.01);
        assertEquals(2.80, priceHash.get("pomegranate"), 0.01);

    }

    @Test
    public void canGetNumItemsToPayFor() {
        loyalBasket.addItem(egg);
        loyalBasket.addItem(egg);

//eggs not bogof, so 2 is 2
        assertEquals(2, loyalBasket.getNumberToPayFor("eggs"));

//        cheese is bogof
//        1 cheese = 1
        loyalBasket.addItem(cheese);
        assertEquals(1, loyalBasket.getNumberToPayFor("cheese"));
//        2 cheeses = 1
        loyalBasket.addItem(cheese);
        assertEquals(1, loyalBasket.getNumberToPayFor("cheese"));
//        3 cheeses = 2 (as 3rd cheese doesn't have a pair)
        loyalBasket.addItem(cheese);
        assertEquals(2, loyalBasket.getNumberToPayFor("cheese"));
//        4 cheeses = 2 (as 4th pairs with 3rd)
        loyalBasket.addItem(cheese);
        assertEquals(2, loyalBasket.getNumberToPayFor("cheese"));
//        5 cheeses = 3 (as 5th has no pair)
        loyalBasket.addItem(cheese);
        assertEquals(3, loyalBasket.getNumberToPayFor("cheese"));


    }

    @Test
    public void canCalculateTotalIncludingBogofs() {
        unloyalBasket.addItem(egg);
        unloyalBasket.addItem(egg);
        unloyalBasket.addItem(cheese);
        unloyalBasket.addItem(cheese);
        double eggPrice = egg.getPrice();
        double cheesePrice = cheese.getPrice();
        assertEquals(2.0 * eggPrice + 1.0 * cheesePrice, unloyalBasket.calcTotal(), 0.01);
    }

    @Test
    public void canGetTenpcDiscountIfOver20() {
        unloyalBasket.addItem(wine);
        unloyalBasket.addItem(wine);

        assertEquals(18.0, unloyalBasket.calcTotal(), 0.01);
    }

    @Test
    public void canGetTwoPcDiscountIfLoyal() {
        loyalBasket.addItem(wine);

        assertEquals(9.80, loyalBasket.calcTotal(), 0.01);
    }

    @Test
    public void canGetBothDiscountsIfLoyalAndSpendsEnough() {
        loyalBasket.addItem(wine);
        loyalBasket.addItem(wine);
        assertEquals(18.0 * 0.98, loyalBasket.calcTotal(), 0.01);
    }

    @Test
    public void canGetAllThreeDiscountTypes() {
        loyalBasket.addItem(wine);
        loyalBasket.addItem(wine);
        loyalBasket.addItem(cheese);
        loyalBasket.addItem(cheese);
        double expectedPrice = (2 * wine.getPrice() + 1 * cheese.getPrice()) * 0.90 * 0.98;
        System.out.println(expectedPrice);
        assertEquals(expectedPrice, loyalBasket.calcTotal(), 0.01);

    }

}
