day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")  # defaul

# ===============================
# EK BİLGİLER - MATCH/CASE
# ===============================
# Match-Case (Python 3.10+) - Gelişmiş Pattern Matching

# 1. Liste/Tuple Pattern Matching
point = (0, 5)

match point:
    case (0, 0):
        print("Orijinde")
    case (0, y):
        print(f"Y ekseni üzerinde: y={y}")
    case (x, 0):
        print(f"X ekseni üzerinde: x={x}")
    case (x, y):
        print(f"Koordinat: ({x}, {y})")

# 2. Guard Clauses (Koşullu Pattern)
age = 25

match age:
    case x if x < 0:
        print("Geçersiz yaş")
    case x if 0 <= x < 18:
        print("Çocuk")
    case x if 18 <= x < 65:
        print("Yetişkin")
    case x if x >= 65:
        print("Yaşlı")

# 3. Or Pattern (|)
status = "error"

match status:
    case "success" | "ok" | "done":
        print("Başarılı durum")
    case "error" | "failed" | "crash":
        print("Hata durumu")
    case _:
        print("Bilinmeyen durum")

# 4. Dictionary Pattern Matching
user = {"name": "Ali", "role": "admin", "active": True}

match user:
    case {"role": "admin", "active": True}:
        print("Aktif admin kullanıcı")
    case {"role": "admin", "active": False}:
        print("Pasif admin kullanıcı")
    case {"role": "user"}:
        print("Normal kullanıcı")
    case _:
        print("Bilinmeyen kullanıcı tipi")

# 5. Sınıf Pattern Matching
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

shape = Circle(Point(0, 0), 5)

match shape:
    case Point(x=0, y=0):
        print("Orijinde nokta")
    case Point(x, y):
        print(f"Nokta: ({x}, {y})")
    case Circle(center=Point(x=0, y=0), radius=r):
        print(f"Merkezde daire, yarıçap: {r}")
    case Circle(radius=r):
        print(f"Daire, yarıçap: {r}")

# 6. Liste Pattern Matching - Döküm (Unpacking)
data = [1, 2, 3, 4, 5]

match data:
    case []:
        print("Boş liste")
    case [x]:
        print(f"Tek eleman: {x}")
    case [x, y]:
        print(f"İki eleman: {x}, {y}")
    case [first, *middle, last]:
        print(f"İlk: {first}, Orta: {middle}, Son: {last}")

# 7. HTTP Status Code Örneği
def handle_response(status_code, data):
    match status_code:
        case 200:
            return f"Başarılı: {data}"
        case 404:
            return "Sayfa bulunamadı"
        case 500 | 502 | 503:
            return "Sunucu hatası"
        case code if 400 <= code < 500:
            return f"Client hatası: {code}"
        case code if 500 <= code < 600:
            return f"Server hatası: {code}"
        case _:
            return "Bilinmeyen durum kodu"

print(handle_response(200, "Veri alındı"))
print(handle_response(503, None))
