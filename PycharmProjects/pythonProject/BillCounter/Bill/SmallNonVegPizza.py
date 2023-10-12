from BillCounter.Bill.NonVegPizza import NonVegPizza


class SmallNonVegPizza(NonVegPizza):
    def name(self): return "Non-Veg Pizza"

    def size(self): return "Small size"

    def price(self): return 180.0
