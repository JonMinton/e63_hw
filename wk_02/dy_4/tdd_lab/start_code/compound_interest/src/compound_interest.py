class CompoundInterest:
    def __init__(self, P, r, t, n, addition = 0):
        self.P = P
        self.r = r
        self.t = t
        self.n = n
        self.addition = addition

    def calc_end_amount(self):
        return self.P * (1 + self.r / self.n) ** (self.n * self.t)

    def return_end_amount(self):
        return self.calc_end_amount()

    def calc_amounts_with_monthly_addition(self):
        return self.P * (1 + self.r / self.n) ** (self.n * self.t) + (self.addition * (1 + self.r / self.t) ** (self.n * self.t) - 1) / (self.r / self.n)
        # using formula specified here: 
        # https://www.bizskinny.com/Finance/Compound-Interest/compound-interest-with-monthly-contributions.php

    def return_end_amounts_with_monthly_addition(self):
        return self.calc_amounts_with_monthly_addition()

# A = P(1 + r/n)<sup>nt</sup>