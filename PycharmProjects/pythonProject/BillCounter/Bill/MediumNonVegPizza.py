from BillCounter.Bill.NonVegPizza import NonVegPizza


class MediumNonVegPizza(NonVegPizza):
    def name(self): return "Non-Veg Pizza"

    def size(self): return "Medium size"

    def price(self): return 200.0
