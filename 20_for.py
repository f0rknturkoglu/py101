fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


for x in "banana":
    print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


for x in range(6):
    print(x)


# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

for x in range(2, 6):
    print(x)
# 2,3,4,5
print("-----")
for x in range(2, 4):
    print(x)
print("-----")

for x in range(1, 11, 3):
    print(x)


for x in range(6):
    print(x)
else:
    print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


for x in [0, 1, 2]:
    pass

# ===============================
# EK BİLGİLER - FOR LOOPS
# ===============================
# enumerate() - index ve değeri birlikte alma
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# enumerate() başlangıç index'i belirleme
for index, fruit in enumerate(fruits, start=1):
    print(f"Meyve {index}: {fruit}")

# zip() - birden fazla listeyi paralel dolaşma
names = ['Ali', 'Veli', 'Ayşe']
ages = [25, 30, 28]
cities = ['İstanbul', 'Ankara', 'İzmir']

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age} yaşında, {city}'de yaşıyor")

# zip() farklı uzunluktaki listelerle
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
for num, letter in zip(list1, list2):
    print(num, letter)  # En kısa liste kadarsını alır

# reversed() - tersten dolaşma
numbers = [1, 2, 3, 4, 5]
for num in reversed(numbers):
    print(num, end=' ')  # 5 4 3 2 1
print()

# range() ile farklı kullanımlar
# Geriye doğru sayma
for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()

# Çift sayılar
for i in range(0, 11, 2):
    print(i, end=' ')  # 0 2 4 6 8 10
print()

# List Comprehension - tek satırda liste oluşturma
squares = [x**2 for x in range(1, 6)]
print("Kareler:", squares)  # [1, 4, 9, 16, 25]

# Koşullu list comprehension
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Çift sayıların kareleri:", even_squares)

# İç içe list comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix:")
for row in matrix:
    print(row)

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print("Kare sözlüğü:", squares_dict)

# Set comprehension
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}
print("Tekil kareler:", unique_squares)

# Dictionary üzerinde dolaşma
person = {'name': 'Ali', 'age': 25, 'city': 'İstanbul'}

# Sadece key'ler
for key in person:
    print(key)

# Key ve value'lar
for key, value in person.items():
    print(f"{key}: {value}")

# Sadece value'lar
for value in person.values():
    print(value)

# Nested loops (iç içe döngüler)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end='\t')
    print()  # Yeni satır

# break ve continue birlikte kullanım
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 3:
        continue  # 3'ü atla
    if num == 8:
        break  # 8'de dur
    print(num, end=' ')  # 1 2 4 5 6 7
print()

# for-else yapısı
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num > 10:
        print("10'dan büyük sayı bulundu")
        break
else:
    print("10'dan büyük sayı yok")  # Break çalışmadıysa bu çalışır

# String karakterlerini dolaşma
text = "Python"
for char in text:
    print(char, end='-')  # P-y-t-h-o-n-
print()

# items() ile sıralama
scores = {'Ali': 85, 'Veli': 92, 'Ayşe': 78}
for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{name}: {score}")
