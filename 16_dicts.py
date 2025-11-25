thistict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"

}
print(thistict)

thistict["age"] = 31
print(thistict)

thistict["job"] = "Engineer"
print(thistict)

del thistict["city"]
print(thistict)

print(len(thistict))

for key in thistict:
    print(key, thistict[key])

for key, value in thistict.items():
    print(key, value)

print(thistict.keys())

print(thistict.values())

print(thistict.items())

thistict.clear()
print(thistict)


anotherdict = dict(name="Bob", age=25, city="Los Angeles")
print(anotherdict)

copydict = anotherdict.copy()
print(copydict)

mergedict = {**thistict, **anotherdict}


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

print(x)

x = thisdict.keys()
print(x)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"  # adding a new key-value pair

print(x)  # after the change


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change


x = thisdict.items()
print(x)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}


for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])
'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''

# ===============================
# EK BİLGİLER - DICTIONARIES
# ===============================
# Dictionary Comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print("Kare sayılar sözlüğü:", squares_dict)

# Koşullu dictionary comprehension
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Çift sayıların kareleri:", even_squares)

# İki listeyi dictionary'ye dönüştürme
keys = ['name', 'age', 'city']
values = ['Ali', 25, 'İstanbul']
person_dict = dict(zip(keys, values))
print("Kişi bilgisi:", person_dict)

# get() metodunun avantajlı kullanımı
person = {'name': 'Ali', 'age': 25}
print(person.get('city', 'Bilinmiyor'))  # Key yoksa varsayılan değer döner
# print(person['city'])  # KeyError verir!

# setdefault() - key yoksa ekler ve değer döner
student = {'name': 'Ayşe'}
student.setdefault('grade', 'A')  # grade yoksa ekler
print("Student:", student)

# defaultdict - otomatik varsayılan değer
from collections import defaultdict

word_count = defaultdict(int)  # Varsayılan değer: 0
text = "hello world hello python world"
for word in text.split():
    word_count[word] += 1
print("Kelime sayısı:", dict(word_count))

# Counter - eleman sayma için özel sözlük
from collections import Counter

fruits = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
fruit_counts = Counter(fruits)
print("Meyve sayıları:", fruit_counts)
print("En çok tekrarlanan 2:", fruit_counts.most_common(2))

# İç içe dictionary işlemleri
company = {
    'IT': {
        'employees': ['Ali', 'Veli'],
        'manager': 'Ahmet'
    },
    'HR': {
        'employees': ['Ayşe', 'Fatma'],
        'manager': 'Mehmet'
    }
}

# İç içe erişim
print("IT çalışanları:", company['IT']['employees'])

# Dictionary birleştirme (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = dict1 | dict2  # Birleştirme operatörü
print("Birleştirilmiş:", merged)

# Dictionary sıralama
scores = {'Ali': 85, 'Veli': 92, 'Ayşe': 78, 'Fatma': 95}
sorted_by_value = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print("Puana göre sıralı:", sorted_by_value)

# Dictionary filtreleme
filtered = {k: v for k, v in scores.items() if v >= 85}
print("85 ve üstü:", filtered)
