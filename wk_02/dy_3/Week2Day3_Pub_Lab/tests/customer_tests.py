import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Beer", 4.00, 3.00, 1)
        self.drink2 = Drink("Wine", 6.00, 6.00, 1)
        self.drink3 = Drink("Champagne", 12.00, 5.00, 1)
        self.drink4 = Drink("Absinthe", 10.00, 20.00, 1)
        self.drinks = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("Simpletons", 500.00, self.drinks)
        self.customer1 = Customer("Jon", 50.00, 42)
        self.customer2 = Customer("Rodger", 40.00, 30)
        self.customer3 = Customer("Steaming Stevie", 100.00, 43, 40.00)
        self.food1 = Food("chips", 3.50, 2.00)
        self.food2 = Food("curry", 8.00, 6.00)
        self.food3 = Food("salad", 7.50, 0.50)
        
    def test_have_names(self):
        self.assertEqual("Jon", self.customer1.name)
        self.assertEqual("Rodger", self.customer2.name)

    def test_has_ages(self):
        self.assertEqual(42, self.customer1.age)
        self.assertEqual(30, self.customer2.age)

    def test_have_money(self):
        self.assertEqual(50.00, self.customer1.wallet)
        self.assertEqual(40.00, self.customer2.wallet)

    def test_can_buy_drink(self):
        self.assertEqual(500.00, self.pub.till)
        self.assertEqual(50.00, self.customer1.wallet)
        self.customer1.buy_a_drink(self.pub, self.drink2)
        self.assertEqual(44.00, self.customer1.wallet)
        self.assertEqual(506.00, self.pub.till)

    def test_can_get_more_drunk(self):
        self.assertEqual(0.00, self.customer1.drunkenness)
        self.customer1.buy_a_drink(self.pub, self.drink1)
        self.assertEqual(3.00, self.customer1.drunkenness)

        self.assertEqual(0.00, self.customer2.drunkenness)
        self.customer2.buy_a_drink(self.pub, self.drink2)
        self.customer2.buy_a_drink(self.pub, self.drink3)
        self.assertEqual(11.00, self.customer2.drunkenness)

    def test_can_get_drunk_and_refused(self):
        self.assertEqual(0.00, self.customer2.drunkenness)
        self.customer2.buy_a_drink(self.pub, self.drink4)
        self.assertEqual(20.00, self.customer2.drunkenness)
        self.assertEqual(30.00, self.customer2.wallet)

        self.customer2.buy_a_drink(self.pub, self.drink4)
        self.assertEqual(40.00, self.customer2.drunkenness)
        self.assertEqual(20.00, self.customer2.wallet)

        self.customer2.buy_a_drink(self.pub, self.drink4)
        self.assertEqual(40.00, self.customer2.drunkenness)
        self.assertEqual(20.00, self.customer2.wallet)

    def test_food_costs_money_and_rejuvinates(self):
        self.assertEqual(40.00, self.customer3.drunkenness)
        self.assertEqual(100.00, self.customer3.wallet)

        self.customer3.buy_a_meal(self.food1)

        self.assertEqual(38.00, self.customer3.drunkenness)
        self.assertEqual(96.50, self.customer3.wallet)

        self.customer3.buy_a_meal(self.food2)

        self.assertEqual(32.00, self.customer3.drunkenness)
        self.assertEqual(88.50, self.customer3.wallet)

    def test_customer_can_buy_drink_and_food(self):
        self.assertEqual(50.00, self.customer1.wallet)
        self.customer1.buy_a_drink(self.pub, self.drink1)
        self.customer1.buy_a_drink(self.pub, self.drink1)
        self.assertEqual(42.00, self.customer1.wallet)
        self.assertEqual(6.00, self.customer1.drunkenness)
        self.customer1.buy_a_meal(self.food2)
        self.assertEqual(34.00, self.customer1.wallet)
        self.assertEqual(0.00, self.customer1.drunkenness)

        




    