# Boolean values
print(10 > 9)  # True
print(10 == 9)  # False
# ===============================
# 1. BOOLEAN DEĞERLER
# ===============================
print(True)  # Doğru
print(False)  # Yanlış
# Boolean değerler karşılaştırma ifadelerinden elde edilir
print(5 > 3)   # True
print(2 == 4)  # False
print(7 <= 7)  # True
print(3 != 3)  # False
# Boolean değerler mantıksal işlemlerde kullanılır
print(True and False)  # False
print(True or False)   # True

a = 200
b = 33

if b > a:
    print("b büyüktür a'dan")
else:
    print("b büyük değildir a'dan")
# ===============================

print(bool("Hello"))
print(bool(15))
print(bool(''))

# ===============================
# EK BİLGİLER - BOOLEANS
# ===============================
# Boolean Değerler ve Dönüşümler:
# Aşağıdaki değerler False olarak değerlendirilir:
# - bool(False)
# - bool(None)
# - bool(0)
# - bool("")
# - bool(())
# - bool([])
# - bool({})

# Bunların dışındaki tüm değerler True'dur
print(bool(None))      # False
print(bool(0))         # False
print(bool([]))        # False
print(bool({}))        # False
print(bool(()))        # False
print(bool(1))         # True
print(bool([1, 2]))     # True
print(bool({"a": 1}))   # True

# Boolean Fonksiyonları


def is_even(number):
    """Sayının çift olup olmadığını kontrol eder"""
    return number % 2 == 0


print(is_even(4))   # True
print(is_even(7))   # False

# Boolean ile Koşullu İfadeler
numbers = [1, 2, 3, 4, 5]
has_even = any(x % 2 == 0 for x in numbers)  # En az bir çift var mı?
all_positive = all(x > 0 for x in numbers)   # Hepsi pozitif mi?

print("Has even number:", has_even)       # True
print("All positive:", all_positive)       # True

# isinstance() ile tip kontrolü
value = 42
print(isinstance(value, int))    # True
print(isinstance(value, str))    # False
