from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class Himalayan(McwgVehicles):
    def name(self):
        return "Royal Enfield - Himalayan"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "250Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{1,80,000}Rs - On Road Price"
