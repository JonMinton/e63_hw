import unittest
from src.drink import Drink
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Beer", 4.00, 3.00, 100)
        self.drink2 = Drink("Wine", 6.00, 6.00, 30)
        self.drink3 = Drink("Champagne", 12.00, 5.00, 10)
        self.drinks = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("Simpletons", 500.00, self.drinks)
        self.customer1 = Customer("Alice", 50, 25)
        self.customer2 = Customer("Baby Boris", 70, 15)
        self.customer3 = Customer("Cashstrapped Charlie", 3.00, 50)
        self.customer4 = Customer("Down-at-heels Derek", 10.00, 68)

    def test_has_name(self):
        self.assertEqual("Simpletons", self.pub.name)

    def test_wont_sell_to_underage(self):
        self.assertEqual(70, self.customer2.wallet)
        self.pub.sell_drink(self.drink3, self.customer2)
        self.assertEqual(70, self.customer2.wallet)

    def test_wont_sell_if_not_rich_enough(self):
        self.assertEqual(3.00, self.customer3.wallet)
        self.pub.sell_drink(self.drink2, self.customer3)
        self.assertEqual(3.00, self.customer3.wallet)

    def test_pub_can_sell_a_drink(self):
        self.assertEqual(500.00, self.pub.till)
        self.pub.sell_drink(self.drink1, self.customer1)
        self.assertEqual(504.00, self.pub.till)
        self.pub.sell_drink(self.drink2, self.customer1)
        self.assertEqual(510.00, self.pub.till)

    def test_can_get_drink_names(self):
        self.assertEqual(
            ["Beer", "Wine", "Champagne"],
            self.pub.get_drink_names()
        )

    def test_drinks_customer_can_afford(self):
        self.assertEqual(
            ["Beer", "Wine"],
            self.pub.get_drinks_customer_can_afford(self.customer4)
        )
        
    def test_pub_can_count_stock(self):
        self.assertEqual(
            140.0,
            self.pub.count_stock()
        )

    def test_pub_can_get_total_stock_value(self):
        self.assertEqual(
            700,
            self.pub.get_stock_value()
        )
    

    

