class OrderedItems:
    items = []

    def addItems(self, item):
        OrderedItems.items.append(item)

    def getCost(self):
        cost = 0.0
        for item in OrderedItems.items:
            cost += item.price()
        return cost

    def showItems(self):
        for item in OrderedItems.items:
            print(f"Item is: {item.name()}")
            print(f'Size is: {item.size()}')
            print(f'Price is: {item.price()}')
