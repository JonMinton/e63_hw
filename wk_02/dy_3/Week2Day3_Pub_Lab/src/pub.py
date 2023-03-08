class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.max_drunkenness = 25
    

    def sell_drink(self, drink, customer):
        self.till += drink.price

    def get_drink_names(self):
        return [x.name for x in self.drinks]
    
    def get_drinks_customer_can_afford(self, customer):
        return [x.name for x in self.drinks if x.price <= customer.wallet]

    def count_stock(self):
        return sum([x.stock for x in self.drinks])
    
    def get_stock_value(self):
        return sum([x.stock * x.price for x in self.drinks])
