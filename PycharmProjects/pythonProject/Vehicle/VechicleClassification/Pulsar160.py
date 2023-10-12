from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class Pulsar160(McwgVehicles):
    def name(self):
        return "Pulsar 160"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "140Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{1,14,000}Rs - On Road Price"
