from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class R15_V4 (McwgVehicles):
    def name(self):
        return "Yamaha R15-Version 4"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "250Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{1,88,000}Rs - On Road Price"
