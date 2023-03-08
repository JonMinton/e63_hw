from src.pub import Pub
from src.drink import Drink
from src.food import Food

class Customer:
    def __init__(self, name, wallet, age, drunkenness = 0):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness
    
    def buy_a_drink(self, pub, drink):
        if drink.price <= self.wallet and self.age >= 18 and self.drunkenness <= pub.max_drunkenness:
            pub.sell_drink(drink, self)
            self.wallet -= drink.price
            self.drunkenness += drink.alc_units
    
    def buy_a_meal(self, food):
        if food.price <= self.wallet:
            self.wallet -= food.price
            self.drunkenness -= food.rejuvination_level