mytuple = ('apple', 'banana', 'cherry')
# tuples are used to store multiple items in a single variable
print(mytuple)

# tuples are immutable, meaning you cannot change their values
# you can create a tuple with one item by adding a comma after the item
mytuple2 = ('apple',)

# you can also create a tuple without parentheses
mytuple3 = 'apple', 'banana', 'cherry'


print(mytuple3)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(thistuple))  # length of the tuple
print(type(mytuple))  # type of the tuple
print(mytuple[1])  # type of the tuple with one item

thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))


tuple1 = ('apple', 'banana', 'cherry')
tuple2 = (1, 2, 3, 4, 5, 6, 7)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
print(type(thistuple))

thistuple = ('apple', 'banana', 'cherry')
print(thistuple[-1])  # negative indexing


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])  # from the beginning to index 4 (not included

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])  # from index 2 to the end

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  # negative indexing from -4 to -1 (not included)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the tuple")
# check if an item exists in a tuple

x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)

print(x)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


thistuple = ("apple", "banana", "cherry")
y = ('orange',)
thistuple += y
print(thistuple)


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)
print(thistuple)


thistuple = ("apple", "banana", "cherry")
del thistuple
# int(thistuple)  # this will raise an error because the tuple no longer exists

fruits = ('apple', 'banana', 'cherry')

(green, yellow, red) = fruits
print(green)  # apple
print(yellow)  # banana
print(red)  # cherry
print('----------------------------------')
# unpacking a tuple

fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
(green, yellow, *red) = fruits
print(green)  # apple
print(yellow)  # banana
print(red)  # ['cherry', 'strawberry', 'raspberry']


thistuple = ('apple', 'banana', 'cherry')
for i in range(len(thistuple)):
    print(thistuple[i])
# loop through a tuple using index numbers

thistuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
# loop through a tuple using a while loop


tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
# joining two tuples

fruits = ('apple', 'banana', 'cherry')
mytuple = fruits * 2
print(mytuple)


# tuple methods


# count()    Returns the number of times a specified value occurs in a tuple
thistuple = (1, 2, 3, 2, 2, 4, 5)
x = thistuple.count(2)
print(x)  # 3
# index()    Searches the tuple for a specified value and returns the position of where it was found
thistuple = (1, 2, 3, 4, 5)
x = thistuple.index(4)
print(x)  # 3

# ===============================
# EK BİLGİLER - TUPLES
# ===============================
# Tuple Avantajları:
# 1. Listelerden daha hızlıdır (immutable olduğu için)
# 2. Değişmemesi gereken verileri korur
# 3. Dictionary key olarak kullanılabilir (listeler kullanılamaz)
# 4. Daha az bellek kullanır

import sys
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
print(f"Liste boyutu: {sys.getsizeof(my_list)} bytes")
print(f"Tuple boyutu: {sys.getsizeof(my_tuple)} bytes")

# Named Tuples - daha okunabilir tuple'lar
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
person1 = Person('Ali', 25, 'İstanbul')
print(person1.name)  # Ali
print(person1.age)   # 25
print(person1.city)  # İstanbul

# Tuple unpacking - gelişmiş
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")

# Tuple'da swap işlemi
a, b = 5, 10
print(f"Önce: a={a}, b={b}")
a, b = b, a  # Swap
print(f"Sonra: a={a}, b={b}")

# Tuple comprehension yok, generator expression var
gen = (x**2 for x in range(5))  # Bu bir generator
print("Generator:", gen)
print("Generator to tuple:", tuple(gen))

# Tuple'ları dictionary key olarak kullanma
locations = {}
locations[(41.0082, 28.9784)] = "İstanbul"
locations[(39.9334, 32.8597)] = "Ankara"
print("Koordinat sözlüğü:", locations)

# Çoklu return değerleri
def calculate_stats(numbers):
    return sum(numbers), len(numbers), sum(numbers)/len(numbers)

total, count, average = calculate_stats([1, 2, 3, 4, 5])
print(f"Toplam: {total}, Adet: {count}, Ortalama: {average}")

# End of 14_tuples.py
