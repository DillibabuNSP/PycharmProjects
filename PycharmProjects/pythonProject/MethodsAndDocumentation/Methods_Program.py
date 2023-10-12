# Methods
import string

my_list = [1, 2, 3]

my_list.append(4)
my_list.append(3)
print(my_list)

print(my_list.count(3))

my_list.pop()
print(my_list)

my_list.insert(3, 3)
print(my_list)


# args
def myfunc(*args):
    return sum(args) * .05


print(myfunc(40, 60, 20))


# Args and Kwargs
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


myfunc('eggs', 'spam', fruit='cherries', juice='orange')


# kwargs
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(
            f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is
        # unfamiliar
    else:
        print("I don't like fruit")


myfunc(fruit='pineapple')


# To find upper and lowercase
def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])


up_low("Atmecs Technologies Pvt Ltd")


# To find unique in a list
def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x


print(unique_list([(1, 1), (1, 1), (2, 2), (3, 3), (3, 3), (4, 5)]))


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaSet = set(alphabet)
    str1 = str1.replace("", '')
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphaSet


print(ispangram("The quick brown fox jumps over the lazy dog"))


def vol(rad):
    result = (4 / 3) * 3.14 * rad ** 3
    return result


print(vol(2))


def ran_check(num, low_num, high_num):
    if num in range(low_num, high_num + 1):
        print(f'{num} is in the range between {low_num} and {high_num}')


ran_check(5, 2, 7)


def ran_bool(num, low_num, high_num):
    return num in range(low_num, high_num + 1)


print(ran_bool(3, 1, 10))

