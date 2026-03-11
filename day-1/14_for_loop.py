"""
=== FOR LOOP ===

Struktur:
    for variabel in iterable:
        # kode dijalankan untuk setiap elemen

Iterable: list, tuple, string, range, dictionary, set, file, dll.
"""

# ============================================================
# 1. FOR DASAR
# ============================================================
print("=" * 60)
print("1. FOR DASAR")
print("=" * 60)

# Loop list
buah = ["apel", "jeruk", "mangga", "pisang"]
print("Daftar buah:")
for b in buah:
    print(f"  - {b}")
print()

# Loop string
kata = "PYTHON"
print(f"Huruf di '{kata}':")
for huruf in kata:
    print(f"  {huruf}", end="")
print()
print()

# Loop tuple
koordinat_list = [(1, 2), (3, 4), (5, 6)]
print("Koordinat:")
for x, y in koordinat_list:
    print(f"  ({x}, {y})")
print()


# ============================================================
# 2. FOR DENGAN RANGE()
# ============================================================
print("=" * 60)
print("2. FOR DENGAN RANGE()")
print("=" * 60)

# range(stop)
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
print("range(3, 8):", end=" ")
for i in range(3, 8):
    print(i, end=" ")
print()

# range(start, stop, step)
print("range(0, 20, 3):", end=" ")
for i in range(0, 20, 3):
    print(i, end=" ")
print()

# Hitung mundur
print("range(10, 0, -1):", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
print()
print()


# ============================================================
# 3. FOR DENGAN ENUMERATE()
# ============================================================
print("=" * 60)
print("3. FOR DENGAN ENUMERATE()")
print("=" * 60)

bahasa = ["Python", "JavaScript", "Go", "Rust", "Java"]

# Tanpa enumerate (cara lama)
print("Tanpa enumerate:")
for i in range(len(bahasa)):
    print(f"  {i}. {bahasa[i]}")

# Dengan enumerate (cara pythonic)
print("\nDengan enumerate:")
for i, b in enumerate(bahasa):
    print(f"  {i}. {b}")

# enumerate dengan start index
print("\nenumerate(start=1):")
for no, b in enumerate(bahasa, 1):
    print(f"  {no}. {b}")
print()


# ============================================================
# 4. FOR DENGAN ZIP()
# ============================================================
print("=" * 60)
print("4. FOR DENGAN ZIP()")
print("=" * 60)

nama = ["Alice", "Bob", "Charlie", "Diana"]
umur = [22, 25, 21, 23]
kota = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta"]

print("Data mahasiswa:")
for n, u, k in zip(nama, umur, kota):
    print(f"  {n} ({u} thn) dari {k}")
print()

# Membuat dictionary dari 2 list
keys = ["nama", "umur", "kota"]
values = ["Budi", 25, "Jakarta"]
data = dict(zip(keys, values))
print(f"dict(zip(...)): {data}")
print()


# ============================================================
# 5. FOR DENGAN DICTIONARY
# ============================================================
print("=" * 60)
print("5. FOR DENGAN DICTIONARY")
print("=" * 60)

mahasiswa = {
    "nama": "Budi Santoso",
    "nim": "2024001",
    "jurusan": "Teknik Informatika",
    "ipk": 3.75
}

# Loop keys
print("Keys:")
for key in mahasiswa:
    print(f"  {key}")

# Loop values
print("\nValues:")
for value in mahasiswa.values():
    print(f"  {value}")

# Loop items (key + value)
print("\nItems:")
for key, value in mahasiswa.items():
    print(f"  {key}: {value}")
print()


# ============================================================
# 6. FOR DENGAN BREAK DAN CONTINUE
# ============================================================
print("=" * 60)
print("6. FOR DENGAN BREAK DAN CONTINUE")
print("=" * 60)

# Break
print("Cari angka pertama > 50:")
angka = [12, 35, 8, 55, 23, 67, 4]
for a in angka:
    if a > 50:
        print(f"  Ditemukan: {a}")
        break
    print(f"  Cek: {a} (bukan)")

# Continue
print("\nSkip angka negatif:")
data = [5, -3, 8, -1, 12, -7, 15]
total = 0
for d in data:
    if d < 0:
        print(f"  Skip: {d}")
        continue
    total += d
    print(f"  Proses: {d}")
print(f"Total (positif saja): {total}")

# For-else
print("\nCari bilangan prima:")
n = 17
for i in range(2, n):
    if n % i == 0:
        print(f"  {n} bukan prima (bisa dibagi {i})")
        break
else:
    print(f"  {n} adalah bilangan PRIMA!")
print()


# ============================================================
# 7. NESTED FOR (FOR BERSARANG)
# ============================================================
print("=" * 60)
print("7. NESTED FOR (FOR BERSARANG)")
print("=" * 60)

# Tabel perkalian
print("Tabel Perkalian:")
print(f"  {'':>3}", end="")
for j in range(1, 6):
    print(f"{j:>4}", end="")
print()
print("  " + "-" * 23)

for i in range(1, 6):
    print(f"  {i:>2} |", end="")
    for j in range(1, 6):
        print(f"{i * j:>4}", end="")
    print()

# Pola bintang
print("\nPola piramida:")
for i in range(1, 6):
    print("  " + " " * (5 - i) + "* " * i)

# Pola angka
print("\nPola angka:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()


# ============================================================
# 8. LIST / DICT / SET COMPREHENSION
# ============================================================
print("=" * 60)
print("8. COMPREHENSION")
print("=" * 60)

# List comprehension
kuadrat = [x ** 2 for x in range(1, 11)]
print(f"Kuadrat 1-10:    {kuadrat}")

genap = [x for x in range(1, 21) if x % 2 == 0]
print(f"Genap 1-20:      {genap}")

# Dict comprehension
kuadrat_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Dict kuadrat:    {kuadrat_dict}")

# Set comprehension
huruf = {char.lower() for char in "Hello World" if char.isalpha()}
print(f"Huruf unik:      {huruf}")

# Nested comprehension
matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
print(f"Matrix 3x3:      {matrix}")
print()


# ============================================================
# 9. TEKNIK LOOP BERGUNA
# ============================================================
print("=" * 60)
print("9. TEKNIK LOOP BERGUNA")
print("=" * 60)

# reversed()
print("Reversed:")
for b in reversed(buah):
    print(f"  {b}", end="")
print()

# sorted()
angka = [5, 2, 8, 1, 9, 3]
print(f"\nSorted {angka}:")
for a in sorted(angka):
    print(f"  {a}", end="")
print()

# Unique (via set, urutan mungkin berubah)
duplikat = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print(f"\nUnique dari {duplikat}: {sorted(set(duplikat))}")

# Looping dengan index menggunakan range(len())
print(f"\nUpdate elemen langsung:")
scores = [70, 85, 60, 90, 75]
print(f"  Sebelum: {scores}")
for i in range(len(scores)):
    scores[i] += 5  # tambah 5 bonus
print(f"  Sesudah (+5 bonus): {scores}")
print()


# ============================================================
# 10. USE CASES
# ============================================================
print("=" * 60)
print("10. USE CASES")
print("=" * 60)

# --- USE CASE 1: Statistik Nilai ---
print("\n--- USE CASE 1: Statistik Nilai ---")
nilai = [85, 92, 78, 95, 88, 72, 90, 65, 80, 98]
print(f"Nilai: {nilai}")

tertinggi = nilai[0]
terendah = nilai[0]
total = 0
lulus = 0

for n in nilai:
    total += n
    if n > tertinggi:
        tertinggi = n
    if n < terendah:
        terendah = n
    if n >= 75:
        lulus += 1

print(f"Tertinggi:  {tertinggi}")
print(f"Terendah:   {terendah}")
print(f"Rata-rata:  {total / len(nilai):.1f}")
print(f"Lulus (≥75): {lulus}/{len(nilai)} ({lulus / len(nilai) * 100:.0f}%)")

# --- USE CASE 2: Word Counter ---
print("\n--- USE CASE 2: Word Counter ---")
teks = "python adalah bahasa python yang mudah dipelajari python sangat populer"
kata_list = teks.split()
word_count = {}
for kata in kata_list:
    if kata in word_count:
        word_count[kata] += 1
    else:
        word_count[kata] = 1

for kata, jumlah in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    bar = "█" * jumlah
    print(f"  {kata:<15} {jumlah}x {bar}")

# --- USE CASE 3: Cetak Nota ---
print("\n--- USE CASE 3: Cetak Nota ---")
pesanan = [
    ("Nasi Goreng", 2, 25000),
    ("Es Teh", 3, 5000),
    ("Sate Ayam", 1, 35000),
    ("Kerupuk", 2, 3000),
]

print("╔══════════════════════════════════════╗")
print("║          WARUNG MAKAN ENAK           ║")
print("╠══════════════════════════════════════╣")
grand_total = 0
for item, qty, harga in pesanan:
    subtotal = qty * harga
    grand_total += subtotal
    print(f"║ {item:<15} {qty}x Rp{harga:>7,} = Rp{subtotal:>7,} ║")
print("╠══════════════════════════════════════╣")
print(f"║ {'TOTAL':<26} Rp{grand_total:>7,} ║")
print("╚══════════════════════════════════════╝")

# --- USE CASE 4: Bilangan Prima ---
print("\n--- USE CASE 4: Bilangan Prima 1-50 ---")
prima = []
for num in range(2, 51):
    is_prima = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prima = False
            break
    if is_prima:
        prima.append(num)
print(f"Bilangan prima: {prima}")

# --- USE CASE 5: Flatten & Process ---
print("\n--- USE CASE 5: Flatten & Process Data ---")
data_kelas = {
    "Kelas A": [80, 85, 90, 75],
    "Kelas B": [70, 88, 92, 78],
    "Kelas C": [95, 82, 77, 86],
}

for kelas, nilai_list in data_kelas.items():
    rata2 = sum(nilai_list) / len(nilai_list)
    tertinggi = max(nilai_list)
    print(f"  {kelas}: Rata-rata={rata2:.1f}, Tertinggi={tertinggi}")

print()
print("=" * 60)
print("Selesai! For loop sudah dicontohkan.")
