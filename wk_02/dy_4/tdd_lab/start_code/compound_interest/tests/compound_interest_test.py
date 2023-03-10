import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    # Tests

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_scenario_01(self):
        calc_01 = CompoundInterest(100, 0.10, 20, 12)
        calc_01.calc_end_amount()
        self.assertEqual(732.81, round(calc_01.return_end_amount(), 2))
    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_scenario_02(self):
        calc_02 = CompoundInterest(100, 0.06, 10, 12)
        calc_02.calc_end_amount()
        self.assertEqual(181.94, round(calc_02.return_end_amount(), 2))

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_scenario_03(self):
        calc_03 = CompoundInterest(100000, 0.05, 8, 12)
        calc_03.calc_end_amount()
        self.assertEqual(149058.55, round(calc_03.return_end_amount(), 2))

    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_scenario_04(self):
        calc_04 = CompoundInterest(0, 0.10, 1, 12)
        calc_04.calc_end_amount()
        self.assertEqual(0.00, round(calc_04.return_end_amount(), 2))

    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_scenario_05(self):
        calc_05 = CompoundInterest(100, 0.00, 10, 12)
        calc_05.calc_end_amount()
        self.assertEqual(100.00, round(calc_05.return_end_amount(), 2))


    # Extention tests

    # # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month
    def test_advanced_scenario_01(self):
        acalc_01 = CompoundInterest(100, 0.05, 8, 12, 1000)
        acalc_01.calc_amounts_with_monthly_addition()
        self.assertEqual(
            118380.16,
            round(acalc_01.return_end_amounts_with_monthly_addition(), 2) 
        )
    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

