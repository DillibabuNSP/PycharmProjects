from BillCounter.Bill.ExtraLargeCheezePizza import ExtraLargeCheezePizza
from BillCounter.Bill.ExtraLargeMasalaPizza import ExtraLargeMasalaPizza
from BillCounter.Bill.ExtraLargeNonVegPizza import ExtraLargeNonVegPizza
from BillCounter.Bill.ExtraLargeOnionPizza import ExtraLargeOnionPizza
from BillCounter.Bill.LargeCheezePizza import LargeCheezePizza
from BillCounter.Bill.LargeCoke import LargeCoke
from BillCounter.Bill.LargeMasalaPizza import LargeMasalaPizza
from BillCounter.Bill.LargeNonVegPizza import LargeNonVegPizza
from BillCounter.Bill.LargeOnionPizza import LargeOnionPizza
from BillCounter.Bill.LargePepsi import LargePepsi
from BillCounter.Bill.MediumCheezePizza import MediumCheezePizza
from BillCounter.Bill.MediumCoke import MediumCoke
from BillCounter.Bill.MediumMasalaPizza import MediumMasalaPizza
from BillCounter.Bill.MediumNonVegPizza import MediumNonVegPizza
from BillCounter.Bill.MediumOnionPizza import MediumOnionPizza
from BillCounter.Bill.MediumPepsi import MediumPepsi
from BillCounter.Bill.OrderedItems import OrderedItems
from BillCounter.Bill.SmallCheezePizza import SmallCheezePizza
from BillCounter.Bill.SmallCoke import SmallCoke
from BillCounter.Bill.SmallMasalaPizza import SmallMasalaPizza
from BillCounter.Bill.SmallNonVegPizza import SmallNonVegPizza
from BillCounter.Bill.SmallOnionPizza import SmallOnionPizza
from BillCounter.Bill.SmallPepsi import SmallPepsi


class OrderBuilder:

    def preparePizza(self):
        itemsOrder = OrderedItems()
        print(" Enter the choice of Pizza ")
        print("============================")
        print("        1. Veg-Pizza       ")
        print("        2. Non-Veg Pizza   ")
        print("        3. Exit            ")
        print("============================")

        pizzaAndColdDrinkChoice = int(input(" Enter the choice of Pizza : "))
        match pizzaAndColdDrinkChoice:
            case 1:
                print("You ordered Veg Pizza")
                print("\n\n")

                print(" Enter the types of Veg-Pizza ")
                print("------------------------------")
                print("        1.Cheeze Pizza        ")
                print("        2.Onion Pizza        ")
                print("        3.Masala Pizza        ")
                print("        4.Exit            ")
                print("------------------------------")

                vegPizzaChoice = int(input("Enter the types of Veg-Pizza: "))

                match vegPizzaChoice:
                    case 1:
                        print("You ordered Cheeze Pizza")

                        print("Enter the cheeze pizza size")
                        print("------------------------------------")
                        print("    1. Small Cheeze Pizza ")
                        print("    2. Medium Cheeze Pizza ")
                        print("    3. Large Cheeze Pizza ")
                        print("    4. Extra-Large Cheeze Pizza ")
                        print("------------------------------------")
                        cheezePizzaSize = int(input("Enter the cheeze pizza size: "))

                        match cheezePizzaSize:
                            case 1:
                                itemsOrder.addItems(SmallCheezePizza())

                            case 2:
                                itemsOrder.addItems(MediumCheezePizza())

                            case 3:
                                itemsOrder.addItems(LargeCheezePizza())

                            case 4:
                                itemsOrder.addItems(ExtraLargeCheezePizza())

                    case 2:
                        print("You ordered Onion Pizza")

                        print("Enter the Onion pizza size")
                        print("----------------------------------")
                        print("    1. Small Onion Pizza ")
                        print("    2. Medium Onion Pizza ")
                        print("    3. Large Onion Pizza ")
                        print("    4. Extra-Large Onion Pizza ")
                        print("----------------------------------")

                        onionPizzaSize = int(input("Enter the Onion pizza size: "))
                        match onionPizzaSize:

                            case 1:
                                itemsOrder.addItems(SmallOnionPizza())

                            case 2:
                                itemsOrder.addItems(MediumOnionPizza())

                            case 3:
                                itemsOrder.addItems(LargeOnionPizza())

                            case 4:
                                itemsOrder.addItems(ExtraLargeOnionPizza())

                    case 3:
                        print("You ordered Masala Pizza")

                        print("Enter the Masala pizza size")
                        print("------------------------------------")
                        print("    1. Small Masala Pizza ")
                        print("    2. Medium Masala Pizza ")
                        print("    3. Large Masala Pizza ")
                        print("    4. Extra-Large Masala Pizza ")
                        print("------------------------------------")

                        masalaPizzaSize = int(input("Enter the Masala pizza size:"))
                        match masalaPizzaSize:
                            case 1:
                                itemsOrder.addItems(SmallMasalaPizza())

                            case 2:
                                itemsOrder.addItems(MediumMasalaPizza())

                            case 3:
                                itemsOrder.addItems(LargeMasalaPizza())

                            case 4:
                                itemsOrder.addItems(ExtraLargeMasalaPizza())

            case 2:
                print("You ordered Non-Veg Pizza")
                print("\n\n")

                print("Enter the Non-Veg pizza size")
                print("------------------------------------")
                print("    1. Small Non-Veg  Pizza ")
                print("    2. Medium Non-Veg  Pizza ")
                print("    3. Large Non-Veg  Pizza ")
                print("    4. Extra-Large Non-Veg  Pizza ")
                print("------------------------------------")

                nonVegPizzaSize = int(input("Enter the Non-Veg pizza size: "))
                match nonVegPizzaSize:
                    case 1:
                        itemsOrder.addItems(SmallNonVegPizza())

                    case 2:
                        itemsOrder.addItems(MediumNonVegPizza())

                    case 3:
                        itemsOrder.addItems(LargeNonVegPizza())

                    case 4:
                        itemsOrder.addItems(ExtraLargeNonVegPizza())

            case _:
                exit()

        print(" Enter the choice of ColdDrink ")
        print("============================")
        print("        1. Pepsi            ")
        print("        2. Coke             ")
        print("        3. Exit             ")
        print("============================")

        coldDrink = int(input("Enter the choice of ColdDrink: "))

        match coldDrink:
            case 1:
                print("You ordered Pepsi ")

                print("Enter the  Pepsi Size ")
                print("------------------------")
                print("    1. Small Pepsi ")
                print("    2. Medium Pepsi ")
                print("    3. Large Pepsi ")
                print("------------------------")

                pepsiSize = int(input("Enter the  Pepsi Size: "))
                match pepsiSize:
                    case 1:
                        itemsOrder.addItems(SmallPepsi())

                    case 2:
                        itemsOrder.addItems(MediumPepsi())

                    case 3:
                        itemsOrder.addItems(LargePepsi())

            case 2:
                print("You ordered Coke")

                print("Enter the Coke Size")
                print("------------------------")
                print("    1. Small Coke ")
                print("    2. Medium Coke  ")
                print("    3. Large Coke  ")
                print("    4. Exit ")
                print("------------------------")

                cokeSize = int(input("Enter the Coke Size: "))
                match cokeSize:
                    case 1:
                        itemsOrder.addItems(SmallCoke())

                    case 2:
                        itemsOrder.addItems(MediumCoke())

                    case 3:
                        itemsOrder.addItems(LargeCoke())

            case _:
                exit()

        return itemsOrder
