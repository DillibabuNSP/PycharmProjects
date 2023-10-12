data_dic = {'String': [], 'Boolean': [], 'Float': [], 'int': []}


def check_input(data_list):
    for element in data_list:
        if element:
            data_dic["int"].append(int(element))
        elif element == "True":
            data_dic["Boolean"].append(bool(element))
        elif element:
            data_dic["String"].append(str(element))
        elif element:
            data_dic["Float"].append(float(element))


if __name__ == "__main__":
    data = [input("Enter the Data: ").split(",")]
    check_input(data)
    print(data_dic)
