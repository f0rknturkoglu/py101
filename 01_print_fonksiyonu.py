"""
PRINT FONKSIYONU - Ekrana Çıktı Verme
=====================================
print() fonksiyonu Python'da ekrana metin, sayı ve diğer değerleri yazdırmak için kullanılır.
"""

# Temel print kullanımı
print("Python is fun!")
print("he baba sensin ok")
print("Hello World")

# end parametresi - Satır sonunu değiştirme
# Varsayılan olarak print() her yazdırmadan sonra yeni satıra geçer
# end parametresi ile bunu değiştirebiliriz
print("merhaba dunya", end=" ")  # Yeni satıra geçmez, boşluk bırakır
print("i will print on the same line.")

# Birden fazla değer yazdırma - virgül ile ayırma
# Virgül ile ayrılan değerler arasında otomatik boşluk konur
print("i am", 35, "years old.")

# sep parametresi - Değerler arasındaki ayırıcıyı değiştirme
print("Elma", "Armut", "Muz", sep=" - ")
print("2024", "11", "23", sep="/")

# Farklı end örnekleri
print("Satır 1", end="...")
print("Satır 2")

# Hem sep hem end kullanımı
print("Python", "Java", "C++", sep=" | ", end=" <- Diller\n")

# Boş print - Sadece yeni satır
print()
print("Bu yukarıda boş bir satır var")
