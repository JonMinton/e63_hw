import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Beer", 4.00, 3.00, 1)
        self.drink2 = Drink("Wine", 6.00, 6.00, 1)
        self.drink3 = Drink("Champagne", 12.00, 5.00, 1)
        self.drinks = [self.drink1, self.drink2, self.drink3]

    def test_drinks_have_names(self):
        self.assertEqual("Beer", self.drink1.name)
        self.assertEqual("Wine", self.drink2.name)
        self.assertEqual("Champagne", self.drink3.name)
    
    def test_drinks_have_prices(self):
        self.assertEqual(4.00, self.drink1.price)
        self.assertEqual(6.00, self.drink2.price)
        self.assertEqual(12.00, self.drink3.price)

    def test_drinks_have_units(self):
        self.assertEqual(3.00, self.drink1.alc_units)
        self.assertEqual(6.00, self.drink2.alc_units)
        self.assertEqual(5.00, self.drink3.alc_units)


    def test_drinks_has_enough_drinks(self):
        self.assertEqual(3, len(self.drinks))



    
