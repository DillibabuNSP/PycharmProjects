from BillCounter.Bill.NonVegPizza import NonVegPizza


class LargeNonVegPizza(NonVegPizza):
    def name(self): return "Non-Veg Pizza"

    def size(self): return "Large size"

    def price(self): return 220.0
