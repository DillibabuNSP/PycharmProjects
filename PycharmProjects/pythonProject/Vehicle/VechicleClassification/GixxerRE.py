from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class GixxerRE(McwgVehicles):
    def name(self):
        return "Suzuki Gixxer - RE"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "2700Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{1,45,000}Rs - On Road Price"
