package models;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

public class ShoppingBasket {

    Customer customer;

    ArrayList<Item> items;

    public ShoppingBasket(Customer customer) {
        this.customer = customer;
        this.items = new ArrayList<>();
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

    public ArrayList<Item> getItems() {
        return items;
    }

    public void setItems(ArrayList<Item> items) {
        this.items = items;
    }

    public void addItem(Item item){
        this.items.add(item);
    }

    public void removeItem(Item item){
        if (this.items.contains(item)) {
            this.items.remove(item);
        }
    }

    public void emptyBasket(){
        this.items.clear();
    }

    public HashMap<String , Integer> calcNumItemsOfEachType() {
        HashMap<String, Integer> itemsAndQuantities = new HashMap<String, Integer>();
        for (Item item : this.items) {
            if (itemsAndQuantities.containsKey(item.getName())) {
                itemsAndQuantities.put(
                        item.getName(),
                        itemsAndQuantities.get(item.getName()) + 1
                );
            } else {
                itemsAndQuantities.put(item.getName(), 1);
            }
        }
        return itemsAndQuantities;
    }


    public HashMap<String, Boolean> getBogofStatusOfItems() {
        HashMap<String, Boolean> itemBogof = new HashMap<String, Boolean>();
        for (Item item : this.items) {
            if (!itemBogof.containsKey(item.getName())) {
                itemBogof.put(item.getName(), item.isBogof());
            }
        }
        return itemBogof;
    }

    public HashMap<String, Double> getPriceOfItems() {
        HashMap<String, Double> itemsPrice = new HashMap<String, Double>();
        for (Item item : this.items) {
            if (!itemsPrice.containsKey(item.getName())){
                itemsPrice.put(item.getName(), item.getPrice());
            }
        }
        return itemsPrice;
    }

    public int getNumberToPayFor(String itemName) {
        HashMap<String, Integer> numItemsHash = calcNumItemsOfEachType();
        int numItems = numItemsHash.get(itemName);
        if (getBogofStatusOfItems().get(itemName)){
            numItems = (int) Math.ceil( (double) numItems / 2) ;
        }
        return numItems;

    }

    public double calcTotal() {
        double total = 0;
        HashMap<String, Double> itemsPrice = getPriceOfItems();
        for(Map.Entry<String, Double> entry : itemsPrice.entrySet()) {
            String itemName = entry.getKey();
            double itemPrice = entry.getValue();
            double effectiveItemQuantity = (double) getNumberToPayFor(itemName);
            double subtotal = itemPrice * effectiveItemQuantity;
            total += subtotal;
        }
        if (total >= 20.0) {
            total = total * 0.90;
        }
        if (this.getCustomer().isHasLoyaltyCard()) {
            total = total * 0.98;
        }
        return total;
    }
}
