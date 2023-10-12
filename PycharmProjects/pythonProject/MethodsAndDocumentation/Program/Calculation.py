def add(numb1, numb2):
    result = numb1 + numb2
    return result


def sub(numb1, numb2):
    if numb1 > numb2:
        result = numb1 - numb2
    else:
        if numb2 > numb1:
            result = numb2 - numb1
    return result


def multiply(numb1, numb2):
    result = numb1 * numb2
    return result


def divide(numb1, numb2):
    quotient = numb1 / numb2
    remainder = numb1 % numb2
    result = f'Q= {quotient} and R= {remainder}'
    return result


number1 = int(input("First Number:  "))
action = input("")
number2 = int(input("Second Number: "))
if action == '+':
    print(add(number1, number2))

elif action == '-':
    print(sub(number1, number2))

elif action == '*':
    print(multiply(number1, number2))

elif action == '/':
    print(divide(number1, number2))
