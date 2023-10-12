from BillCounter.Bill.Coke import Coke


class MediumCoke(Coke):
    def name(self): return "500 ml Coke"

    def size(self): return "Medium Size"

    def price(self): return 35.0
