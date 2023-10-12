from BillCounter.Bill.OrderBuilder import OrderBuilder


class BuilderDemo:
    builder = OrderBuilder()

    orderedItems = builder.preparePizza()

    orderedItems.showItems()

    print("\n")
    print(f"Total Cost : {orderedItems.getCost()}")
