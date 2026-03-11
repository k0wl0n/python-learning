"""
=== TERNARY OPERATOR (Conditional Expression) ===

Syntax:
    nilai_true if kondisi else nilai_false

Ternary operator adalah cara singkat menulis if-else dalam satu baris.
"""

# ============================================================
# 1. TERNARY DASAR
# ============================================================
print("=" * 60)
print("1. TERNARY DASAR")
print("=" * 60)

# Cara biasa (if-else)
umur = 20
if umur >= 17:
    status = "Dewasa"
else:
    status = "Anak-anak"
print(f"Cara biasa:  umur={umur} -> {status}")

# Cara ternary (1 baris)
umur = 20
status = "Dewasa" if umur >= 17 else "Anak-anak"
print(f"Ternary:     umur={umur} -> {status}")
print()

# Contoh lain
angka = 7
hasil = "Genap" if angka % 2 == 0 else "Ganjil"
print(f"{angka} adalah {hasil}")

suhu = 38
kondisi = "Demam" if suhu > 37.5 else "Normal"
print(f"Suhu {suhu}°C: {kondisi}")

nilai = 85
lulus = "LULUS" if nilai >= 75 else "TIDAK LULUS"
print(f"Nilai {nilai}: {lulus}")

saldo = 50000
bisa_beli = "Bisa beli" if saldo >= 30000 else "Saldo kurang"
print(f"Saldo Rp{saldo:,}: {bisa_beli}")
print()


# ============================================================
# 2. TERNARY DALAM PRINT
# ============================================================
print("=" * 60)
print("2. TERNARY DALAM PRINT")
print("=" * 60)

x = 10
print(f"{x} adalah {'positif' if x > 0 else 'negatif atau nol'}")

nama = ""
print(f"Nama: {'(kosong)' if not nama else nama}")

nama = "Budi"
print(f"Nama: {'(kosong)' if not nama else nama}")

items = 3
print(f"Keranjang: {items} {'item' if items == 1 else 'items'}")
print()


# ============================================================
# 3. TERNARY BERSARANG (NESTED)
# ============================================================
print("=" * 60)
print("3. TERNARY BERSARANG (NESTED)")
print("=" * 60)

# Grading dengan nested ternary
nilai = 82
grade = "A" if nilai >= 90 else "B" if nilai >= 80 else "C" if nilai >= 70 else "D" if nilai >= 60 else "E"
print(f"Nilai {nilai}: Grade {grade}")

# Tanda angka
for angka in [-5, 0, 7]:
    tanda = "positif" if angka > 0 else "nol" if angka == 0 else "negatif"
    print(f"  {angka:>3} -> {tanda}")

# Kategori umur
for u in [3, 10, 15, 30, 65]:
    kat = "Balita" if u < 5 else "Anak" if u < 12 else "Remaja" if u < 18 else "Dewasa" if u < 60 else "Lansia"
    print(f"  Umur {u:>2} -> {kat}")
print()


# ============================================================
# 4. TERNARY DALAM LIST COMPREHENSION
# ============================================================
print("=" * 60)
print("4. TERNARY DALAM LIST COMPREHENSION")
print("=" * 60)

# Genap/Ganjil label
angka = list(range(1, 11))
label = ["genap" if x % 2 == 0 else "ganjil" for x in angka]
print(f"Angka: {angka}")
print(f"Label: {label}")

# Lulus/Tidak lulus
nilai_list = [85, 60, 92, 45, 78, 55, 90]
status_list = ["Lulus" if n >= 75 else "Remedial" for n in nilai_list]
print(f"\nNilai:  {nilai_list}")
print(f"Status: {status_list}")

# Absolut value manual
data = [-3, 5, -1, 8, -6, 2]
absolut = [x if x >= 0 else -x for x in data]
print(f"\nData:    {data}")
print(f"Absolut: {absolut}")

# Clamp nilai (min 0, max 100)
raw = [-10, 50, 120, 75, -5, 200, 80]
clamped = [0 if x < 0 else 100 if x > 100 else x for x in raw]
print(f"\nRaw:     {raw}")
print(f"Clamped: {clamped}")

# Replace None dengan default
data = [10, None, 30, None, 50]
cleaned = [x if x is not None else 0 for x in data]
print(f"\nData:    {data}")
print(f"Cleaned: {cleaned}")
print()


# ============================================================
# 5. TERNARY DALAM FUNGSI & LAMBDA
# ============================================================
print("=" * 60)
print("5. TERNARY DALAM FUNGSI & LAMBDA")
print("=" * 60)

# Dalam fungsi
def nilai_absolut(x):
    return x if x >= 0 else -x

print(f"nilai_absolut(-7) = {nilai_absolut(-7)}")
print(f"nilai_absolut(5)  = {nilai_absolut(5)}")

# Dalam lambda
max_val = lambda a, b: a if a > b else b
min_val = lambda a, b: a if a < b else b
print(f"max(10, 25) = {max_val(10, 25)}")
print(f"min(10, 25) = {min_val(10, 25)}")

# Lambda untuk sorting
siswa = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
siswa_sorted = sorted(siswa, key=lambda s: s[1], reverse=True)
print(f"\nSiswa sorted by nilai: {siswa_sorted}")
print()


# ============================================================
# 6. TERNARY DALAM ASSIGNMENT
# ============================================================
print("=" * 60)
print("6. TERNARY DALAM ASSIGNMENT")
print("=" * 60)

# Default value
user_input = ""
nama = user_input if user_input else "Guest"
print(f"Input kosong -> nama = '{nama}'")

user_input = "Budi"
nama = user_input if user_input else "Guest"
print(f"Input 'Budi' -> nama = '{nama}'")

# Min/Max
a, b = 15, 23
terbesar = a if a > b else b
terkecil = a if a < b else b
print(f"\na={a}, b={b}")
print(f"Terbesar: {terbesar}")
print(f"Terkecil: {terkecil}")

# Conditional increment
score = 85
bonus = 10 if score > 80 else 5 if score > 60 else 0
print(f"\nScore: {score}, Bonus: {bonus}, Total: {score + bonus}")
print()


# ============================================================
# 7. TERNARY DALAM DICTIONARY
# ============================================================
print("=" * 60)
print("7. TERNARY DALAM DICTIONARY")
print("=" * 60)

# Conditional dict value
is_vip = True
config = {
    "max_upload": 100 if is_vip else 10,
    "storage": "unlimited" if is_vip else "5GB",
    "support": "priority" if is_vip else "standard",
    "ads": False if is_vip else True,
}
print(f"VIP = {is_vip}")
for key, val in config.items():
    print(f"  {key}: {val}")
print()


# ============================================================
# 8. USE CASES
# ============================================================
print("=" * 60)
print("8. USE CASES")
print("=" * 60)

# --- USE CASE 1: Format Angka ---
print("\n--- USE CASE 1: Format Angka ---")
angka_list = [0, 1, -1, 100, -50, 0.5]
for a in angka_list:
    sign = "+" if a > 0 else "" if a == 0 else ""
    formatted = f"{sign}{a}"
    print(f"  {formatted:>6} -> {'positif' if a > 0 else 'nol' if a == 0 else 'negatif'}")

# --- USE CASE 2: Sapaan Berdasarkan Waktu ---
print("\n--- USE CASE 2: Sapaan Berdasarkan Waktu ---")
for jam in [6, 10, 13, 18, 22]:
    sapaan = "Selamat Pagi" if jam < 12 else "Selamat Siang" if jam < 15 else "Selamat Sore" if jam < 18 else "Selamat Malam"
    print(f"  Jam {jam:02d}:00 -> {sapaan}")

# --- USE CASE 3: Status HTTP ---
print("\n--- USE CASE 3: Status HTTP ---")
for code in [200, 301, 404, 500, 403]:
    status = (
        "OK" if code == 200
        else "Redirect" if code == 301
        else "Not Found" if code == 404
        else "Forbidden" if code == 403
        else "Server Error" if code == 500
        else "Unknown"
    )
    print(f"  HTTP {code}: {status}")

# --- USE CASE 4: Plural/Singular ---
print("\n--- USE CASE 4: Plural/Singular ---")
for jumlah in [0, 1, 5]:
    pesan = f"Tidak ada pesan" if jumlah == 0 else f"{jumlah} pesan baru" if jumlah == 1 else f"{jumlah} pesan baru"
    notif = f"({jumlah})" if jumlah > 0 else ""
    print(f"  Jumlah {jumlah}: {pesan} {notif}")

# --- USE CASE 5: Data Cleaning ---
print("\n--- USE CASE 5: Data Cleaning ---")
raw_data = ["  Alice  ", "", None, "BOB", "  charlie", "  ", "Diana  "]
print(f"Raw:     {raw_data}")
cleaned = [
    name.strip().title() if name and name.strip() else "(unknown)"
    for name in raw_data
]
print(f"Cleaned: {cleaned}")

# --- USE CASE 6: Emoji Rating ---
print("\n--- USE CASE 6: Rating ---")
ratings = [1, 2, 3, 4, 5]
for r in ratings:
    stars = "*" * r + "." * (5 - r)
    label = "Buruk" if r <= 1 else "Kurang" if r <= 2 else "Cukup" if r <= 3 else "Bagus" if r <= 4 else "Sempurna"
    print(f"  [{stars}] {r}/5 - {label}")

print()
print("=" * 60)
print("Selesai! Ternary operator sudah dicontohkan.")
