"""
DEĞİŞKEN İSİMLENDİRME KURALLARI VE KONVANSIYONLARI
===================================================
Python'da değişken isimlendirmenin kuralları ve yaygın kullanım şekilleri
"""

# ===============================
# YASAL DEĞİŞKEN İSİMLERİ (Legal Variable Names)
# ===============================

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# ===============================
# YASADIŞI DEĞİŞKEN İSİMLERİ (Illegal Variable Names)
# ===============================
# Aşağıdaki kullanımlar HATA verir:

# 2myvar = "John"        # HATA: Sayı ile başlayamaz
# my-var = "John"        # HATA: Tire (-) kullanılamaz
# my var = "John"        # HATA: Boşluk kullanılamaz
# for = "John"           # HATA: Ayrılmış kelime (keyword) kullanılamaz

# ===============================
# PYTHON AYRIŞMIŞ KELİMELER (Keywords)
# ===============================
# Bu kelimeler değişken adı olarak KULLANILMAZ:
"""
and, as, assert, break, class, continue, def, del, elif, else, except, 
False, finally, for, from, global, if, import, in, is, lambda, None, 
nonlocal, not, or, pass, raise, return, True, try, while, with, yield
"""

# Keyword'leri görmek için:
import keyword
print("Python Keywords:")
print(keyword.kwlist)

# ===============================
# İSİMLENDİRME KONVANSIYONLARI
# ===============================

# 1. Camel Case - Her kelimenin ilk harfi büyük (ilk kelime hariç)
# Genellikle değişkenlerde kullanılır
myVariableName = "John"
totalAmount = 1000
isStudentActive = True

# 2. Pascal Case - Her kelimenin ilk harfi büyük (ilk kelime dahil)
# Genellikle sınıf (class) isimlerinde kullanılır
MyVariableName = "John"
StudentRecord = {}
PersonData = []

# 3. Snake Case - Kelimeler alt çizgi ile ayrılır (PYTHON'DA ÖNERİLEN)
# Python topluluğu tarafından en çok tercih edilen yöntem
my_variable_name = "John"
total_amount = 1000
is_student_active = True

# 4. SCREAMING_SNAKE_CASE - Sabitler için (constants)
# Tamamı büyük harf, kelimeler alt çizgi ile ayrılır
MAX_VALUE = 100
PI = 3.14159
DATABASE_URL = "localhost:5432"

# ===============================
# İYİ PRATİKLER
# ===============================

# ✅ AÇIKLAYICI isimler kullanın
student_age = 20  # İyi
s_a = 20  # Kötü - ne anlama geldiği belirsiz

# ✅ Anlamlı isimler
total_price = 150.50  # İyi
tp = 150.50  # Kötü

# ✅ Boolean değişkenler soru formatında
is_active = True
has_permission = False
can_edit = True

# ✅ Çoğul/tekil ayrımı
student = "Ali"  # Tekil
students = ["Ali", "Veli", "Ayşe"]  # Çoğul

# ===============================
# KAÇINILMASI GEREKENLER
# ===============================

# ❌ Tek karakter (döngü değişkenleri hariç)
# x = 10  # Anlamsız
user_count = 10  # Daha iyi

# ❌ Türkçe karakter kullanımı (teknik olarak çalışır ama önerilmez)
değişken = "test"  # Çalışır ama tavsiye edilmez
degisken = "test"  # Daha iyi

# ❌ Çok uzun isimler
# this_is_a_very_long_variable_name_that_is_hard_to_read = 10  # Aşırı uzun
user_registration_count = 10  # Dengeli
