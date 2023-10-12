from BillCounter.Bill.Coke import Coke


class LargeCoke(Coke):

    def name(self):
        return "750 ml Coke"

    def size(self):
        return "Large Size"

    def price(self):
        return 50.0
