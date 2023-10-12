from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class HondaShine(McwgVehicles):
    def name(self):
        return "Honda Shine"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "100Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{98,000}Rs - On Road Price"
