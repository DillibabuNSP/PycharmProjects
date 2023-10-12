class VehicleList:
    vehicleList = []

    def addList(self, list):
        VehicleList.vehicleList.append(list)

    def showList(self):
        for mylist in VehicleList.vehicleList:
            print(f"Name of the Vehicle - {mylist.name()}")
            print(f"Vehicle type - {mylist.type()}")
            print(f'Speed of the Vehicle - {mylist.speed()}')
            print(f"Seating Capacity of the vehicle - {mylist.seating_Capacity()}")
            print(f'Price of the Vehicle - {mylist.price()}')
