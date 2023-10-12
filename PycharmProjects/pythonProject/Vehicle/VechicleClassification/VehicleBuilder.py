from Vehicle.VechicleClassification.FZS import FZS
from Vehicle.VechicleClassification.FZ_F1 import FZ_F1
from Vehicle.VechicleClassification.GixxerRE import GixxerRE
from Vehicle.VechicleClassification.GixxerSE import GixxerSE
from Vehicle.VechicleClassification.Himalayan import Himalayan
from Vehicle.VechicleClassification.HondaShine import HondaShine
from Vehicle.VechicleClassification.Hornet import Hornet
from Vehicle.VechicleClassification.Platinum import Platinum
from Vehicle.VechicleClassification.Pulsar160 import Pulsar160
from Vehicle.VechicleClassification.Pulsar180 import Pulsar180
from Vehicle.VechicleClassification.Pulsar200Ns import Pulsar200Ns
from Vehicle.VechicleClassification.R15_V4 import R15_V4
from Vehicle.VechicleClassification.ThunderBird import ThunderBird
from Vehicle.VechicleClassification.VehicleList import VehicleList


class VehicleBuilder:
    class OrderBuilder:

        def wishList(self):
            Vbs = VehicleList()
            print(" Enter the Type Of the Vehicle ")
            print("============================")
            print("        1. MCWG       ")
            print("        2. LMV   ")
            print("        3. HMV   ")
            print("        4. Trailers   ")
            print("        5. Exit            ")
            print("============================")

            customersChoice = int(input(" Enter the type of the Vehicle : "))
            match customersChoice:
                case 1:
                    print("You have selected MCWG")
                    print("\n\n")

                    print(" Enter the types of MCWG ")
                    print("------------------------------")
                    print("        1.GearBike        ")
                    print("        2.Scooty        ")
                    print("        3.Exit            ")
                    print("------------------------------")

                    gearBike = int(input("Enter the types of MCWG_ "))

                    match gearBike:
                        case 1:
                            print("You have selected Gear Vehicle")

                            print("Select the Brand of Vehicle you need - ")
                            print("------------------------------------")
                            print("     Bajaj ")
                            print("     Honda ")
                            print("     Royal Enfield ")
                            print("     Suzuki ")
                            print("     Yamaha ")
                            print("------------------------------------")
                            brand = int(input("Select the Brand of Vehicle you need -  "))

                            match brand:
                                case "Bajaj":
                                    print("You have selected Bajaj")

                                    print("Select the Brand of Vehicle you need - ")
                                    print("------------------------------------")
                                    print("     Pulsar 200Ns ")
                                    print("     Pulsar 180 ")
                                    print("     Pulsar 160 ")
                                    print("     Platinum")
                                    print("------------------------------------")
                                    brandType = int(input("Select the Vehicle -  "))
                                    match brandType:
                                        case "Pulsar 200Ns":
                                            Vbs.addList(Pulsar200Ns())

                                        case "Pulsar 180":
                                            Vbs.addList(Pulsar180())

                                        case "Pulsar 160":
                                            Vbs.addList(Pulsar160())

                                        case "Platinum":
                                            Vbs.addList(Platinum())
                                case "Honda":
                                    print("You have selected Honda")

                                    print("Select the Brand of Vehicle you need - ")
                                    print("------------------------------------")
                                    print("     Honda Shine ")
                                    print("     Hornet ")
                                    print("------------------------------------")
                                    brandType = int(input("Select the Vehicle -  "))
                                    match brandType:
                                        case "Honda Shine":
                                            Vbs.addList(HondaShine())

                                        case "Hornet":
                                            Vbs.addList(Hornet())
                                case "Royal Enfield":
                                    print("You have selected Royal Enfield")

                                    print("Select the Brand of Vehicle you need - ")
                                    print("------------------------------------")
                                    print("     ThunderBird ")
                                    print("     Himalayan ")
                                    print("------------------------------------")
                                    brandType = int(input("Select the Vehicle -  "))
                                    match brandType:
                                        case "ThunderBird":
                                            Vbs.addList(ThunderBird())

                                        case "Himalayan":
                                            Vbs.addList(Himalayan())

                                case "Suzuki":
                                    print("You have selected Suzuki")

                                    print("Select the Brand of Vehicle you need - ")
                                    print("------------------------------------")
                                    print("     Gixxer SE ")
                                    print("     Gixxer RE ")
                                    print("------------------------------------")
                                    brandType = int(input("Select the Vehicle -  "))
                                    match brandType:
                                        case "Gixxer SE":
                                            Vbs.addList(GixxerSE())

                                        case "Gixxer RE":
                                            Vbs.addList(GixxerRE())

                                case "Yamaha":
                                    print("You have selected Yamaha")

                                    print("Select the Brand of Vehicle you need - ")
                                    print("------------------------------------")
                                    print("     R15 Version-4 ")
                                    print("     FZ-S     ")
                                    print("     Fz-F1    ")
                                    print("------------------------------------")
                                    brandType = int(input("Select the Vehicle -  "))
                                    match brandType:
                                        case "R15 Version-4":
                                            Vbs.addList(R15_V4())

                                        case "FZS":
                                            Vbs.addList(FZS())

                                        case "Fz-F1":
                                            Vbs.addList(FZ_F1())

                        case 2:
                            print("You selected Without Gear Vehicle")

                            print("Select the Brand of Vehicle you need - ")
                            print("------------------------------------")
                            print("     Bajaj ")
                            print("     Honda ")
                            print("     Suzuki ")
                            print("     Yamaha ")
                            print("------------------------------------")
                            brand = int(input("Select the Brand of Vehicle you need -  "))
                            match brand:
                                case Suzuki:
                                    Vbs.addList()

                case _:
                    exit()

            return Vbs
