import unittest

from src.high_scores import latest, personal_best, personal_top_three, personal_sorted

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.scores = [500, 300, 800, 2000, 600]

    # Test latest score (the last thing in the list)
    def test_returns_last_score(self):
        self.assertEqual(600, latest(self.scores))
    # Test personal best (the highest score in the list)
    def test_returns_highest_score(self):
        self.assertEqual(2000, personal_best(self.scores))
    # Test top three from list of scores
    def test_returns_top_three(self):
        self.assertEqual([2000, 800, 600], personal_top_three(self.scores))

    # Test ordered from highest to lowest
    def test_returns_sorted_scores(self):
        self.assertEqual([2000, 800, 600, 500, 300], personal_sorted(self.scores))

    # Test top three when there is a tie
    def test_returns_top_when_tie(self):
        tied_scores = [500, 600, 200, 600, 800]
        self.assertEqual([800, 600, 600], personal_top_three(tied_scores))

    # Test top three when there are less than three
    def test_returns_top_from_under_three(self):
        little_scores = [500, 1000]
        self.assertEqual([1000, 500], personal_top_three(little_scores))

    # Test top three when there is only one
    def test_returns_top_one_from_one(self):
        single_score = [1000]
        self.assertEqual([1000], personal_top_three(single_score))
    
