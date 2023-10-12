def display(data_):
    print(checkingData.check_input(data_))


class checkingData:
    data_dic = {'String': [], 'Boolean': [], 'Float': [], 'int': []}

    @staticmethod
    def check_input(data_list):
        for element in data_list:
            if element:
                checkingData.data_dic["int"].append(int(element))
            elif element == "True":
                checkingData.data_dic["Boolean"].append(bool(element))
            elif element:
                checkingData.data_dic["String"].append(str(element))
            elif element:
                checkingData.data_dic["Float"].append(float(element))
        return checkingData.data_dic


if __name__ == "__main__":
    data = [input("Enter the Data: ").split(",")]
    check = checkingData()
    display(data)
