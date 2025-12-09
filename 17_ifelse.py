a = 33
b = 200
if b > a:
    print("b is greater than a")


age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")


isLoggedIn = True
if isLoggedIn:
    print("Welcome back, user!")


a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")


day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")


temperature = 22

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside!")


username = "Emil"

if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty")


a = 5
b = 2
if a > b:
    print("a is greater than b")


a = 2
b = 330
print("A") if a > b else print("B")


a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)


username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)


# Logical Operators

# and, or, not


age = 25
if age >= 18 and age <= 65:
    print("You are eligible to work")


age = 17
if age < 18 or age > 65:
    print("You are not in the working age group")


is_raining = False
if not is_raining:
    print("You don't need an umbrella today")


temperature = 25
if temperature > 20 and not is_raining:
    print("It's a nice day for a walk")


time = 14
if time < 12 or (time >= 12 and time < 18):
    print("Good day!")
if time < 12:
    print("Good morning!")
elif time >= 12 and time < 18:
    print("Good afternoon!")
else:
    print("Good evening!")


age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")


a = 33
b = 200


value = 50

if value < 0:
    print("Negative value")
elif value == 0:
    pass  # Zero case - no action needed
else:
    print("Positive value")

# ===============================
# EK BİLGİLER - IF/ELSE
# ===============================
# İç İçe (Nested) If Yapıları
age = 25
income = 30000

if age >= 18:
    if income >= 25000:
        print("Kredi başvurunuz onaylandı")
    else:
        print("Gelir yetersiz")
else:
    print("Yaşınız 18'den küçük")

# Ternary Operator (Üçlü Koşul) - Gelişmiş
number = 15
result = "Pozitif" if number > 0 else "Negatif" if number < 0 else "Sıfır"
print(f"{number} sayısı {result}")

# Birden fazla koşulun kontrolü
username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Giriş başarılı")
elif username != "admin":
    print("Kullanıcı adı yanlış")
else:
    print("Şifre yanlış")

# in operatörü ile kontrol
allowed_users = ['admin', 'user1', 'user2']
user = 'admin'

if user in allowed_users:
    print(f"{user} sisteme giriş yapabilir")
else:
    print("Yetkiniz yok")

# Match-Case vs If-Elif (Python 3.10+)
# Match-Case daha okunabilir olabilir
status_code = 404

# If-elif yöntemi
if status_code == 200:
    message = "OK"
elif status_code == 404:
    message = "Not Found"
elif status_code == 500:
    message = "Server Error"
else:
    message = "Unknown"

print(f"If-Elif: {message}")

# Match-case yöntemi (Python 3.10+)
match status_code:
    case 200:
        message = "OK"
    case 404:
        message = "Not Found"
    case 500:
        message = "Server Error"
    case _:
        message = "Unknown"

print(f"Match-Case: {message}")

# Truthy ve Falsy değerler
# Falsy: False, None, 0, 0.0, '', [], {}, ()
# Truthy: Falsy olmayan her şey

empty_list = []
if empty_list:
    print("Liste dolu")
else:
    print("Liste boş")  # Bu çalışacak

name = "Ali"
if name:  # name boş string değilse True
    print(f"Merhaba {name}")

# Short-circuit evaluation


def check():
    print("Fonksiyon çağrıldı")
    return True


# and operatörü: sol taraf False ise sağ taraf kontrol edilmez
if False and check():  # check() çağrılmaz
    print("Buraya gelmez")

# or operatörü: sol taraf True ise sağ taraf kontrol edilmez
if True or check():  # check() çağrılmaz
    print("Buraya gelir")
