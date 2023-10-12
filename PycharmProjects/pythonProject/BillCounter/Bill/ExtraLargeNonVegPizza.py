from BillCounter.Bill.NonVegPizza import NonVegPizza


class ExtraLargeNonVegPizza(NonVegPizza):
    def name(self): return "non-Veg Pizza"

    def size(self): return "Extra Large size"

    def price(self): return 250.0
