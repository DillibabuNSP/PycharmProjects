from collections import defaultdict, namedtuple

from AdvancedPythonModule.Collections.collection import letters

list(letters)
d = {'word': 2}
print(d)
d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['WRONG KEY!'])

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5, breed='Husky', name='sam')
print(type(sammy))
print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy.name)
