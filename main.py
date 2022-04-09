# https://www.youtube.com/watch?v=C-gEQdGVXbk

# 1
condition = True
y = 1 if condition else 0
print(y)

# 2
with open("file.txt", "r") as f:
    content  = f.read()
words = content.split(" ")
print(words)

# 3
names = ['a', 'b', 'c']
data = enumerate(names, start=1)
print(data)
for index, name in data:
    print(index, name)

# 4
names = ["Spider Man", "Superman", "Batman"]
heroes = ["Peter", "Clark", "Wayne"]
universes = ["Marvel", "DC", "DC"]

for name, hero, universe in zip(names, heroes, universes):
    print(name, hero, universe)

# 5
for data in zip(names, heroes, universes):
    name, hero, universe = data
    print(name, hero, universe)

# 6
a,*b,c = (1,2,3,4,5,6)
print(a, b, c)

# 7
a,b,*c,d = (1,2,3,4,5,6)
print(a, b, c, d)

# 8 
class Person():
    pass

person = Person()

setattr(person, 'key1', 'val1')

print(getattr(person, 'key1'))

# 9
person = Person()
person_info = {'first':'Corey', 'last':'Schafer'}

for key, val in person_info.items():
    setattr(person, key, val)

for key in person_info.keys():
    print(getattr(person, key))

# 10 - list comprehension
squares = []
for i in range(10):
    squares.append(i*i)
print(squares)

squares = [i*i for i in range(11)]
print(squares)

# 11 - Sorting array of dicts
data = [
    {"name":"Jon", "age": 12},
    {"name":"Max", "age": 21},
    {"name":"Cameron", "age": 89},
    {"name":"Josh", "age": 10},
    {"name":"Paulie", "age": 13},
]

sorted_data = sorted(data, key= lambda x: x["age"])

print("Ordered by Age:")
for i in sorted_data:
    print(i)

sorted_data = sorted(data, key= lambda x: x["name"])

print("Ordered by Name:")
for i in sorted_data:
    print(i)

# 12 - Save memory with generators
import sys

my_list = [i for i in range(10_000)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")

# 😱 insane.
my_list = (i for i in range(10_000))
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")

# 13 - dicts - don't thows if key not in dict

my_dict = {"item": "football", "price": 10.00}
my_dict.setdefault("count", 0)
count = my_dict.get("count", 0)
print(my_dict)

# 14 - Count with collections.Counter

from collections import Counter

my_list = [10, 10, 10, 5, 4, 9, 9]
counter = Counter(my_list)

moster_common = counter.most_common(1)
print(moster_common[0][0])

# 15 - Merge dicts (3.5+)

d1 = {"name": "Alex"}
d2 = {"age": 20}

merged = {**d1, **d2}

print(merged)

# 16
if "r" in ["r", "g", "b"]: print("check")