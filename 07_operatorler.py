"""
OPERATÖRLER (Operators)
=======================
Python'daki operatörler ve kullanımları
"""

# ===============================
# 1. ARİTMETİK OPERATÖRLER
# ===============================

a = 10
b = 3

print(a + b)   # 13 - Toplama
print(a - b)   # 7  - Çıkarma
print(a * b)   # 30 - Çarpma
print(a / b)   # 3.333... - Bölme (float)
print(a // b)  # 3  - Tam bölme (int)
print(a % b)   # 1  - Mod (kalan)
print(a ** b)  # 1000 - Üs alma (10^3)

# Öncelik sırası: ** > * / // % > + -
print(2 + 3 * 4)      # 14 (önce çarpma)
print((2 + 3) * 4)    # 20 (parantez önce)

# ===============================
# 2. ATAMA OPERATÖRLERİ
# ===============================

x = 10         # Basit atama
x += 5         # x = x + 5  -> 15
x -= 3         # x = x - 3  -> 12
x *= 2         # x = x * 2  -> 24
x /= 4         # x = x / 4  -> 6.0
x //= 2        # x = x // 2 -> 3.0
x %= 2         # x = x % 2  -> 1.0
x **= 3        # x = x ** 3 -> 1.0


# Çoklu atama
a = b = c = 0
x, y, z = 1, 2, 3


# ===============================
# 3. KARŞILAŞTIRMA OPERATÖRLERİ
# ===============================

x = 5
y = 10

print(x == y)  # False - Eşit mi?
print(x != y)  # True  - Eşit değil mi?
print(x > y)   # False - Büyük mü?
print(x < y)   # True  - Küçük mü?
print(x >= y)  # False - Büyük veya eşit mi?
print(x <= y)  # True  - Küçük veya eşit mi?

# String karşılaştırma (alfabetik)
print("a" < "b")      # True
print("abc" < "abd")  # True

# ===============================
# 4. MANTIKSAL OPERATÖRLER
# ===============================

x = 5

# and - Her ikisi de True olmalı
print(x > 3 and x < 10)   # True
print(x > 3 and x < 4)    # False

# or - En az biri True olmalı
print(x > 3 or x < 4)     # True
print(x < 3 or x > 10)    # False

# not - Tersi
print(not(x > 3))         # False

# Kombinasyonlar
yas = 25
print(yas >= 18 and yas <= 65)  # Çalışma yaşı
print(yas < 18 or yas > 65)     # Çalışma yaşı dışı

# ===============================
# 5. KİMLİK OPERATÖRLERİ
# ===============================

x = ["elma", "armut"]
y = ["elma", "armut"]
z = x

# is - Aynı nesne mi?
print(x is z)    # True  - Aynı nesne
print(x is y)    # False - Farklı nesneler (aynı içerik olsa da)

# is not
print(x is not y)  # True

# == vs is farkı
print(x == y)    # True  - İçerik aynı
print(x is y)    # False - Farklı nesneler

# None kontrolü (is kullanılmalı)
deger = None
print(deger is None)      # Doğru kullanım
print(deger == None)      # Çalışır ama önerilmez

# ===============================
# 6. ÜYELİK OPERATÖRLERİ
# ===============================

# in - İçeriyor mu?
meyveler = ["elma", "armut", "muz"]
print("elma" in meyveler)     # True
print("çilek" in meyveler)    # False

# not in - İçermiyor mu?
print("çilek" not in meyveler)  # True

# String içinde arama
metin = "Python programlama"
print("Python" in metin)      # True
print("Java" in metin)        # False

# Dictionary'de arama (key'lerde arar)
kisi = {"isim": "Ali", "yas": 30}
print("isim" in kisi)         # True
print("Ali" in kisi)          # False (value'da değil)
print("Ali" in kisi.values()) # True

# ===============================
# 7. BİTWİSE (Bit Düzeyinde) OPERATÖRLER
# ===============================

a = 60   # 0011 1100
b = 13   # 0000 1101

print(a & b)   # 12  - AND (VE)
print(a | b)   # 61  - OR (VEYA)
print(a ^ b)   # 49  - XOR (Özel VEYA)
print(~a)      # -61 - NOT (Tersi)
print(a << 2)  # 240 - Sola kaydırma
print(a >> 2)  # 15  - Sağa kaydırma

# ===============================
# 8. WALRUS OPERATÖRÜ := (Python 3.8+)
# ===============================

# Atama ve kullanma aynı anda
# Eskiden:
n = 10
if n > 5:
    print(n)

# Walrus ile:
if (n := 10) > 5:
    print(n)

# Liste comprehension içinde
# Eskiden:
sayilar = [1, 2, 3, 4, 5]
sonuc = []
for x in sayilar:
    y = x * 2
    if y > 4:
        sonuc.append(y)

# Walrus ile:
sonuc = [y for x in sayilar if (y := x * 2) > 4]

# ===============================
# 9. OPERATÖR ÖNCELİĞİ (Yüksekten Düşüğe)
# ===============================

"""
1. ()                          - Parantez
2. **                          - Üs alma
3. +x, -x, ~x                  - Unary plus, minus, bitwise NOT
4. *, /, //, %                 - Çarpma, bölme, mod
5. +, -                        - Toplama, çıkarma
6. <<, >>                      - Bitwise shift
7. &                           - Bitwise AND
8. ^                           - Bitwise XOR
9. |                           - Bitwise OR
10. ==, !=, >, >=, <, <=       - Karşılaştırma
    is, is not, in, not in
11. not                        - Boolean NOT
12. and                        - Boolean AND
13. or                         - Boolean OR
14. :=                         - Walrus
"""

# Örnek
sonuc = 2 + 3 * 4 ** 2  # 2 + 3 * 16 = 2 + 48 = 50
print(sonuc)

sonuc = (2 + 3) * 4 ** 2  # 5 * 16 = 80
print(sonuc)

# ===============================
# 10. ÖZEL OPERATÖRLER
# ===============================

# Ternary (Koşullu) operatör
yas = 20
durum = "Reşit" if yas >= 18 else "Reşit değil"
print(durum)  # Reşit

# String çarpma
print("Ha" * 3)  # HaHaHa

# Liste toplama
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
print(liste1 + liste2)  # [1, 2, 3, 4, 5, 6]

# Liste çarpma
print([0] * 5)  # [0, 0, 0, 0, 0]

