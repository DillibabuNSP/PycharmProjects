from MobileCode.Mobile.IPhone import IPhone
from MobileCode.Mobile.Micromax import Micromax
from MobileCode.Mobile.MobileType import MobileType
from MobileCode.Mobile.Redmi import Redmi


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
