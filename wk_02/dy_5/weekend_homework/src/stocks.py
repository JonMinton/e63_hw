class Stocks:
    def __init__(self, drinks):
        self.stock_dict = dict([(x.name, 0) for x in drinks])
        self._drink_value = dict([(x.name, x.price) for x in drinks])

    def stock_drink(self, name, amt):
        self.stock_dict[name] += amt

    def calc_total_stock_value(self):
        total_value = 0.0
        drink_names = list(self.stock_dict.keys())
        for x in drink_names:
            total_value += self.stock_dict[x] * self._drink_value[x]

        return total_value