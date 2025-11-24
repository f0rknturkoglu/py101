"""
STRING İŞLEMLERİ (String Operations)
====================================
Python'da string'lerle yapılabilecek işlemler ve metotlar
"""

# ===============================
# 1. STRING OLUŞTURMA
# ===============================

# Tek tırnak
metin1 = 'Merhaba'

# Çift tırnak
metin2 = "Dünya"

# Tırnak içinde tırnak kullanımı
metin3 = "O dedi ki: 'Merhaba'"
metin4 = 'O dedi ki: "Merhaba"'
metin5 = "O dedi ki: \"Merhaba\""  # Escape karakteri ile

print(metin3)
print(metin4)
print(metin5)

# ===============================
# 2. ÇOK SATIRLI STRING
# ===============================

# Üç çift tırnak ile
cok_satirli1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# Üç tek tırnak ile
cok_satirli2 = '''Bu da
çok satırlı
bir metindir.'''

print(cok_satirli1)
print(cok_satirli2)

# ===============================
# 3. STRING'LER DİZİDİR (Arrays)
# ===============================
# String'ler karakter dizileridir ve index ile erişilebilir

a = "Hello World"
print(a[0])    # H - İlk karakter
print(a[1])    # e
print(a[-1])   # d - Son karakter (negatif index)
print(a[-2])   # l - Sondan ikinci

# ⚠️ String'ler değiştirilemez (immutable)
# a[0] = "h"  # HATA! TypeError

# ===============================
# 4. STRING ÜZERİNDE DÖNGÜ
# ===============================

# for döngüsü ile
for karakter in "banana":
    print(karakter)

# Index ile döngü
metin = "Python"
for i in range(len(metin)):
    print(f"Index {i}: {metin[i]}")

# enumerate ile
for index, karakter in enumerate("Python"):
    print(f"Index {index}: {karakter}")

# ===============================
# 5. STRING UZUNLUĞU
# ===============================

a = "Hello World"
print(len(a))  # 11

# Boş string
bos = ""
print(len(bos))  # 0

# ===============================
# 6. STRING KONTROLÜ - in ve not in
# ===============================

txt = "The best things in life are free!"
print("free" in txt)      # True
print("expensive" in txt)  # False

print("free" not in txt)  # False
print("expensive" not in txt)  # True

# ===============================
# 7. STRING DİLİMLEME (Slicing)
# ===============================

b = "Hello World"

# Baştan dilimleme
print(b[:5])   # Hello - İlk 5 karakter

# Sona kadar dilimleme
print(b[2:])   # llo World - 2. indexten sona kadar

# Belirli aralık
print(b[2:5])  # llo - 2'den 5'e kadar (5 dahil değil)

# Negatif index ile
print(b[-5:-2])  # Wor - Sondan 5'ten sondan 2'ye kadar

# Adım (step) ile
print(b[::2])    # HloWrd - Her 2 karakterden birini al
print(b[1::2])   # el ol - 1'den başlayarak her 2 karakterden birini al
print(b[::-1])   # dlroW olleH - Ters çevir

# ===============================
# 8. STRING METOTLARI - Dönüştürme
# ===============================

# upper() - Büyük harfe çevir
a = "Hello World"
print(a.upper())  # HELLO WORLD

# lower() - Küçük harfe çevir
print(a.lower())  # hello world

# capitalize() - İlk harfi büyük
print("hello world".capitalize())  # Hello world

# title() - Her kelimenin ilk harfini büyük
print("hello world".title())  # Hello World

# swapcase() - Büyük/küçük harfleri değiştir
print("Hello World".swapcase())  # hELLO wORLD

# ===============================
# 9. STRING METOTLARI - Temizleme
# ===============================

# strip() - Başındaki ve sonundaki boşlukları temizle
a = "     Hello World     "
print(a.strip())  # "Hello World"

# lstrip() - Sadece soldaki boşlukları temizle
print(a.lstrip())  # "Hello World     "

# rstrip() - Sadece sağdaki boşlukları temizle
print(a.rstrip())  # "     Hello World"

# ===============================
# 10. STRING METOTLARI - Değiştirme
# ===============================

# replace() - Karakter/kelime değiştirme
a = "Hello World"
print(a.replace("H", "J"))  # Jello World
print(a.replace("World", "Python"))  # Hello Python

# Orijinal string değişmez (immutable)
print(a)  # Hello World

# ===============================
# 11. STRING METOTLARI - Bölme ve Birleştirme
# ===============================

# split() - String'i böl (liste döner)
a = "Hello, World"
print(a.split(","))  # ['Hello', ' World']
print(a.split())     # ['Hello,', 'World'] - Boşluktan böler

# join() - Liste/tuple'ı string'e çevir
liste = ["Hello", "World", "Python"]
print(" ".join(liste))   # Hello World Python
print("-".join(liste))   # Hello-World-Python
print("".join(liste))    # HelloWorldPython

# ===============================
# 12. STRING METOTLARI - Kontrol
# ===============================

# isalpha() - Sadece harf mi?
print("Hello".isalpha())    # True
print("Hello123".isalpha()) # False

# isdigit() - Sadece rakam mı?
print("123".isdigit())      # True
print("12.3".isdigit())     # False

# isalnum() - Harf veya rakam mı?
print("Hello123".isalnum()) # True
print("Hello 123".isalnum()) # False (boşluk var)

# isspace() - Sadece boşluk mu?
print("   ".isspace())      # True
print("Hello".isspace())    # False

# startswith() - Belirli string ile başlıyor mu?
print("Hello World".startswith("Hello"))  # True

# endswith() - Belirli string ile bitiyor mu?
print("Hello World".endswith("World"))    # True

# ===============================
# 13. STRING METOTLARI - Bulma
# ===============================

# find() - İlk bulduğu yerdeki index (bulamazsa -1)
txt = "Hello World"
print(txt.find("World"))   # 6
print(txt.find("Python"))  # -1

# index() - İlk bulduğu yerdeki index (bulamazsa hata)
print(txt.index("World"))  # 6
# print(txt.index("Python"))  # ValueError

# count() - Kaç kez geçiyor?
print("Hello World".count("l"))  # 3

# ===============================
# 14. STRING BİRLEŞTİRME (Concatenation)
# ===============================

# + operatörü ile
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Hello World

# ⚠️ DİKKAT: + operatörü sadece string'lerle çalışır
sayi = 100
# print("Sayı: " + sayi)  # HATA! TypeError

# Çözümler:
print("Sayı: " + str(sayi))  # str() ile dönüştür
print("Sayı:", sayi)          # Virgül kullan
print(f"Sayı: {sayi}")        # f-string kullan

# ===============================
# 15. STRING FORMATLAMA
# ===============================

# f-string (Python 3.6+) - Önerilen
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

# Ondalık formatlama
price = 60
txt = f"The price is {price:.2f} dollars"
print(txt)  # The price is 60.00 dollars

# + operatörü ile (str() gerekir)
age = 35
txt = "My name is John, I am " + str(age)
print(txt)

# ===============================
# 16. ESCAPE KARAKTERLERİ
# ===============================

# \n - Yeni satır
print("Birinci satır\nİkinci satır")

# \t - Tab (sekme)
print("İsim:\tAli\nYaş:\t25")

# \\ - Ters slash
print("C:\\Users\\Documents")

# \" - Çift tırnak
print("O dedi ki: \"Merhaba\"")

# \' - Tek tırnak
print('O dedi ki: \'Merhaba\'')

# \r - Satır başı
print("Merhaba\rDünya")  # Dünya (Merhaba'nın üzerine yazar)

# ===============================
# 17. RAW STRING
# ===============================
# r veya R ile başlar, escape karakterlerini yorumlamaz

print(r"C:\Users\new\test")  # \ karakteri olduğu gibi yazılır
print(r"Merhaba\nDünya")     # \n yorumlanmaz, olduğu gibi yazılır

# ===============================
# 18. STRING ÇARPMA
# ===============================

print("Ha" * 3)  # HaHaHa
print("-" * 20)  # --------------------

# ===============================
# 19. STRING KARŞILAŞTIRMA
# ===============================

# Alfabetik karşılaştırma
print("a" < "b")      # True
print("abc" < "abd")  # True
print("A" < "a")      # True (ASCII değerleri)

# == ve !=
print("Hello" == "Hello")  # True
print("Hello" != "World")  # True

# ===============================
# 20. STRING METOTLARI - Hizalama
# ===============================

# center() - Ortala
print("Hello".center(20))      # "       Hello        "
print("Hello".center(20, "-")) # "-------Hello--------"

# ljust() - Sola hizala
print("Hello".ljust(20))        # "Hello               "

# rjust() - Sağa hizala
print("Hello".rjust(20))       # "               Hello"

# zfill() - Sıfırlarla doldur
print("42".zfill(5))           # "00042"

