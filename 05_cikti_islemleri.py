"""
ÇIKTI İŞLEMLERİ (Output Operations)
====================================
Python'da ekrana çıktı vermenin farklı yöntemleri
"""

# ===============================
# 1. TEK DEĞİŞKEN YAZDIRMA
# ===============================

x = "Python is fun!"
print(x)

# ===============================
# 2. ÇOKLU DEĞİŞKEN YAZDIRMA - VIRGÜL İLE
# ===============================
# Virgül ile ayrılan değerler arasında otomatik boşluk eklenir

x = "Python"
y = "is"
z = "fun!"
print(x, y, z)  # Python is fun!

# Karışık tipler
isim = "Ali"
yas = 25
print("İsim:", isim, "Yaş:", yas)  # İsim: Ali Yaş: 25

# ===============================
# 3. STRING BİRLEŞTİRME - + OPERATÖRÜ
# ===============================
# + operatörü string'leri birleştirir (boşluk eklemez)

x = "Python "
y = "is "
z = "fun!"
print(x + y + z)  # Python is fun!

# ⚠️ DİKKAT: + operatörü sadece string'lerle çalışır
sayi = 100
# print("Sayı: " + sayi)  # HATA! int ile str birleştirilemez

# Çözümler:
print("Sayı: " + str(sayi))  # str() ile dönüştürme
print("Sayı:", sayi)  # Virgül kullanma

# ===============================
# 4. F-STRING (Formatted String Literals) - Modern ve Önerilen
# ===============================
# Python 3.6+ - En modern ve okunabilir yöntem

isim = "Furkan"
yas = 25
boy = 1.75

# Temel kullanım
print(f"Merhaba, ben {isim}")
print(f"Ben {yas} yaşındayım")

# Birden fazla değişken
print(f"{isim} {yas} yaşında ve boyu {boy}m")

# İfadeler içinde hesaplama
print(f"5 yıl sonra {yas + 5} yaşında olacak")
print(f"10 kişiye {100 / 10} TL düşer")

# Formatlama
pi = 3.14159265
print(f"Pi sayısı: {pi:.2f}")  # 2 ondalık basamak: 3.14

sayi = 1234567
print(f"Formatlanmış: {sayi:,}")  # Binlik ayırıcı: 1,234,567

# ===============================
# 5. %-FORMATTING (Eski Stil)
# ===============================
# Python 2 tarzı, hala çalışır ama önerilmez

isim = "Ali"
yas = 30

print("İsim: %s, Yaş: %d" % (isim, yas))
print("Yüzde: %.2f%%" % 45.67)  # Yüzde: 45.67%

# %s - String
# %d - Integer
# %f - Float

# ===============================
# 6. .format() METODU
# ===============================
# Python 3 tarzı, f-string'den önce kullanılırdı

isim = "Ayşe"
yas = 28

print("İsim: {}, Yaş: {}".format(isim, yas))
print("İsim: {0}, Yaş: {1}".format(isim, yas))  # Index ile
print("İsim: {i}, Yaş: {y}".format(i=isim, y=yas))  # İsimli

# Formatlama
print("Fiyat: {:.2f} TL".format(123.456))  # Fiyat: 123.46 TL

# ===============================
# 7. ÖZEL KARAKTERLER
# ===============================

# Yeni satır (\n)
print("Birinci satır\nİkinci satır")

# Tab (\t)
print("İsim:\tAli\nYaş:\t25")

# Ters slash (\\)
print("C:\\Users\\Documents")

# Tırnak işareti
print('O dedi ki: "Merhaba"')
print("O dedi ki: \"Merhaba\"")

# ===============================
# 8. RAW STRING
# ===============================
# r veya R ile başlar, özel karakterleri yorumlamaz

print(r"C:\Users\new\test")  # \ karakteri olduğu gibi yazılır

# ===============================
# 9. ÇOKLU SATIRLI STRING
# ===============================
# Üç tırnak ile (''' veya """)

mesaj = """Bu bir
çok satırlı
mesajdır."""
print(mesaj)

# ===============================
# 10. PRINT PARAMETRELERİ
# ===============================

# sep - Ayırıcı (varsayılan: boşluk)
print("A", "B", "C", sep="-")  # A-B-C
print(2024, 11, 23, sep="/")  # 2024/11/23

# end - Satır sonu (varsayılan: \n)
print("Birinci", end=" ")
print("aynı satırda")  # Birinci aynı satırda

# Her ikisini birlikte
print("Python", "Java", "C++", sep=" | ", end=" <- Diller\n")

# file - Dosyaya yazdırma
with open("cikti.txt", "w", encoding="utf-8") as f:
    print("Bu dosyaya yazılır", file=f)

# flush - Tamponu temizleme (animasyonlar için)
import time
for i in range(5):
    print(f"\rYükleniyor: {i+1}/5", end="", flush=True)
    time.sleep(0.5)
print()  # Yeni satır

# ===============================
# 11. REPR VS STR
# ===============================

metin = "Merhaba\nDünya"
print(str(metin))   # Okunabilir çıktı
print(repr(metin))  # Geliştirici çıktısı: 'Merhaba\nDünya'

tarih = "2024-11-23"
print(f"Tarih: {tarih}")        # Tarih: 2024-11-23
print(f"Tarih: {tarih!r}")      # Tarih: '2024-11-23'
