print('babu')
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)

# Module or 'Mod' Operators
# Odd or Even which represents 1 its odd and Which represents 0 its even
print(20 % 2)
print(23 % 2)

# Floor division
print(5 // 2)
print(0.1 + 0.2 - 0.3)

# Variables
a = 10
print(a)
a = 25
print(a)
print(type(a))
a = "dog"
print(type(a))

# String
print(len('babu'))

# Indexing
words = 'Atmecs'
print(words[-1])
print(words[-3])

# Slicing
print(words[1:])  # output = tmecs

# negative Indexing slicing
print(words[::2])
print(words[::-4])
print(words[1:5:2])  # [Start:Stop:Step]
print(words[::-1])  # Reversible

# String Properties and Methods
company_name = words + ' Technologies Pvt Ltd.'
print(company_name)
print(company_name.upper())

# Print Formatting
print('Atmecs {2} {0} {1}'.format('Ltd', 'Pvt', 'Technologies'))

result = 234 / 678
print(result)
print('The Result was {r:1.3f}'.format(r=result))

name = 'Babu'
print(f"My name is {name}, and i'm working in {company_name}")

my_list = ['Atmecs', 'Technologies', 'Pvt']
print(my_list)
my_list.append('Ltd')
print(my_list)
print(my_list.pop())
print(my_list)

# Dictionary
price_list = {'Iphone': 65000, 'Redmi': 20000, 'Realme': 16000, '1Plus': {'Nord': 24000},
              '1plus 7T': [35000, 38000, 32000]}
print(price_list['1Plus']['Nord'])

print(price_list['1plus 7T'])

one_plus = price_list['1plus 7T']
print(one_plus[2])
print(price_list.items())
# phone_list = {3400: '1Plus', 16000: 'Realme'}
# print(phone_list[34000])    // results invalid

# Tuples
t_list = (1, 2, 'Atmecs')
print(t_list.count(2))
print(t_list.index('Atmecs'))

# Sets
my_num = set()
my_num.add(224)
my_num.add('Atmecs')
print(my_num)
my_set = [1, 1, 1, 2, 2, 2, 3, 3, 3]
print(set(my_set))

print(2 == 2)
print(2 != 2)
