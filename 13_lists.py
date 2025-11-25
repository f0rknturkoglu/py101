thislist = ["apple", "banana", "cherry"]
print(thislist)
'''
ordered
changeable
allow duplicate members
list length is unlimited

'''
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]  # farklı veri tipleri

print(type(list1))

# using list constructor
# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)
print(type(thislist))

# python collections - arrays
# lists
# tuples
# sets
# dictionaries


# acess list items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])  # banana
print(thislist[-1])  # mango
print(thislist[2:5])  # ['cherry', 'orange', 'kiwi']
print(thislist[:4])  # ['apple', 'banana', 'cherry', 'orange']
print(thislist[2:])  # ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[-4:-1])  # ['kiwi', 'melon', 'mango']
# check if item exists
if "apple" in thislist:
    print("yes, 'apple' is in the fruits list")

 # change list items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist[1:3] = ["watermelon", "kiwi"]
print(thislist)
thislist.insert(2, "banana")
print(thislist)
thislist.append("orange")
print(thislist)
thislist.extend(["mango", "grapes"])
print(thislist)
tropical = ["pineapple", "papaya", "passionfruit"]
thislist.extend(tropical)
print(thislist)
for x in tropical:
    thislist.append(x)
print(thislist)

thislist = ['apple', 'banana', 'cherry']
for x in thislist:
    print(x)


thislist = ['apple', 'banana', 'cherry']
for i in range(len(thislist)):
    print(thislist[i])


thislist = ['apple', 'banana', 'cherry']
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1


thislist = ['apple', 'banana', 'cherry']
[print(x) for x in thislist]


fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)


fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits if "a" in x]
print(newlist)
# newlist = [expression for item in iterable if condition == True]


thislist = ["apple", "banana", "cherry"]
thislist.sort()
print(thislist)

thislist = [1, 2, 3, 4, 55, 332, 22, 3, 77]
thislist.sort()
print(thislist)


thislist = [1, 2, 3, 4, 55, 332, 22, 3, 77]
thislist.sort(reverse=True)
print(thislist)


def myFunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myFunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


thislist = ["BBanana", "Orange", "kiwi", "cherry"]
thislist.sort(key=str.lower)  # case insensitive sort
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


thislist = ['apple', 'banana', 'orange']
mylist = thislist.copy()
print(mylist)


thislist = ['apple', 'banana', 'orange']
mylist = list(thislist)  # another way to copy a list
print(mylist)

thislist = ['apple', 'banana', 'orange']
mylist = thislist[:]  # another way to copy a list
print(mylist)

# JOIN Two list

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list3 = list1 + list2  # using + operator
print(list3)

for x in list2:
    list1.append(x)  # using append() method

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)  # using extend() method
print(list1)


# LİST METHODS

# append() - Adds an element at the end of the list
# clear() - Removes all the elements from the list
# copy() - Returns a copy of the list
# count() - Returns the number of elements with the specified value
# extend() - Adds the elements of a list (or any iterable), to the end of the current list
# index() - Returns the index of the first element with the specified value
# insert() - Adds an element at the specified position
# pop() - Removes the element at the specified position
# remove() - Removes the first item with the specified value
# reverse() - Reverses the order of the list
# sort() - Sorts the list

# ===============================
# EK BİLGİLER - LISTS
# ===============================
# List Comprehension - Gelişmiş Örnekler
squares = [x**2 for x in range(10)]
print("Kareler:", squares)

# Koşullu list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Çift sayıların kareleri:", even_squares)

# İç içe list comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix:", matrix)

# Liste metodları - Gelişmiş kullanım
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("5 sayısı kaç kez geçiyor:", numbers.count(5))  # 3
print("İlk 5'in index'i:", numbers.index(5))  # 4

# Liste dilimleme (slicing) - Gelişmiş
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Tersten:", fruits[::-1])
print("İkişer atlayarak:", fruits[::2])
print("Son 3 eleman:", fruits[-3:])

# Liste kopyalama - Shallow vs Deep copy
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()  # Sığ kopya
deep = copy.deepcopy(original)  # Derin kopya

original[0][0] = 999
print("Original:", original)  # [[999, 2], [3, 4]]
print("Shallow:", shallow)   # [[999, 2], [3, 4]] - etkilendi!
print("Deep:", deep)         # [[1, 2], [3, 4]] - etkilenmedi!

# zip() fonksiyonu ile listeler
names = ['Ali', 'Veli', 'Ayşe']
ages = [25, 30, 28]
cities = ['İstanbul', 'Ankara', 'İzmir']

combined = list(zip(names, ages, cities))
print("Birleştirilmiş:", combined)

# enumerate() ile index ve değer
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# filter() ve map() fonksiyonları
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
squared = list(map(lambda x: x**2, numbers))
print("Çift sayılar:", even)
print("Kareler:", squared)
