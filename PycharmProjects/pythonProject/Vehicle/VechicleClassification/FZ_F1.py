from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class FZ_F1(McwgVehicles):
    def name(self):
        return "Yamaha Fz-F1"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "180Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{1,30,000}Rs - On Road Price"
