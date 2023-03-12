class Stocks:
    def __init__(self, drinks):
        self.stock_dict = dict([(x.name, 0) for x in drinks])

    def stock_drink(self, name, amt):
        self.stock_dict[name] += amt