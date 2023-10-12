from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class Platinum(McwgVehicles):
    def name(self):
        return "Bajaj Platinum"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "140Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{94,000}Rs - On Road Price"
