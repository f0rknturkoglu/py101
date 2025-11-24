"""
DEĞİŞKEN KAPSAMI (Variable Scope) - Global ve Local
===================================================
Python'da değişkenlerin erişilebilirlik alanı ve global/local kullanımı
"""

# ===============================
# 1. GLOBAL DEĞİŞKENLER
# ===============================
# Fonksiyon dışında tanımlanan değişkenler global'dir

x = "awesome"  # Global değişken

def myfunc():
    """Global değişkene erişim"""
    print("Python is " + x)  # Global x'e erişebilir

myfunc()
print("Python is " + x)  # awesome

# ===============================
# 2. LOCAL DEĞİŞKENLER
# ===============================
# Fonksiyon içinde tanımlanan değişkenler local'dir

def myfunc2():
    """Local değişken örneği"""
    y = "fantastic"  # Local değişken
    print("Python is " + y)

myfunc2()
# print(y)  # HATA! y sadece fonksiyon içinde geçerli

# ===============================
# 3. GLOBAL KEYWORD - Global Değişkeni Değiştirme
# ===============================
# Fonksiyon içinden global değişkeni değiştirmek için global keyword kullanılır

x = "awesome"  # Global değişken

def myfunc3():
    """Global değişkeni değiştirme"""
    global x
    x = "fantastic"  # Global x'i değiştirir
    print("Python is " + x)

myfunc3()
print("Python is " + x)  # fantastic (değişti!)

# ===============================
# 4. GLOBAL KEYWORD İLE YENİ DEĞİŞKEN OLUŞTURMA
# ===============================
# Global keyword ile fonksiyon içinde yeni global değişken oluşturulabilir

def myfunc4():
    """Yeni global değişken oluşturma"""
    global z
    z = "yeni global değişken"

myfunc4()
print(z)  # yeni global değişken

# ===============================
# 5. AYNI İSİMLİ GLOBAL VE LOCAL DEĞİŞKENLER
# ===============================

a = "global"  # Global değişken

def myfunc5():
    """Aynı isimli local değişken"""
    a = "local"  # Local değişken (global'ı gizler)
    print("Fonksiyon içi: " + a)  # local

myfunc5()
print("Fonksiyon dışı: " + a)  # global

# ===============================
# 6. NONLOCAL KEYWORD - İç İçe Fonksiyonlarda
# ===============================
# İç içe fonksiyonlarda dış fonksiyonun değişkenine erişim

def outer():
    """Dış fonksiyon"""
    x = "outer"
    
    def inner():
        """İç fonksiyon"""
        nonlocal x  # Dış fonksiyonun x'ine erişir
        x = "inner"  # Dış fonksiyonun x'ini değiştirir
        print("İç fonksiyon: " + x)
    
    inner()
    print("Dış fonksiyon: " + x)  # inner (değişti!)

outer()

# ===============================
# 7. GLOBAL vs NONLOCAL FARKI
# ===============================

# Global - En üst seviye değişkene erişir
global_var = "global"

def outer2():
    """Dış fonksiyon"""
    nonlocal_var = "nonlocal"
    
    def inner2():
        """İç fonksiyon"""
        global global_var
        nonlocal nonlocal_var
        
        global_var = "değişti (global)"
        nonlocal_var = "değişti (nonlocal)"
    
    inner2()
    print("Nonlocal: " + nonlocal_var)  # değişti (nonlocal)

outer2()
print("Global: " + global_var)  # değişti (global)

# ===============================
# 8. KAPSAM KURALLARI (Scope Rules)
# ===============================

# Python'da kapsam sırası (LEGB):
# L - Local (Yerel)
# E - Enclosing (Kapsayan - iç içe fonksiyonlar)
# G - Global (Genel)
# B - Built-in (Yerleşik)

# Örnek:
x = "global x"

def outer3():
    x = "outer x"
    
    def inner3():
        x = "inner x"
        print(x)  # inner x (en yakın kapsam)
    
    inner3()
    print(x)  # outer x

outer3()
print(x)  # global x

# ===============================
# 9. DİKKAT EDİLMESİ GEREKENLER
# ===============================

# ⚠️ Global değişkenleri değiştirmek genellikle önerilmez
# Bunun yerine parametre ve return kullanmak daha iyidir

# Kötü örnek:
counter = 0

def artir_kotu():
    global counter
    counter += 1

# İyi örnek:
def artir_iyi(sayac):
    return sayac + 1

counter = artir_iyi(counter)

# ⚠️ Global keyword olmadan atama yapılırsa local değişken oluşur
x = 10

def test():
    # x = 20  # Bu local x oluşturur (global x'e erişemez)
    # print(x)  # HATA! x henüz tanımlanmadı
    
    # Çözüm:
    global x
    x = 20  # Şimdi global x'i değiştirir

test()
print(x)  # 20

