i = 1
while i < 6:
    print(i)
    i += 1
print("Done")


i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# ===============================
# EK BİLGİLER - WHILE LOOPS
# ===============================
# While-Else yapısı
# Else bloğu, döngü normal şekilde biterse çalışır (break ile bitmezse)
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Döngü tamamlandı")

# Break ile biterse else çalışmaz
i = 1
while i <= 10:
    if i == 5:
        print("5'te dur!")
        break
    print(i)
    i += 1
else:
    print("Bu çalışmaz")  # Break kullanıldığı için

# Sonsuz döngü (Infinite loop) - Dikkatli kullanın!
# while True:
#     user_input = input("Bir şey yaz (q için çıkış): ")
#     if user_input == 'q':
#         break
#     print(f"Yazdın: {user_input}")

# Kullanıcı girişi doğrulama
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    # password = input("Lütfen şifrenizi girin: ")
    password = "12345"  # Test için
    
    if password == "12345":
        print("Giriş başarılı!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Yanlış şifre! Kalan deneme: {remaining}")
else:
    print("Maksimum deneme sayısına ulaştınız!")

# Do-While taklidi (Python'da do-while yok)
# İlk çalıştır, sonra kontrol et
count = 0
while True:
    print(f"Sayı: {count}")
    count += 1
    if count >= 5:
        break

# Liste elemanlarını while ile işleme
fruits = ['apple', 'banana', 'cherry', 'date']
index = 0

while index < len(fruits):
    print(f"Index {index}: {fruits[index]}")
    index += 1

# While ile toplam hesaplama
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
i = 0

while i < len(numbers):
    total += numbers[i]
    i += 1
print(f"Toplam: {total}")

# Nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i}, {j})", end=" ")
        j += 1
    print()  # Yeni satır
    i += 1

# While ile sayı tahmin oyunu
import random
secret = random.randint(1, 10)
guess_count = 0
max_guesses = 5

print("1-10 arası bir sayı tuttum!")
while guess_count < max_guesses:
    # guess = int(input("Tahmininiz: "))
    guess = random.randint(1, 10)  # Test için
    guess_count += 1
    
    if guess == secret:
        print(f"Tebrikler! {guess_count} denemede buldunuz!")
        break
    elif guess < secret:
        print("Daha yüksek bir sayı girin")
    else:
        print("Daha düşük bir sayı girin")
else:
    print(f"Oyun bitti! Doğru cevap: {secret}")
