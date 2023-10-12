from BillCounter.Bill.Coke import Coke


class SmallCoke(Coke):

    def name(self):
        return "300 ml Coke"

    def size(self):
        return 'Small Size'

    def price(self):
        return 25.0
    