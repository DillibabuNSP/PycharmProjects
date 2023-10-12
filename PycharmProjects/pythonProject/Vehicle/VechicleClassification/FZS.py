from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class FZS(McwgVehicles):
    def name(self):
        return "Yamaha Fzs"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "180Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{1,39,000}Rs -On Road Price"
