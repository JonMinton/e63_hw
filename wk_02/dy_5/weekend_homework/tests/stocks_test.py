import unittest

from src.stocks import Stocks
from src.drink import Drink

class TestStocks(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Red Wine", "Wine", 0.12, 3.00)
        self.drink2 = Drink("Wheat Beer", "Beer", 0.055, 6.50)
        self.drink3 = Drink("Small Beer", "Beer", 0.005, 1.50)
        self.drink4 = Drink("Orange Juice", "Soft Drink", 0.0, 1.80)
        self.drinks = [self.drink1, self.drink2, self.drink3, self.drink4]
        self.stocks = Stocks(self.drinks)


    def test_drinks_exists(self):
        self.assertEqual(4, len(self.drinks))

    def test_names_of_drinks_in_drinks_as_expected(self):
        self.assertEqual(
            ["Red Wine", "Wheat Beer", "Small Beer", "Orange Juice"],
            [x.name for x in self.drinks]
        )
    
    def test_stocks_class_converts_drink_names_to_a_dict(self):
        self.assertEqual(
            {"Red Wine": 0, "Wheat Beer": 0, "Small Beer": 0, "Orange Juice": 0},
            self.stocks.stock_dict
        )
    
    def test_drink_price_lookup_generated_from_drinks(self):
        self.assertEqual(
            {"Red Wine": 3.00, "Wheat Beer": 6.50, "Small Beer": 1.50, "Orange Juice": 1.80},
            self.stocks._drink_value
        )

    def test_can_calculate_total_stock_value(self):
        self.assertEqual(0.0, self.stocks.calc_total_stock_value())
        self.stocks.stock_drink("Wheat Beer", 2)
        self.assertEqual(13.0, self.stocks.calc_total_stock_value())
        self.stocks.stock_drink("Orange Juice", 1)
        self.assertEqual(14.8, self.stocks.calc_total_stock_value())

    def test_stocks_are_initially_zero(self):
        self.assertEqual(0, sum(self.stocks.stock_dict.values()))

    def test_can_add_stocks_by_name(self):
        self.assertEqual(0, sum(self.stocks.stock_dict.values()))
        self.stocks.stock_drink("Wheat Beer", 10)
        self.assertEqual(10, sum(self.stocks.stock_dict.values()))
        self.stocks.stock_drink("Orange Juice", 25)
        self.assertEqual(35, sum(self.stocks.stock_dict.values()))

