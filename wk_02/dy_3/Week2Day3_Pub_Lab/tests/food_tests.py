import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food1 = Food("chips", 3.50, 1.00)
        self.food2 = Food("curry", 8.00, 6.00)
        self.food3 = Food("salad", 7.50, 0.50)

    def test_foods_have_names(self):
        self.assertEqual("chips", self.food1.name)
        self.assertEqual("curry", self.food2.name)
        self.assertEqual("salad", self.food3.name)

    def test_foods_have_prices(self):
        self.assertEqual(3.50, self.food1.price)
        self.assertEqual(8.00, self.food2.price)
        self.assertEqual(7.50, self.food3.price)        