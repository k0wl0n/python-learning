"""
=== USE CASE: KALKULATOR LENGKAP ===

Contoh nyata penggunaan function untuk membangun aplikasi kalkulator.
Mendemonstrasikan:
    - Function untuk setiap operasi
    - Function untuk validasi
    - Function untuk display
    - Cross function calls
    - Dictionary dispatch (pengganti if-elif panjang)
"""


# ============================================================
# FUNCTION: OPERASI DASAR
# ============================================================

def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        return None
    return a / b


def pangkat(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def bagi_bulat(a, b):
    if b == 0:
        return None
    return a // b


# ============================================================
# FUNCTION: OPERASI LANJUTAN
# ============================================================

def faktorial(n):
    """Hitung n! (n harus integer >= 0)."""
    if not isinstance(n, int) or n < 0:
        return None
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def akar_kuadrat(n):
    """Hitung akar kuadrat (n harus >= 0)."""
    if n < 0:
        return None
    return n ** 0.5


def rata_rata(*angka):
    """Hitung rata-rata dari sejumlah angka."""
    if not angka:
        return None
    return sum(angka) / len(angka)


# ============================================================
# FUNCTION: KONVERSI
# ============================================================

def celcius_ke_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_ke_celcius(f):
    return (f - 32) * 5 / 9


def km_ke_mil(km):
    return km * 0.621371


def mil_ke_km(mil):
    return mil / 0.621371


def desimal_ke_biner(n):
    """Konversi desimal ke string biner."""
    if not isinstance(n, int) or n < 0:
        return None
    return bin(n)[2:]


def biner_ke_desimal(biner_str):
    """Konversi string biner ke desimal."""
    try:
        return int(biner_str, 2)
    except ValueError:
        return None


# ============================================================
# FUNCTION: DISPLAY
# ============================================================

def tampilkan_menu():
    print("\n╔════════════════════════════════════════╗")
    print("║         KALKULATOR PYTHON              ║")
    print("╠════════════════════════════════════════╣")
    print("║  OPERASI DASAR:                        ║")
    print("║    1. Tambah (+)                        ║")
    print("║    2. Kurang (-)                        ║")
    print("║    3. Kali (×)                          ║")
    print("║    4. Bagi (÷)                          ║")
    print("║    5. Pangkat (^)                       ║")
    print("║    6. Modulus (%)                       ║")
    print("║    7. Bagi Bulat (//)                   ║")
    print("║                                         ║")
    print("║  OPERASI LANJUTAN:                      ║")
    print("║    8. Faktorial (n!)                    ║")
    print("║    9. Akar Kuadrat (√)                  ║")
    print("║   10. Rata-rata                         ║")
    print("║                                         ║")
    print("║  KONVERSI:                              ║")
    print("║   11. Celcius ↔ Fahrenheit              ║")
    print("║   12. KM ↔ Mil                          ║")
    print("║   13. Desimal ↔ Biner                   ║")
    print("║                                         ║")
    print("║    0. Keluar                            ║")
    print("╚════════════════════════════════════════╝")


def tampilkan_hasil(operasi, result):
    if result is None:
        print(f"  ❌ Error: Operasi tidak valid")
    else:
        print(f"  ✅ {operasi} = {result}")


def garis():
    print("  " + "─" * 40)


# ============================================================
# FUNCTION: PROSES OPERASI (Cross Function)
# ============================================================

def proses_operasi_dasar(pilihan, a, b):
    """Dispatch operasi berdasarkan pilihan menggunakan dictionary."""
    operasi_map = {
        1: ("+", tambah),
        2: ("-", kurang),
        3: ("×", kali),
        4: ("÷", bagi),
        5: ("^", pangkat),
        6: ("%", modulus),
        7: ("//", bagi_bulat),
    }

    if pilihan not in operasi_map:
        return None, None

    simbol, func = operasi_map[pilihan]
    hasil = func(a, b)
    label = f"{a} {simbol} {b}"
    return label, hasil


# ============================================================
# DEMO: Simulasi penggunaan kalkulator
# ============================================================

print("=" * 60)
print("DEMO KALKULATOR")
print("=" * 60)

tampilkan_menu()

# Simulasi operasi dasar
print("\n--- Operasi Dasar ---")
demo_operasi = [
    (1, 15, 8),     # tambah
    (2, 20, 7),     # kurang
    (3, 6, 9),      # kali
    (4, 100, 3),    # bagi
    (4, 10, 0),     # bagi dengan 0
    (5, 2, 10),     # pangkat
    (6, 17, 5),     # modulus
    (7, 17, 5),     # bagi bulat
]

for pilihan, a, b in demo_operasi:
    label, hasil = proses_operasi_dasar(pilihan, a, b)
    tampilkan_hasil(label, hasil)

# Simulasi operasi lanjutan
print("\n--- Operasi Lanjutan ---")
for n in [5, 10, 0]:
    hasil = faktorial(n)
    tampilkan_hasil(f"{n}!", hasil)

for n in [16, 144, 2]:
    hasil = akar_kuadrat(n)
    tampilkan_hasil(f"√{n}", hasil)

hasil = rata_rata(85, 90, 78, 92, 88)
tampilkan_hasil("Rata-rata(85,90,78,92,88)", hasil)

# Simulasi konversi
print("\n--- Konversi ---")
garis()
print("  Suhu:")
for c in [0, 37, 100]:
    f = celcius_ke_fahrenheit(c)
    tampilkan_hasil(f"{c}°C -> °F", f"{f:.1f}°F")

for f in [32, 98.6, 212]:
    c = fahrenheit_ke_celcius(f)
    tampilkan_hasil(f"{f}°F -> °C", f"{c:.1f}°C")

garis()
print("  Jarak:")
for km in [1, 10, 42.195]:
    m = km_ke_mil(km)
    tampilkan_hasil(f"{km} km -> mil", f"{m:.3f} mil")

garis()
print("  Bilangan:")
for n in [10, 42, 255]:
    b = desimal_ke_biner(n)
    tampilkan_hasil(f"{n} -> biner", b)

for b in ["1010", "101010", "11111111"]:
    d = biner_ke_desimal(b)
    tampilkan_hasil(f"{b} -> desimal", d)

print()

# ============================================================
# RIWAYAT PERHITUNGAN
# ============================================================
print("--- Riwayat Perhitungan ---")

riwayat = []


def hitung_dan_simpan(a, simbol, b, func):
    """Hitung, simpan ke riwayat, dan tampilkan."""
    hasil = func(a, b)
    entry = {"operasi": f"{a} {simbol} {b}", "hasil": hasil}
    riwayat.append(entry)
    return hasil


def tampilkan_riwayat():
    if not riwayat:
        print("  (Riwayat kosong)")
        return
    for i, r in enumerate(riwayat, 1):
        print(f"  {i}. {r['operasi']} = {r['hasil']}")


hitung_dan_simpan(100, "+", 200, tambah)
hitung_dan_simpan(500, "-", 150, kurang)
hitung_dan_simpan(25, "×", 4, kali)
hitung_dan_simpan(1000, "÷", 3, bagi)

tampilkan_riwayat()

print()
print("=" * 60)
print("Selesai! Use case kalkulator sudah dicontohkan.")
