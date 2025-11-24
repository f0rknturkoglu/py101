"""
RANDOM MODÜLÜ - Rastgele Sayı ve Seçim İşlemleri
=================================================
Python'da rastgele sayı üretme ve seçim yapma işlemleri
"""

import random

# ===============================
# 1. RANDOM MODÜLÜNÜ İÇE AKTARMA
# ===============================

import random

# ===============================
# 2. RANDOM SAYI ÜRETME
# ===============================

# random() - 0.0 ile 1.0 arasında rastgele float
print(random.random())  # Örnek: 0.548734...

# uniform(a, b) - a ile b arasında rastgele float
print(random.uniform(1.0, 10.0))  # Örnek: 5.234...

# randint(a, b) - a ile b arasında rastgele integer (her ikisi dahil)
print(random.randint(1, 10))  # Örnek: 7

# randrange(start, stop, step) - range() benzeri
print(random.randrange(1, 10))      # 1 ile 9 arası (10 dahil değil)
print(random.randrange(0, 100, 5)) # 0, 5, 10, 15, ..., 95

# ===============================
# 3. LİSTEDEN RASTGELE SEÇİM
# ===============================

# choice() - Listeden rastgele bir eleman seç
meyveler = ["elma", "armut", "muz", "çilek", "kiraz"]
print(random.choice(meyveler))  # Örnek: "muz"

# String'den de seçebilir
print(random.choice("Python"))  # Örnek: "t"

# choices() - Birden fazla seçim (tekrarlı olabilir)
print(random.choices(meyveler, k=3))  # Örnek: ['elma', 'muz', 'elma']

# Ağırlıklı seçim
print(random.choices(meyveler, weights=[10, 1, 1, 1, 1], k=3))

# ===============================
# 4. LİSTEYİ KARIŞTIRMA
# ===============================

# shuffle() - Listeyi yerinde karıştırır
sayilar = [1, 2, 3, 4, 5]
random.shuffle(sayilar)
print(sayilar)  # Örnek: [3, 1, 5, 2, 4]

# ⚠️ DİKKAT: shuffle() orijinal listeyi değiştirir
liste = [1, 2, 3, 4, 5]
random.shuffle(liste)
print(liste)  # Karıştırılmış

# Orijinali korumak için:
liste = [1, 2, 3, 4, 5]
kopya = liste.copy()
random.shuffle(kopya)
print("Orijinal:", liste)  # [1, 2, 3, 4, 5]
print("Karıştırılmış:", kopya)  # Örnek: [3, 1, 5, 2, 4]

# ===============================
# 5. LİSTEDEN ÖRNEKLEME
# ===============================

# sample() - Tekrarsız rastgele örnekleme
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.sample(sayilar, 3))  # Örnek: [7, 2, 9] (tekrarsız)

# ⚠️ DİKKAT: sample() k sayısı listenin uzunluğundan fazla olamaz
# print(random.sample(sayilar, 20))  # HATA! ValueError

# ===============================
# 6. RANDOM SEED - Tekrarlanabilirlik
# ===============================

# seed() - Aynı seed ile aynı rastgele sayılar üretilir
random.seed(42)
print(random.randint(1, 100))  # Örnek: 82
print(random.randint(1, 100))  # Örnek: 15

random.seed(42)  # Aynı seed
print(random.randint(1, 100))  # 82 (aynı)
print(random.randint(1, 100))  # 15 (aynı)

# Seed olmadan her seferinde farklı
print(random.randint(1, 100))  # Farklı bir sayı

# ===============================
# 7. GAUSSIAN (Normal Dağılım)
# ===============================

# gauss(mu, sigma) - Normal dağılım
# mu: ortalama, sigma: standart sapma
print(random.gauss(0, 1))  # Ortalama 0, standart sapma 1

# Örnek: Boy ortalaması 175cm, standart sapma 10cm
boylar = [random.gauss(175, 10) for _ in range(10)]
print(boylar)

# ===============================
# 8. PRATİK ÖRNEKLER
# ===============================

# Şifre oluşturma
karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
sifre = ''.join(random.choices(karakterler, k=12))
print(f"Rastgele şifre: {sifre}")

# Zar atma
zar = random.randint(1, 6)
print(f"Zar sonucu: {zar}")

# İki zar
zar1 = random.randint(1, 6)
zar2 = random.randint(1, 6)
print(f"Zar 1: {zar1}, Zar 2: {zar2}, Toplam: {zar1 + zar2}")

# Rastgele renk seçimi
renkler = ["kırmızı", "mavi", "yeşil", "sarı", "mor", "turuncu"]
rastgele_renk = random.choice(renkler)
print(f"Rastgele renk: {rastgele_renk}")

# Kart çekme simülasyonu
kartlar = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Vale", "Kız", "Papaz"]
renkler_kart = ["Maça", "Kupa", "Karo", "Sinek"]

kart = random.choice(kartlar)
renk = random.choice(renkler_kart)
print(f"Çekilen kart: {kart} {renk}")

# ===============================
# 9. RANDOM İLE LİSTE OLUŞTURMA
# ===============================

# Rastgele sayı listesi
rastgele_sayilar = [random.randint(1, 100) for _ in range(10)]
print(rastgele_sayilar)

# Rastgele float listesi
rastgele_float = [random.uniform(0.0, 1.0) for _ in range(5)]
print(rastgele_float)

# ===============================
# 10. RANDOM MODÜLÜNÜN DİĞER FONKSİYONLARI
# ===============================

# betavariate(alpha, beta) - Beta dağılımı
print(random.betavariate(2, 5))

# expovariate(lambd) - Üstel dağılım
print(random.expovariate(1.5))

# triangular(low, high, mode) - Üçgen dağılım
print(random.triangular(0, 10, 5))

# ===============================
# 11. DİKKAT EDİLMESİ GEREKENLER
# ===============================

# ⚠️ Güvenlik için random yerine secrets kullanın
# Şifre, token gibi güvenlik gerektiren durumlarda:
import secrets
guvenli_sifre = secrets.token_hex(16)
print(f"Güvenli token: {guvenli_sifre}")

# ⚠️ shuffle() orijinal listeyi değiştirir
# ⚠️ sample() k sayısı listenin uzunluğundan fazla olamaz
# ⚠️ choice() boş liste için hata verir
# liste = []
# print(random.choice(liste))  # HATA! IndexError

