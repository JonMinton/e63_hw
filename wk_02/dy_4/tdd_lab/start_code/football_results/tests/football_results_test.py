import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def setUp(self):
        self.game1 = {"home_score" : 0, "away_score": 3}
        self.game2 = {"home_score" : 0, "away_score": 0}
        self.game3 = {"home_score" : 2, "away_score": 1}
        self.games = [self.game1, self.game2, self.game3]

    # Test we get the right result string for a final score dictionary representing -
    def test_returns_which_team_wins(self):
        self.assertEqual(
            "Home win", 
            get_result(self.game3)
        )
        self.assertEqual(
            "Away win",
            get_result(self.game1)
        )
        self.assertEqual(
            "Draw",
            get_result(self.game2)
        )

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_list_of_game_results_is_correct(self):
        self.assertEqual(
            ["Away win", "Draw", "Home win"],
            get_results(self.games)
        )

if __name__ == "__main__":
    unittest.main()
