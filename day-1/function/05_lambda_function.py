"""
=== LAMBDA FUNCTION (Anonymous Function) ===

Syntax:
    lambda parameter: ekspresi

Lambda adalah function tanpa nama, biasanya untuk operasi singkat 1 baris.
    - Tidak bisa pakai statement (if-else biasa, loop, dll)
    - Bisa pakai ternary expression
    - Sering dipakai dengan map(), filter(), sorted()
"""


# ============================================================
# 1. LAMBDA DASAR
# ============================================================
print("=" * 60)
print("1. LAMBDA DASAR")
print("=" * 60)

# Function biasa
def kuadrat(x):
    return x ** 2

# Lambda equivalent
kuadrat_lambda = lambda x: x ** 2

print(f"Function biasa: kuadrat(5) = {kuadrat(5)}")
print(f"Lambda:         kuadrat(5) = {kuadrat_lambda(5)}")
print()

# Beberapa contoh lambda
tambah = lambda a, b: a + b
kali = lambda a, b: a * b
sapa = lambda nama: f"Halo, {nama}!"
absolut = lambda x: x if x >= 0 else -x

print(f"tambah(3, 4)  = {tambah(3, 4)}")
print(f"kali(3, 4)    = {kali(3, 4)}")
print(f"sapa('Budi')  = {sapa('Budi')}")
print(f"absolut(-10)  = {absolut(-10)}")
print()


# ============================================================
# 2. LAMBDA DENGAN map()
# ============================================================
print("=" * 60)
print("2. LAMBDA DENGAN map()")
print("=" * 60)

angka = [1, 2, 3, 4, 5]

kuadrat_list = list(map(lambda x: x ** 2, angka))
print(f"Kuadrat:     {kuadrat_list}")

celcius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celcius))
print(f"Celcius:     {celcius}")
print(f"Fahrenheit:  {fahrenheit}")

nama_list = ["budi", "rina", "andi"]
title_list = list(map(lambda n: n.title(), nama_list))
print(f"Title case:  {title_list}")

harga = [15000, 25000, 50000]
ppn = list(map(lambda h: int(h * 1.11), harga))
print(f"Harga + PPN: {ppn}")
print()


# ============================================================
# 3. LAMBDA DENGAN filter()
# ============================================================
print("=" * 60)
print("3. LAMBDA DENGAN filter()")
print("=" * 60)

angka = list(range(1, 21))

genap = list(filter(lambda x: x % 2 == 0, angka))
print(f"Genap (1-20):    {genap}")

prima_kecil = list(filter(lambda x: all(x % i != 0 for i in range(2, x)) and x > 1, range(2, 30)))
print(f"Prima (<30):     {prima_kecil}")

kata = ["Python", "AI", "Go", "JavaScript", "C", "Rust"]
panjang = list(filter(lambda k: len(k) > 3, kata))
print(f"Kata > 3 huruf:  {panjang}")

nilai = [85, 42, 91, 67, 55, 78, 93]
lulus = list(filter(lambda n: n >= 75, nilai))
tidak_lulus = list(filter(lambda n: n < 75, nilai))
print(f"Lulus (>=75):     {lulus}")
print(f"Tidak lulus:      {tidak_lulus}")
print()


# ============================================================
# 4. LAMBDA DENGAN sorted()
# ============================================================
print("=" * 60)
print("4. LAMBDA DENGAN sorted()")
print("=" * 60)

# Sort by custom key
siswa = [
    {"nama": "Charlie", "nilai": 78},
    {"nama": "Alice", "nilai": 92},
    {"nama": "Bob", "nilai": 85},
    {"nama": "Diana", "nilai": 95},
]

by_nama = sorted(siswa, key=lambda s: s["nama"])
by_nilai = sorted(siswa, key=lambda s: s["nilai"], reverse=True)

print("Sorted by nama:")
for s in by_nama:
    print(f"  {s['nama']}: {s['nilai']}")

print("\nSorted by nilai (desc):")
for s in by_nilai:
    print(f"  {s['nama']}: {s['nilai']}")

# Sort string by length
kata = ["Python", "AI", "Go", "JavaScript", "C"]
by_length = sorted(kata, key=lambda k: len(k))
print(f"\nBy length: {by_length}")

# Sort tuple
data = [(3, "c"), (1, "a"), (2, "b")]
by_first = sorted(data, key=lambda x: x[0])
by_second = sorted(data, key=lambda x: x[1])
print(f"By first:  {by_first}")
print(f"By second: {by_second}")
print()


# ============================================================
# 5. LAMBDA DENGAN reduce()
# ============================================================
print("=" * 60)
print("5. LAMBDA DENGAN reduce()")
print("=" * 60)

from functools import reduce

angka = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, angka)
print(f"Sum {angka} = {total}")

produk = reduce(lambda a, b: a * b, angka)
print(f"Product {angka} = {produk}")

terbesar = reduce(lambda a, b: a if a > b else b, angka)
print(f"Max {angka} = {terbesar}")

kata = ["Belajar", "Python", "itu", "seru"]
gabung = reduce(lambda a, b: f"{a} {b}", kata)
print(f"Join {kata} = '{gabung}'")
print()


# ============================================================
# 6. LAMBDA SEBAGAI ARGUMENT
# ============================================================
print("=" * 60)
print("6. LAMBDA SEBAGAI ARGUMENT")
print("=" * 60)


def terapkan_ke_semua(func, data):
    """Terapkan function ke semua elemen."""
    return [func(x) for x in data]


angka = [1, -2, 3, -4, 5]
print(f"Data: {angka}")
print(f"Kuadrat:  {terapkan_ke_semua(lambda x: x**2, angka)}")
print(f"Absolut:  {terapkan_ke_semua(lambda x: abs(x), angka)}")
print(f"Kali 10:  {terapkan_ke_semua(lambda x: x*10, angka)}")
print(f"String:   {terapkan_ke_semua(lambda x: str(x), angka)}")
print()


def buat_operasi(op):
    """Return lambda berdasarkan string operasi."""
    operasi = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else "Error",
    }
    return operasi.get(op, lambda a, b: "Operasi tidak dikenal")


for op in ["+", "-", "*", "/"]:
    fn = buat_operasi(op)
    print(f"  10 {op} 3 = {fn(10, 3)}")

print()
print("=" * 60)
print("Selesai! Lambda function sudah dicontohkan.")
