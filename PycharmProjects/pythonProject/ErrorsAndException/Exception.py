def ask():
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break

    print('Thank you, your number squared is: ', n ** 2)


ask()


# Zero Division Error
x = 5
y = 0
try:
    z = x / y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')
print('==========================')


# except statement using with exception variable
try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a / b
    print("a/b = %d" % c)
except Exception:
    print("can't divide by zero")
    print(Exception)
else:
    print("Hi I am else block")
print('==========================')


try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a / b
    print("a/b = %d" % c)

except Exception as e:
    print("can't divide by zero")
    print(e)
else:
    print("Hi I am else block")
print('==========================')


try:
    fileptr = open("file.txt", "r")
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    fileptr.close()
print('==========================')


# try...finally block
try:
    fileptr = open("file2.txt", "r")
    try:
        fileptr.write("Hi I am good")
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error")

print('==========================')


# Raising exceptions
try:
    age = int(input("Enter the age:"))
    if age < 18:
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("The age is not valid")
print('==========================')


# Raise the exception with message
try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        raise ValueError("That is  a negative number!")
except ValueError as e:
    print(e)

print('==========================')


# Custom Exception
class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
    print("Received error:", ae.data)
