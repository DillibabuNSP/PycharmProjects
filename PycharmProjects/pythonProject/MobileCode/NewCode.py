
class Micromax:
    def price(self):
        return 7200

    def pack(self):
        return "Micromax Mobile"


class IPhone(Micromax):
    def price(self):
        return f'{1.3200}lakhs'

    def pack(self):
        return "IPhone Mobile"


class Redmi(IPhone):

    def price(self):
        return 6500

    def pack(self):
        return "Redmi Mobile"


class MobileType(Redmi):
    def __init__(self):
        self.items = []

    def addItems(self, packs):
        self.items.clear()
        self.items.append(packs)

    def showItems(self):
        for packing in self.items:
            print(f'Mobile Name: {packing.pack()}, Price: {packing.price()}')


class MobileBuilder:

    def buildMicromaxMP(self):
        Mds = MobileType()
        Mds.addItems(Micromax())
        return Mds

    def buildRedmiMP(self):
        Mds = MobileType()
        Mds.addItems(Redmi())
        return Mds

    def buildIPhoneMP(self):
        Mds = MobileType()
        Mds.addItems(IPhone())
        return Mds


class Builder(MobileBuilder, MobileType):
    mobileBuilder = MobileBuilder()

    Micromax = mobileBuilder.buildMicromaxMP()
    Micromax.showItems()

    Redmi = mobileBuilder.buildRedmiMP()
    Redmi.showItems()

    IPhone = mobileBuilder.buildIPhoneMP()
    IPhone.showItems()
