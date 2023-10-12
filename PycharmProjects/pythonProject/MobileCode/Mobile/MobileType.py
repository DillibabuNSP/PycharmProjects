class MobileType:
    items = []

    def addItems(self, packs):
        MobileType.items.clear()
        MobileType.items.append(packs)

    def showItems(self):
        for packing in MobileType.items:
            print(f'Mobile Name: {packing.pack()}, Price: {packing.price()}')

