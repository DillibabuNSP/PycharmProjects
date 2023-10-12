# Program 1
from random import shuffle, randint

x = 0

while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1

# Program 2
x = 0

while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1

else:
    print('All Done!')

# Program 3 - Continue
x = 0

while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1
    if x == 3:
        print('x==3')
    else:
        print('continuing...')
        continue

# Program 4
# prints all letters except 'a' and 't'
i = 0
str1 = 'Atmecs Technologies Pvt Ltd'

while i < len(str1):
    if str1[i] == 'o' or str1[i] == 't':
        i += 1
        continue
    print('Current Letter :', str1[i])
    i += 1

# Program 5 - break
x = 0

while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1
    if x == 3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue

# Program 6
i = 0
str1 = 'Atmecs Technologies Pvt Ltd'

while i < len(str1):
    if str1[i] == 't':
        i += 1
        break
    print('Current Letter :', str1[i])
    i += 1

# Program 7 - pass statement

str1 = 'Atmecs Technologies Pvt Ltd'
i = 0

while i < len(str1):
    i += 1
    pass
print('Value of i :', i)

# Program  8
index_count = 0
word = 'Atmecs Technologies Pvt Ltd'
for letter in word:
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1

# Program 9 - enumerate
word = 'Atmecs Technologies Pvt Ltd'
for letter in enumerate(word):
    print(letter)

# Program 10 - zip
mylist1 = [1, 2, 3, 4]
mylist2 = ['Atmecs', 'Technologies', 'Pvt', 'Ltd']
for item1, item2 in zip(mylist1, mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1, item2))

# Program 11 - useful operators
mylist = [10, 20, 30, 40, 100]
print(min(mylist))
print(max(mylist))

shuffle(mylist)
print(mylist)

print(randint(0, 100))

input("enter something")

# Program 12 - Comprehensions
celsius = [0, 10, 20.1, 34.5]

fahrenheit = [((9 / 5) * temp + 32) for temp in celsius]

print(fahrenheit)
