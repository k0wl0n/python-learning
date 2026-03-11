"""
=== IDENTITY OPERATORS (Operator Identitas) ===

Operator    Deskripsi
is          Mengembalikan True jika kedua variabel menunjuk ke objek yang SAMA
is not      Mengembalikan True jika kedua variabel menunjuk ke objek yang BERBEDA

Penting: 'is' mengecek identitas objek (apakah lokasi memori sama),
         '==' mengecek kesamaan nilai.
"""

print("=== IDENTITY OPERATORS ===")
print()

# --- Contoh dasar ---
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")
print()

# 'is' - cek apakah objek yang sama (lokasi memori sama)
print(f"a is b     -> {a is b}")       # False (objek berbeda, meski nilainya sama)
print(f"a is c     -> {a is c}")       # True (c menunjuk ke objek yang sama dengan a)
print(f"a is not b -> {a is not b}")   # True
print(f"a is not c -> {a is not c}")   # False
print()

# Perbandingan 'is' vs '=='
print("--- Perbedaan 'is' vs '==' ---")
print(f"a == b     -> {a == b}")       # True (nilainya sama)
print(f"a is b     -> {a is b}")       # False (objek berbeda)
print()

# Membuktikan dengan id()
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}")
print(f"id(a) == id(c) -> {id(a) == id(c)}")  # True
print()

# --- Contoh dengan None ---
print("--- Contoh dengan None ---")
x = None
y = 5

print(f"x = {x}")
print(f"x is None     -> {x is None}")        # True
print(f"y is None     -> {y is None}")         # False
print(f"y is not None -> {y is not None}")     # True
print()

# --- Contoh dengan integer kecil (Python caching) ---
print("--- Python Integer Caching (-5 sampai 256) ---")
p = 256
q = 256
print(f"p = {p}, q = {q}")
print(f"p is q -> {p is q}")    # True (Python meng-cache integer -5 s/d 256)

r = 257
s = 257
print(f"r = {r}, s = {s}")
print(f"r is s -> {r is s}")    # Bisa True atau False tergantung implementasi
print(f"r == s -> {r == s}")    # Selalu True
