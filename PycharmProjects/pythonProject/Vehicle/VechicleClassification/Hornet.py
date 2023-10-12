from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class Hornet(McwgVehicles):
    def name(self):
        return "Honda Hornet"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "160Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{1,34,000}Rs - On Road Price"
