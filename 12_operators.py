print(10+3)  # 13
print(10-3)  # 7
print(10*3)  # 30
print(10/3)  # 3.3333...
print(10//3)  # 3
print(10 % 3)  # 1
print(10**3)  # 1000
# ===============================
# 1. ARİTMETİK OPERATÖRLER
# Aritmetik operatörler sayılar üzerinde matematiksel işlemler yapar
a = 15
b = 4
print(a + b)  # Toplama: 19
print(a - b)  # Çıkarma: 11
print(a * b)  # Çarpma: 60
print(a / b)  # Bölme: 3.75
print(a // b)  # Tam Bölme: 3
print(a % b)  # Modül: 3
print(a ** b)  # Üs Alma: 50625
# ===============================
# 2. ATAMA OPERATÖRLERİ
# Atama operatörleri değişkenlere değer atar veya mevcut değeri günceller
x = 10
x += 5  # x = x + 5
print(x)  # 15
x -= 3  # x = x - 3
print(x)  # 12
x *= 2  # x = x * 2
print(x)  # 24
x /= 4  # x = x / 4
print(x)  # 6.0
x //= 2  # x = x // 2
print(x)  # 3.0
x %= 2  # x = x % 2
print(x)  # 1.0
x **= 3  # x = x ** 3
print(x)  # 1.0
# ===============================
# 3. KARŞILAŞTIRMA OPERATÖRLERİ
# Karşılaştırma operatörleri iki değeri karşılaştırır ve boolean (True/False) döner
a = 10
b = 20
print(a == b)  # Eşit mi? False
print(a != b)  # Eşit değil mi? True
print(a > b)   # Büyük mü? False
print(a < b)   # Küçük mü? True
print(a >= b)  # Büyük veya eşit mi? False
print(a <= b)  # Küçük veya eşit mi? True
# ===============================
# 4. MANTIKSAL OPERATÖRLER
# Mantıksal operatörler boolean değerler üzerinde işlem yapar
x = True
y = False
print(x and y)  # Ve (AND): False
print(x or y)   # Veya (OR): True
print(not x)    # Değil (NOT): False
print(not y)    # Değil (NOT): True
# Kombinasyon
print((a < b) and (b > 15))  # True and True -> True
print((a > b) or (b > 15))   # False or True -> True
print(not (a == b))          # not False -> True
# ===============================
# 5. ÜYELİK OPERATÖRÜ
# Üyelik operatörleri bir değerin bir koleksiyonda (liste, dizi, vb.) olup olmadığını kontrol eder
meyveler = ['elma', 'muz', 'çilek']
print('muz' in meyveler)      # True
print('portakal' not in meyveler)  # True
# ===============================
# 6. KİMLİK OPERATÖRÜ
# Kimlik operatörleri iki nesnenin aynı nesne olup olmadığını kontrol eder
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)      # True (aynı nesne)
print(a is c)      # False (farklı nesneler)
print(a is not c)  # True
print(a == c)      # True (değerler aynı)
# ===============================
# 7. ÖNCELİK OPERATÖRLERİ
# Operatör önceliği, hangi işlemin önce yapılacağını belirler
x = 10 + 5 * 2  # Çarpma önce yapılır: 10 + (5 * 2) = 20
print(x)  # 20
y = (10 + 5) * 2  # Parantez içi önce yapılır: (10 + 5) * 2 = 30
print(y)  # 30
z = 10 / 2 + 3 ** 2  # Üs alma önce: (10 / 2) + (3 ** 2) = 5 + 9 = 14.0
print(z)  # 14.0
# Operatör önceliği sırası:
# 1. Parantez ()
# 2. Üs alma **
# 3. Çarpma *, Bölme /, Tam Bölme //, Modül %
# 4. Toplama +, Çıkarma -
# 5. Karşılaştırma operatörleri
# 6. Mantıksal operatörler
# 7. Atama operatörleri
# ===============================
# 8. BİT DÜZEYİ OPERATÖRLERİ
# Bit düzeyi operatörler ikili (binary) sayılar üzerinde işlem yapar
a = 60  # 0011 1100
b = 13  # 0000 1101
print(a & b)  # AND: 0000 1100 -> 12
print(a | b)  # OR:  0011 1101 -> 61
print(a ^ b)  # XOR: 0011 0001 -> 49
print(~a)     # NOT: 1100 0011 -> -61
print(a << 2)  # Sola kaydırma: 1111 0000 -> 240
print(a >> 2)  # Sağa kaydırma: 0000 1111 -> 15
# ===============================
# 9. İDENTİTY VE MEMBERSHIP OPERATÖRLERİNİN KULLANIMI
# identity operatörleri (is, is not) ve membership operatörleri (
# in, not in) ile ilgili örnekler
liste1 = [1, 2, 3]
liste2 = liste1
liste3 = [1, 2, 3]
print(liste1 is liste2)      # True
print(liste1 is liste3)      # False
print(liste1 == liste3)      # True
print(2 in liste1)           # True
print(5 not in liste1)       # True
# ===============================
# 10. TERNARY (KOŞULLU) OPERATÖR
# Koşullu ifade ile değer atama
a = 10
b = 20
maks = a if a > b else b
print(maks)  # 20
# Koşullu ifade ile fonksiyon çağrısı


def buyuk_sayi(x, y):
    return x if x > y else y


print(buyuk_sayi(15, 25))  # 25
# ===============================
# 11. OPERATÖR BİRLİKTE KULLANIMI
a = 5
b = 10
c = 15
sonuc = (a + b) * c / (b - a)

print(sonuc)  # 75.0

# BİTWİSE OPERATÖRLERİNİ KULLANARAK İKİ SAYININ BİT DÜZEYİNDE TOPLAMINI HESAPLAYALIM
x = 29  # 0001 1101
y = 15  # 0000 1111
toplam = 0
for i in range(32):  # 32 bit için
    bit_x = (x >> i) & 1
    bit_y = (y >> i) & 1
    toplam |= (bit_x ^ bit_y) << i  # XOR ile toplama
print(toplam)  # 44 (0010 1100)
# ===============================
# 12. EK BİLGİLER - OPERATORS
# ===============================
# Walrus Operator (:=) - Python 3.8+
# Değer atama ve kullanma işlemini tek satırda yapar
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"Liste uzunluğu {n} ve 3'ten büyük")

# Liste comprehension ile walrus operator
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [y for x in numbers if (y := x ** 2) % 2 == 0]
print("Çift kareler:", even_squares)

# Operatör Overloading (Sınıflarda operatör yüklemesi)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2  # __add__ metodunu çağırır
print(v3)  # Vector(5, 7)

# Karşılaştırma Operatörleri Zincirleme
x = 5
print(1 < x < 10)  # True
print(10 > x <= 5)  # True
print(x == 5 == 5)  # True

# in ve not in operatörü detaylı kullanım
text = "Python Programming"
print('Py' in text)         # True
print('Java' not in text)  # True

# Operator modülü kullanımı
import operator
print(operator.add(5, 3))      # 8
print(operator.mul(4, 7))      # 28
print(operator.pow(2, 3))      # 8
print(operator.truediv(10, 3)) # 3.333...
