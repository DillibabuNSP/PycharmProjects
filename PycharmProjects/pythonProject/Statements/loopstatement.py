mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Program 1
for num in mylist:
    if num % 2 == 0:
        print(f'Even number is: {num}')
    else:
        print(f'odd number is: {num}')

# Program 2
n = int(input('Enter the number'))
for i in mylist:
    c = n * i
    print(f'{n} * {i} = {c}')

#  Program 3
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum)

print(list_sum)

# Program 3 - Tuple's in List
my_list = [(1, 2), (3, 4), (5, 6), (7, 8), 9, 10]  # cannot unpack non-iterable int object
for num in my_list:
    print(num)

my_list1 = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
for (a, b) in my_list1:
    print(a)
    print(b)

# program 4 - Dictionaries
d = {'k1': 'Atmecs', 'k2': 'Technologies', 'k3': 'pvt', 'k4': 'ltd'}
for key, value in d.items():
    print(key, value)

# program 5
for i in range(10):
    print(i, end=' ')

# program 6
n = int(input("Enter the number "))
for i in range(1, 11):
    c = n * i
    print(n, "*", i, "=", c)

# program 7
n = int(input("Enter the number "))
for i in range(2, n, 2):
    print(i)

# program 8
rows = int(input("Enter the rows:"))
for i in range(0, rows + 1):
    for j in range(i):
        print("*", end='')
    print()

# program 9
rows = int(input("Enter the rows"))
for i in range(0, rows + 1):
    for j in range(i):
        print(i, end='')
    print()
