from Vehicle.VechicleClassification.McwgVehicles import McwgVehicles


class Pulsar200Ns(McwgVehicles):
    def name(self):
        return "Pulsar 200Ns"

    def type(self):
        return "Motor Cycle"

    def speed(self):
        return "250Km"

    def seating_Capacity(self):
        return "2 Persons"

    def price(self):
        return f"{1,54,000}Rs - On Road Price"
