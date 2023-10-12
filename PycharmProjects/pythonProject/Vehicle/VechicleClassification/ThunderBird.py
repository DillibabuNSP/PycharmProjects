from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class ThunderBird(McwgVehicles):
    def name(self):
        return "Royal Enfield - Thunder Bird"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "250Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{1,84,000}Rs - On Road Price"
