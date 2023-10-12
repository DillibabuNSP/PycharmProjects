from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class GixxerSE(McwgVehicles):
    def name(self):
        return "Suzuki Gixxer - Standard"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "250Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{1,37,000}Rs - On Road Price"
