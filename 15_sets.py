import time
myset = {'apple', 'banana', 'cherry'}
# sets are used to store multiple items in a single variable

# set is one of 4 built-in data types in python used to store collections of data, the other 3 are list tupler and diyt

# set is a collectio which is unorderec unchangable and unindexed:


# * Note: Set items are unchangeable, but you can remove items and add new items.


thisset = {'a', 'b', 'c'}

print(thisset)
# duplicates not allowed


thisset = {'apple', 'banana', 'cherry', 'apple'}
print(thisset)  # duplicate values will be ignored


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


# True aand 1 are considered the same value in sets and are treated ass duplicates

# false and 0 too
thisset = {'apple', 'banana', 'cherry'}

print(len(thisset))


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3, 3, 3, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
print(type(set1))


# the set() constructor
thisset = set(('apple', 'banana', 'cherry'))
print(thisset)

# a set can contain different data types

set1 = {"abc", 34, True, 40, "male"}


# access set items

thisset = {'apple', 'banana', 'cherry'}
print('banana' in thisset)


thisset = {'apple', 'banana', 'cherry'}
print('banana' not in thisset)


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {'apple', 'banana', 'cherry'}
tropical = ['pineapple', 'mango', 'papaya']
thisset.update(tropical)


print(thisset)


thisset = {'apple', 'banana', 'cherry'}
thisset.remove('banana')

print(thisset)

thisset = {"apple", "banana", "cherry"}

# get an arbitrary element without assigning the result of a function that may be marked as returning None
x = next(iter(thisset))
thisset.remove(x)
print(x)
print(thisset)

# JOIN SETS
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# keep only the duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)
print(z)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
'''

The difference_update() method will also keep the items
 from the first set that are not in the other set,
   but it will change the original set instead of 
   returning a new set.

'''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)


# FROZEN SETS
# frozenset is a set that cannot be changed
thisset = frozenset({"apple", "banana", "cherry"})
print(thisset)
# thisset.add("orange")  # will raise an error
print(thisset)
# thisset.remove("banana")  # will raise an error
# print(thisset)
# thisset.clear()  # will raise an error
print(thisset)
# del thisset  # will delete the frozenset


# SET METHODS
thisset = {'apple', 'banana', 'cherry'}
print(thisset.copy())  # returns a copy of the set
print(thisset.clear())  # removes all the elements from the set
print(thisset)  # the set is now empty
thisset = {'apple', 'banana', 'cherry'}
print(thisset.pop())  # removes and returns an arbitrary element from the set
print(thisset)  # the set after popping an element
# returns True if two sets have no elements in common
print(thisset.isdisjoint({'orange', 'kiwi'}))
# returns True if all elements of the set are in the specified set
print(thisset.issubset({'apple', 'banana', 'cherry', 'orange'}))
# returns True if the set contains all elements of the specified set
print(thisset.issuperset({'apple', 'banana'}))
# returns a set with the symmetric differences of two sets
print(thisset.symmetric_difference({'banana', 'kiwi', 'mango'}))
# updates the set with the symmetric differences of two sets
print(thisset.symmetric_difference_update({'banana', 'kiwi', 'mango'}))
print(thisset)  # the set after symmetric difference update
# adds elements from another set to the current set
print(thisset.update({'kiwi', 'mango'}))
print(thisset)  # the set after update
# removes an element from the set if it is a member
print(thisset.discard('banana'))
print(thisset)  # the set after discarding an element
# removes an element from the set, raises KeyError if not found
print(thisset.remove('cherry'))
print(thisset)  # the set after removing an element
print(thisset.add('orange'))  # adds an element to the set
print(thisset)  # the set after adding an element
# adds elements from an iterable to the set
print(thisset.update(['grape', 'melon']))
print(thisset)  # the set after updating with an iterable
# returns a set containing the union of sets
print(thisset.union({'kiwi', 'mango'}))
print(thisset)  # the original set remains unchanged
# returns a set with the intersection of two sets
print(thisset.intersection({'apple', 'kiwi', 'mango'}))
print(thisset)  # the original set remains unchanged
# returns a set with the difference of two sets
print(thisset.difference({'kiwi', 'mango'}))
print(thisset)  # the original set remains unchanged
print(thisset.copy())  # returns a shallow copy of the set
print(thisset.clear())  # removes all elements from the set
print(thisset)  # the set is now empty

# ===============================
# EK BİLGİLER - SETS
# ===============================
# Set Comprehension
squares_set = {x**2 for x in range(10)}
print("Kare sayılar seti:", squares_set)

# Set işlemleri - Matematiksel kümeler
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Birleşim (Union):", A | B)           # {1, 2, 3, 4, 5, 6, 7, 8}
print("Kesişim (Intersection):", A & B)     # {4, 5}
print("Fark (Difference):", A - B)          # {1, 2, 3}
print("Simetrik Fark:", A ^ B)              # {1, 2, 3, 6, 7, 8}

# Alt küme ve üst küme kontrolü
C = {1, 2, 3}
D = {1, 2, 3, 4, 5}
print("C, D'nin alt kümesi mi?", C.issubset(D))      # True
print("D, C'nin üst kümesi mi?", D.issuperset(C))    # True
print("A ve B ayrık mı?", A.isdisjoint(B))           # False

# Tekrarlanan elemanları kaldırma
duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
unique = list(set(duplicates))
print("Tekrarsız liste:", unique)

# Set ile performans avantajı
# Liste yerine set kullanmak üyelik kontrolünde çok daha hızlıdır

large_list = list(range(100000))
large_set = set(range(100000))

# Liste araması
start = time.time()
99999 in large_list
list_time = time.time() - start

# Set araması
start = time.time()
99999 in large_set
set_time = time.time() - start

print(f"Liste araması: {list_time:.10f} saniye")
print(f"Set araması: {set_time:.10f} saniye")
print(f"Set {list_time/set_time:.2f}x daha hızlı!")

# Pratik kullanım: Ortak elemanları bulma
email_list1 = {'user1@mail.com', 'user2@mail.com', 'user3@mail.com'}
email_list2 = {'user2@mail.com', 'user4@mail.com', 'user5@mail.com'}

common_users = email_list1 & email_list2
print("Ortak kullanıcılar:", common_users)

# Sadece bir listede olan kullanıcılar
only_in_list1 = email_list1 - email_list2
print("Sadece liste 1'de:", only_in_list1)

# Frozenset kullanım örneği
immutable_set = frozenset([1, 2, 3, 4, 5])
print("Frozenset:", immutable_set)
# immutable_set.add(6)  # Hata verir - frozenset değiştirilemez

# Frozenset dictionary key olarak kullanılabilir
set_dict = {}
set_dict[frozenset([1, 2, 3])] = "Birinci set"
set_dict[frozenset([4, 5, 6])] = "İkinci set"
print("Set dictionary:", set_dict)
