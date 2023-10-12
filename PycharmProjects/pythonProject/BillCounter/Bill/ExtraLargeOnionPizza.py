from BillCounter.Bill.VegPizza import VegPizza


class ExtraLargeOnionPizza(VegPizza):
    def name(self): return "Onion Pizza"

    def size(self): return "Extra Large size"

    def price(self): return 200.0
