# if else Statement
loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')
elif loc == "Bank":
    print('Welcome to the bank!')
elif loc == 'store':
    print('welcome to the store')
else:
    print('Where are you?')

# program 2
a = int(input("Enter a? "))
b = int(input("Enter b? "))
c = int(input("Enter c? "))
if a > b and a > c:
    print("a is largest")
if b > a and b > c:
    print("b is largest")
if c > a and c > b:
    print("c is largest")

# Program 3
age = int(input("Enter your age? "))
if age >= 18:
    print("You are eligible to vote !!")
else:
    print("Sorry! you have to wait !!")
