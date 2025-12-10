# LAMBDA FUNCTIONS

import sys
def x(a): return a + 10


print(x(5))


def x(a, b): return a*b


print(x(5, 6))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))


# lambda with build in functions


numbers = [2, 3, 4, 5, 1, 2]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)

# using lambda with filter()

students = [('John', 88), ('Emma', 92), ('Sam', 75), ('Olivia', 95)]
passed_students = list(filter(lambda student: student[1] >= 80, students))
print(passed_students)


words = ["apple", "pie", "banaaaaaaaaaana", "cheeerry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


# Python recursion

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)


countdown(5)


def factorial(n):
    # BASE CASE
    if n == 1 or n == 0:
        return 1
    else:
        # RECURSIVE CASE
        return n * factorial(n-1)


print(factorial(5))


# FIBONACCI SERIES

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))


# recursion with list

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])


my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))
# OUTPUT: 15


# recursion depth limit

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())


# PYTHON GENERATORS

def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)


def kareler_generator(n):
    for i in range(n):
        yield i * i


g = kareler_generator(5)
print(next(g))
print(next(g))
print(next(g))


def large_sequence(n):
    for i in range(n):
        yield i


# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))


def simple_gen():
    yield 1
    yield 2


gen = simple_gen()
print(next(gen))
print(next(gen))
# print(next(gen)) #this will raise StopIteration


def fibonacci2():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Get first 100 Fibonacci numbers
gen = fibonacci2()
for _ in range(100):
    print(next(gen))


# ============================================================
# 1) Normal fonksiyon vs Generator fonksiyonu
# ============================================================

def kareler_liste(n):
    """
    Bu fonksiyon *liste* döner.
    Tüm kareleri hafızaya alır, sonra listeyi geri verir.
    """
    sonuc = []
    for i in range(n):
        sonuc.append(i * i)
    return sonuc  # burada fonksiyon tamamen biter


def kareler_generator(n):
    """
    Bu fonksiyon bir *generator* döner.
    Değerleri tek tek 'yield' ile üretir.
    """
    for i in range(n):
        # 'yield' = "şu değeri ver, ama fonksiyonu bitirme, kaldığın yerden devam et"
        yield i * i


# ============================================================
# 2) next() ile adım adım çalışmayı görmek
# ============================================================

def adim_adim():
    print("1. adım")
    yield 10  # durdur, 10 döndür
    print("2. adım")
    yield 20  # tekrar durdur, 20 döndür
    print("3. adım")
    yield 30  # tekrar durdur, 30 döndür
    print("fonksiyon gerçekten bitti")


# ============================================================
# 3) Generator ifadesi (generator expression)
#    List comprehension'ın tembel (lazy) versiyonu
# ============================================================

# Liste:
# kareler_liste_comp = [x * x for x in range(5)]

# Generator:
# kareler_gen_exp = (x * x for x in range(5))

# Liste tüm değerleri hafızaya yükler.
# Generator ise ihtiyaca göre üretir.


# ============================================================
# DEMO BÖLÜMÜ
# Bu dosyayı direkt çalıştırınca burası çalışır.
# ============================================================

if __name__ == "__main__":
    print("=== 1) Normal fonksiyon vs Generator fonksiyonu ===")
    lst = kareler_liste(5)
    print("kareler_liste(5) ->", lst)

    gen = kareler_generator(5)
    print("kareler_generator(5) ->", gen)  # generator objesi
    print("list(kareler_generator(5)) ->", list(kareler_generator(5)))

    print("\n=== 2) next() ile adım adım ===")
    g = adim_adim()
    print("next(g) ->", next(g))  # 1. adım yazdırır, 10 döner
    print("next(g) ->", next(g))  # 2. adım yazdırır, 20 döner
    print("next(g) ->", next(g))  # 3. adım yazdırır, 30 döner

    # Bir sonraki next(g) çağrısı StopIteration hatası verir
    # çünkü generator tamamen bitmiştir.
    # Bunu görmek istersen yorumdan çıkar:
    # print("next(g) ->", next(g))

    print("\n=== 3) Generator ifadesi örneği ===")
    kareler_gen_exp = (x * x for x in range(5))
    print("kareler_gen_exp ->", kareler_gen_exp)
    for deger in kareler_gen_exp:
        print("generator ifadesinden gelen:", deger)
