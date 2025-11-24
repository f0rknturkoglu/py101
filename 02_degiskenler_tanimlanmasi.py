"""
DEĞİŞKENLER - Temel Tanımlama ve Tipler
========================================
Değişkenler, verileri saklamak için kullanılan isimlendirilmiş bellek alanlarıdır.
Python dinamik tiplemeli bir dildir - değişken tipi otomatik belirlenir.
"""

# Temel değişken tanımlama
x = 5
y = 'John'
print(x)  # 5
print(y)  # John

# Değişkenin değeri değiştirilebilir
x = "salih"
print(x)  # salih

# ===============================
# TİP DÖNÜŞÜMÜ (Type Casting)
# ===============================

# str() - Metine çevirme
a = str(3)     # a = '3' (string)
b = int(3)     # b = 3 (integer)
c = float(3)   # c = 3.0 (float)

# type() fonksiyonu - Değişkenin tipini öğrenme
print(type(a))  # <class 'str'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'float'>

# Daha fazla tip dönüşümü örneği
sayi_str = "100"
sayi_int = int(sayi_str)  # String'i integer'a çevirme
print(sayi_int + 50)  # 150

ondalik = float("3.14")
print(ondalik)  # 3.14

# Boolean dönüşümü
bool_deger = bool(1)  # True
print(bool_deger)

# ===============================
# CASE SENSITIVE (Büyük/Küçük Harf Duyarlılığı)
# ===============================

a = 4
A = "Sally"
print(a)  # 4
print(A)  # Sally
# a ve A farklı değişkenlerdir!

# ===============================
# TEMEL VERİ TİPLERİ
# ===============================

# Integer (Tam sayı)
yaş = 25
nufus = 1000000

# Float (Ondalıklı sayı)
boy = 1.75
agirlik = 68.5

# String (Metin)
isim = "Furkan"
soyisim = 'Türkoğlu'  # Tek veya çift tırnak kullanılabilir

# Boolean (Mantıksal)
aktif_mi = True
ogrenci_mi = False

# None (Boş değer)
adres = None

# Tipleri kontrol etme
print(type(yaş))        # <class 'int'>
print(type(boy))        # <class 'float'>
print(type(isim))       # <class 'str'>
print(type(aktif_mi))   # <class 'bool'>
print(type(adres))      # <class 'NoneType'>
