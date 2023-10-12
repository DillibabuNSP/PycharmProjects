import random


def simple_Gen():
    for x in range(3):
        yield x


for num in simple_Gen():
    print(num)

g = simple_Gen()
print(next(g))
print(next(g))
print(next(g))

my_list = [1, 2, 3, 4, 5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

# iter() function
s = 'hello'

s = iter(s)

print(next(s))
print(next(s))
print(next(s))
print(next(s))


##############################################################
def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)
