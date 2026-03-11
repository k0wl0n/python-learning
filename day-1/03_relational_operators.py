"""
=== RELATIONAL OPERATORS (Operator Perbandingan) ===

Operator relasional digunakan untuk membandingkan dua nilai.
Hasilnya selalu Boolean (True atau False).
"""

a = 10
b = 20
c = 10

print("=== RELATIONAL OPERATORS ===")
print(f"a = {a}, b = {b}, c = {c}")
print()

# Sama dengan (==)
print(f"a == b  -> {a == b}")    # False
print(f"a == c  -> {a == c}")    # True

# Tidak sama dengan (!=)
print(f"a != b  -> {a != b}")    # True
print(f"a != c  -> {a != c}")    # False

# Lebih besar (>)
print(f"a > b   -> {a > b}")     # False
print(f"b > a   -> {b > a}")     # True

# Lebih kecil (<)
print(f"a < b   -> {a < b}")     # True
print(f"b < a   -> {b < a}")     # False

# Lebih besar atau sama dengan (>=)
print(f"a >= c  -> {a >= c}")    # True
print(f"a >= b  -> {a >= b}")    # False

# Lebih kecil atau sama dengan (<=)
print(f"a <= c  -> {a <= c}")    # True
print(f"b <= a  -> {b <= a}")    # False

print()

# --- Contoh penggunaan ---
print("=== CONTOH PENGGUNAAN ===")

nilai = 75
if nilai >= 60:
    print(f"Nilai {nilai} >= 60: LULUS")
else:
    print(f"Nilai {nilai} < 60: TIDAK LULUS")

umur = 17
if umur >= 17:
    print(f"Umur {umur} >= 17: Boleh buat SIM")
else:
    print(f"Umur {umur} < 17: Belum boleh buat SIM")

password_input = "rahasia123"
password_benar = "rahasia123"
if password_input == password_benar:
    print("Password cocok! Login berhasil.")
else:
    print("Password salah!")
