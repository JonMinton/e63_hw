import unittest
from src.card import Card
from src.card_game import CardGame



class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game1 = CardGame("Gamey")
        self.card1 = Card("J", 4)
        self.card2 = Card("S", 3)
        self.card3 = Card("H", 10)
        self.card4 = Card("S", 1)
        self.cards = [self.card1, self.card2, self.card3, self.card4]

    def test_game_exists(self):
        self.assertEqual("Gamey", self.game1.name)

    def test_can_check_for_ace(self):
        self.assertFalse(self.game1.check_for_ace(self.card1))
        self.assertTrue(self.game1.check_for_ace(self.card4))

    def test_can_determine_highest_card(self):
        self.assertEqual(
            4, 
            self.game1.highest_card(
                self.card1, 
                self.card4
            ).value
        )

        self.assertEqual(
            10,
            self.game1.highest_card(
            self.card2,
            self.card3
            ).value
        )

    def test_can_totalise_cards(self):
        self.assertEqual("You have a total of 18", self.game1.cards_total(self.cards))
