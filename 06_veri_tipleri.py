"""
VERİ TİPLERİ (Data Types)
=========================
Python'daki temel veri tipleri ve özellikleri
"""

# ===============================
# 1. NUMERİK TİPLER (Numeric Types)
# ===============================

# Integer (int) - Tam sayılar
sayi = 10
negatif = -5
buyuk_sayi = 1000000000000
print(type(sayi))  # <class 'int'>

# Float - Ondalıklı sayılar
ondalik = 3.14
bilimsel = 2.5e2  # 2.5 * 10^2 = 250.0
print(type(ondalik))  # <class 'float'>

# Complex - Karmaşık sayılar
karmasik = 3 + 4j
print(type(karmasik))  # <class 'complex'>
print(karmasik.real)  # 3.0
print(karmasik.imag)  # 4.0

# ===============================
# 2. STRING (str) - Metin
# ===============================

# Tek veya çift tırnak
metin1 = 'Merhaba'
metin2 = "Dünya"

# Çok satırlı string
uzun_metin = """Bu bir
çok satırlı
metindir."""

# String işlemleri
print(len("Python"))  # 6 - Uzunluk
print("Python"[0])    # P - İlk karakter (index 0)
print("Python"[-1])   # n - Son karakter
print("Python"[0:3])  # Pyt - Dilimle (slice)

# String metotları
print("python".upper())        # PYTHON
print("PYTHON".lower())        # python
print("python".capitalize())   # Python
print("  python  ".strip())    # "python" - Boşlukları temizle
print("python".replace("p", "P"))  # Python

# ===============================
# 3. BOOLEAN (bool) - Mantıksal Değerler
# ===============================

dogru = True
yanlis = False
print(type(dogru))  # <class 'bool'>

# Boolean dönüşümleri
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False - Boş string
print(bool("text")) # True
print(bool([]))     # False - Boş liste
print(bool([1, 2])) # True

# ===============================
# 4. NONE - Boş/Yok Değeri
# ===============================

bos_deger = None
print(type(bos_deger))  # <class 'NoneType'>

# None kontrolü
if bos_deger is None:
    print("Değer None")

# ===============================
# 5. LİSTE (list) - Sıralı, Değiştirilebilir Koleksiyon
# ===============================

# Liste oluşturma
meyveler = ["elma", "armut", "muz"]
sayilar = [1, 2, 3, 4, 5]
karisik = [1, "iki", 3.0, True]  # Farklı tipler olabilir

print(type(meyveler))  # <class 'list'>

# Liste işlemleri
print(meyveler[0])      # elma - İlk eleman
print(meyveler[-1])     # muz - Son eleman
print(len(meyveler))    # 3 - Uzunluk

# Liste değiştirme
meyveler[0] = "çilek"
print(meyveler)  # ['çilek', 'armut', 'muz']

# Liste metotları
meyveler.append("kiraz")      # Sona ekle
meyveler.insert(0, "elma")    # Başa ekle
meyveler.remove("armut")      # Kaldır
son = meyveler.pop()          # Son elemanı çıkar

# ===============================
# 6. TUPLE - Sıralı, DEĞİŞTİRİLEMEZ Koleksiyon
# ===============================

# Tuple oluşturma (parantez ile)
koordinat = (10, 20)
renkler = ("kırmızı", "yeşil", "mavi")
tek_elemanli = (5,)  # Tek elemanlı tuple (virgül önemli!)

print(type(koordinat))  # <class 'tuple'>

# Tuple işlemleri (sadece okuma)
print(koordinat[0])   # 10
print(len(renkler))   # 3

# ⚠️ Tuple değiştirilemez!
# renkler[0] = "sarı"  # HATA! TypeError

# Tuple avantajları:
# - Daha hızlı
# - Değişmemesi gereken veriler için güvenli
# - Dictionary key olarak kullanılabilir

# ===============================
# 7. SET - Sırasız, Tekil Eleman Koleksiyonu
# ===============================

# Set oluşturma
sayilar_set = {1, 2, 3, 4, 5}
meyveler_set = {"elma", "armut", "muz"}

print(type(sayilar_set))  # <class 'set'>

# Tekrarlı elemanlar otomatik silinir
tekrarli = {1, 2, 2, 3, 3, 3}
print(tekrarli)  # {1, 2, 3}

# Set işlemleri
sayilar_set.add(6)      # Ekle
sayilar_set.remove(1)   # Kaldır
# print(sayilar_set[0])  # HATA! Index yok

# Set matematiksel işlemleri
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Birleşim: {1, 2, 3, 4, 5}
print(set1 & set2)  # Kesişim: {3}
print(set1 - set2)  # Fark: {1, 2}

# ===============================
# 8. DİCTİONARY (dict) - Anahtar-Değer Çiftleri
# ===============================

# Dictionary oluşturma
kisi = {
    "isim": "Ali",
    "yas": 30,
    "sehir": "İstanbul"
}

print(type(kisi))  # <class 'dict'>

# Erişim
print(kisi["isim"])      # Ali
print(kisi.get("yas"))   # 30
print(kisi.get("adres", "Belirtilmemiş"))  # Varsayılan değer

# Değiştirme ve ekleme
kisi["yas"] = 31
kisi["meslek"] = "Mühendis"

# Dictionary metotları
print(kisi.keys())    # Anahtarlar
print(kisi.values())  # Değerler
print(kisi.items())   # Anahtar-değer çiftleri

# Döngü
for anahtar, deger in kisi.items():
    print(f"{anahtar}: {deger}")

# ===============================
# 9. RANGE - Sayı Dizisi
# ===============================

# Range oluşturma
sayilar = range(5)        # 0, 1, 2, 3, 4
sayilar2 = range(2, 10)   # 2, 3, 4, 5, 6, 7, 8, 9
sayilar3 = range(0, 10, 2)  # 0, 2, 4, 6, 8 (adım: 2)

print(type(sayilar))  # <class 'range'>
print(list(sayilar))  # [0, 1, 2, 3, 4] - Listeye çevirme

# ===============================
# 10. BYTES ve BYTEARRAY - İkili Veriler
# ===============================

# Bytes - Değiştirilemez
b = b"Hello"
print(type(b))  # <class 'bytes'>

# Bytearray - Değiştirilebilir
ba = bytearray(b"Hello")
print(type(ba))  # <class 'bytearray'>
ba[0] = 74  # 'J'
print(ba)  # bytearray(b'Jello')

# ===============================
# TİP KONTROLÜ VE DÖNÜŞÜMÜ
# ===============================

# type() - Tipi öğrenme
x = 5
print(type(x))  # <class 'int'>

# isinstance() - Tip kontrolü
print(isinstance(x, int))    # True
print(isinstance(x, str))    # False

# Tip dönüşümleri
str(123)        # "123"
int("123")      # 123
float("3.14")   # 3.14
list("abc")     # ['a', 'b', 'c']
tuple([1, 2])   # (1, 2)
set([1, 2, 2])  # {1, 2}
