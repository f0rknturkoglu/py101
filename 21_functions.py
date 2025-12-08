def my_function():
    print("This is my function.")

    pass

my_function()
my_function()
my_function()

def get_greeting():
    return "Hello, World!"

greeting = get_greeting()
print(greeting)
print(get_greeting())

#bir fonksiyon return statementne sahip değilse, None döner
def my_other_function():
    pass

result = my_other_function()
print(result)  # None yazdırır


##arguments##

def myfunc_with_arguments(fname):
    print(fname+'turkoglu')

myfunc_with_arguments("furkan ")

# -parameters vs arguments 
# parameters: fonksiyon tanımlanırken kullanılan değişken isimleridir.
# arguments: fonksiyon çağrılırken verilen gerçek değerlerdir.

def myfunc_with_multiple_arguments(fname, lname): #fname lname is a parameter
    print(fname + ' ' + lname)


myfunc_with_multiple_arguments("furkan", "turkoglu")
myfunc_with_multiple_arguments("ali", "veli") #ali veli argument'tir.


##Default parameter values##

def myfunc_with_default_parameter(country = "Norway"):
    print("I am from " + country)


myfunc_with_default_parameter("Sweden")
myfunc_with_default_parameter("India")
myfunc_with_default_parameter() #burda norway default olarak gelir


##keyword arguments

def myfunc_with_keyword_arguments(child3, child2, child1):
    print("The youngest child is " + child3)

myfunc_with_keyword_arguments(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
myfunc_with_keyword_arguments(child2 = "Tobias", child1 = "Emil", child3 = "Linus")


##positional arguments##

def my_function2(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function2(animal = "dog", name = "Buddy")


##mixing positional and keyword arguments##

def my_function3(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function3("dog", name = "Buddy", age = 5)

#passing different data types



def my_function4(fruits):
    for fruit in fruits:
        print(fruit)

fruits_list = ["apple", "banana", "cherry"]
my_function4(fruits_list)



def my_function5(person):
    return f"{person['name']} is {person['age']} years old."
person_info = {"name": "Alice", "age": 30}
result = my_function5(person_info)
print(result)  # "Alice is 30 years old."




##return values##
def my_function6(x,y):
    return y * x


result = my_function6(3,2)

print(result)  # 6


##returning different data types

def my_function7():
    return [1, 2, 3, 4, 5]

fruits=my_function7()
print(fruits)  # [1, 2, 3, 4,5]
print(fruits[0])  # 1
print(fruits[1])  # 2
print(fruits[2])  # 3


##positional-only arguments

def ornek(a, b, /, c, d, *, e, f):
    """
    a, b: positional-only
    c, d: positional veya keyword
    e, f: keyword-only
    """
    print(a, b, c, d, e, f)

# Doğru kullanım
ornek(1, 2, 3, d=4, e=5, f=6)
ornek(1, 2, c=3, d=4, e=5, f=6)


def uzaklik(x1, y1, x2, y2, /):
    """İki nokta arası uzaklık - parametreler sadece sırayla"""
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Doğal kullanım:
uzaklik(0, 0, 3, 4)  # 5.0
# x1=0, y1=0 gibi yazmaya gerek yok, sıra belli


def sunucu_ayarla(*, host, port, ssl=True, timeout=60):
    """Sunucu ayarları - tüm parametreler keyword ile verilmeli"""
    print(f"{host}:{port} (SSL: {ssl}, Timeout: {timeout})")

# Açık ve okunabilir:
sunucu_ayarla(host="example.com", port=8080, ssl=False)
# sunucu_ayarla("example.com", 8080)  # HATA! Karışıklık olurdu



def veri_isle(dosya_yolu, /, encoding="utf-8", *, kaydet=False, loglama=True):
    """
    dosya_yolu: positional-only (zorunlu ve sırayla)
    encoding: normal (optional, positional/keyword)
    kaydet, loglama: keyword-only (seçenekler açık olmalı)
    """
    print(f"{dosya_yolu} - {encoding} - kaydet:{kaydet} - log:{loglama}")

# Kullanım:
veri_isle("rapor.txt", "ascii", kaydet=True, loglama=False)
veri_isle("rapor.txt", kaydet=True)  # encoding varsayılan




###keyword-only arguments###

def my_function8(*, name):
    print("Hello, " + name)

my_function8(name="Alice")




## *args and **kwargs##


def topla(*args):
    """Sınırsız sayıda sayıyı toplar"""
    print(f"args türü: {type(args)}")  # <class 'tuple'>
    print(f"args değeri: {args}")      # Gelen sayıların tuple'ı
    return sum(args)

print(topla(1, 2, 3))          # 6
print(topla(1, 2, 3, 4, 5))    # 15
print(topla())                  # 0 (boş tuple)




def kullanici_bilgileri(**kwargs):
    """Sınırsız sayıda keyword argüman alır"""
    print(f"kwargs türü: {type(kwargs)}")  # <class 'dict'>
    print(f"kwargs değeri: {kwargs}")      # Gelen keyword'lerin dictionary'si
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kullanici_bilgileri(ad="Ali", yas=25, sehir="Ankara")
# Çıktı:
# ad: Ali
# yas: 25
# sehir: Ankara
kullanici_bilgileri(ad="Ayşe", meslek="Mühendis")
kullanici_bilgileri(am="Fatma",im='sss')


##using **kwargs with regular arguments

def my_function9(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function9("emil123", age = 25, city = "Oslo", hobby = "coding")
my_function9("veli456", country = "Turkey", profession = "engineer")



##combining *args and **kwargs

# the order must be:
#1-regular positional arguments
#2-*args
#3-**kwargs



def my_function10(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function10("User Info", "Emil", "Tobias", age = 25, city = "Oslo")
my_function10("Product Details", "Laptop", "Smartphone", price = 1500, stock = 30)
my_function10("Event", "Conference", date="2024-10-15", location="New York")
my_function10("Test")


##unpacking lists with *

def my_function11(a,b,c):
    return a+b+c

numbers=[1,2,3]
result=my_function11(*numbers)  #unpacking list
print(result)  #6


#unpacking dictionaries with **

def my_function12(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

person_info = {"name": "Alice", "age": 30, "city": "New York"}
result = my_function12(**person_info)  #unpacking dictionary
print(result)  #Alice is 30 years old and lives in New York.




##python scope##

def myFunc():
    x = 10  # local scope
    print("Inside function, x =", x)

#local scope

def myFunc2():
    x = 5  # local scope
    def innerFunc():
        y = 10  # inner function scope
        print("Inside inner function, y =", y)
    innerFunc()
    print("Inside outer function, x =", x)



myFunc2()    

##global scope##

x=300

def myFunc3():
    x=200  # local scope
    print("Inside function, x =", x)  # accesses global x
myFunc3()
print("Outside function, x =", x)  # accesses global x

print("--------------")
#global keyword

x=300
def myFunc4():
    global x
    x = 200  # modifies global x
    print("Inside function, x =", x)


myFunc4()

print("Outside function, x =", x)  # accesses modified global x


##nonlocal keyword##

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


##LEGB Rule
'''
Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace

'''

