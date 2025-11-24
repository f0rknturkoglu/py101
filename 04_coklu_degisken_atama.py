"""
ÇOKLU DEĞİŞKEN ATAMA (Multiple Variable Assignment)
====================================================
Python'da birden fazla değişkene aynı anda değer atama yöntemleri
"""

# ===============================
# 1. FARKLI DEĞİŞKENLERE FARKLI DEĞERLER
# ===============================
# Tek satırda birden fazla değişkene farklı değerler atama

x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Orange
print(y)  # Banana
print(z)  # Cherry

# Daha fazla değişken
a, b, c, d = 10, 20, 30, 40
print(a, b, c, d)  # 10 20 30 40

# Karışık tipler
isim, yas, aktif = "Ali", 25, True
print(f"{isim} {yas} yaşında ve aktif: {aktif}")

# ⚠️ DİKKAT: Değişken sayısı ve değer sayısı eşit olmalı!
# x, y = "A", "B", "C"  # HATA: Çok fazla değer
# x, y, z = "A", "B"    # HATA: Çok az değer

# ===============================
# 2. AYNI DEĞER ATAMA
# ===============================
# Birden fazla değişkene aynı değeri atama

x = y = z = "Orange"
print(x)  # Orange
print(y)  # Orange
print(z)  # Orange

# Sayısal örnekler
a = b = c = 0
print(a, b, c)  # 0 0 0

counter1 = counter2 = counter3 = 100
print(counter1, counter2, counter3)  # 100 100 100

# ⚠️ DİKKAT: Listeler ve sözlükler ile dikkatli kullanın!
list1 = list2 = []  # İkisi de AYNI listeyi gösterir
list1.append(1)
print(list2)  # [1] - list2 de değişir!

# Doğru kullanım:
list1 = []
list2 = []  # Ayrı listeler

# ===============================
# 3. LİSTEDEN DEĞER ÇIKARTMA (Unpacking)
# ===============================

# Liste unpacking
meyveler = ["Elma", "Armut", "Muz"]
meyve1, meyve2, meyve3 = meyveler
print(meyve1)  # Elma
print(meyve2)  # Armut
print(meyve3)  # Muz

# Tuple unpacking
koordinat = (10, 20)
x, y = koordinat
print(f"x: {x}, y: {y}")  # x: 10, y: 20

# * operatörü ile geri kalan değerleri alma
sayilar = [1, 2, 3, 4, 5]
ilk, *orta, son = sayilar
print(ilk)   # 1
print(orta)  # [2, 3, 4]
print(son)   # 5

# Sadece ilk ve son
a, *_, z = [1, 2, 3, 4, 5]
print(a)  # 1
print(z)  # 5

# ===============================
# 4. DEĞİŞKEN DEĞİŞTİRME (Swapping)
# ===============================

# Python'da iki değişkenin değerini değiştirmenin kolay yolu
x = 5
y = 10
print(f"Önce: x={x}, y={y}")

# Tek satırda swap
x, y = y, x
print(f"Sonra: x={x}, y={y}")

# Geleneksel yöntem (diğer dillerde):
a = 5
b = 10
temp = a
a = b
b = temp

# ===============================
# 5. DICTIONARY UNPACKING
# ===============================

kisi = {"isim": "Ali", "yas": 30}
isim, yas = kisi.values()
print(isim, yas)  # Ali 30

# Key ve value birlikte
for key, value in kisi.items():
    print(f"{key}: {value}")

# ===============================
# 6. FONKSİYON DÖNÜŞ DEĞERLERİ
# ===============================

def hesapla():
    """Birden fazla değer döndüren fonksiyon"""
    toplam = 100
    fark = 50
    carpim = 2500
    return toplam, fark, carpim

# Çoklu atama ile alma
t, f, c = hesapla()
print(f"Toplam: {t}, Fark: {f}, Çarpım: {c}")

# Sadece bazı değerleri alma
toplam, _, _ = hesapla()  # Sadece toplam'ı kullan
print(f"Sadece toplam: {toplam}")
