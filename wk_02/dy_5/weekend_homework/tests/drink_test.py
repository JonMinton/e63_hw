import unittest

from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Red Wine", "Wine", 0.12, 3.00)
        self.drink2 = Drink("Wheat Beer", "Beer", 0.055, 6.50)
        self.drink3 = Drink("Small Beer", "Beer", 0.005, 1.50)
        self.drink4 = Drink("Orange Juice", "Soft Drink", 0.0, 1.80)
    
    def test_drinks_have_names(self):
        self.assertEqual("Red Wine", self.drink1.name)
        self.assertEqual("Wheat Beer", self.drink2.name)

    def test_drinks_have_types(self):
        self.assertEqual("Beer", self.drink2.type)
        self.assertEqual("Soft Drink", self.drink4.type)

    def test_drinks_have_abvs(self):
        self.assertEqual(0.055, self.drink2.abv)
        self.assertEqual(0.005, self.drink3.abv)

    def test_drinks_have_prices(self):
        self.assertEqual(3.00, self.drink1.price)
        self.assertEqual(1.80, self.drink4.price)
