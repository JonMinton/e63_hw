class CompoundInterest:
    def __init__(self, P, r, t, n):
        self.P = P
        self.r = r
        self.t = t
        self.n = n

    def calc_end_amount(self):
        self.A = self.P * (1 + self.r / self.n) ** (self.n * self.t)

    def return_end_amount(self):
        return self.A

# A = P(1 + r/n)<sup>nt</sup>