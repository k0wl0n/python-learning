"""
=== ARITHMETIC OPERATORS (Operator Aritmatika) ===

Operator aritmatika digunakan untuk operasi matematika dasar.
"""

a = 15
b = 4

print("=== ARITHMETIC OPERATORS ===")
print(f"a = {a}, b = {b}")
print()

# Penjumlahan
print(f"a + b  = {a + b}")       # 19

# Pengurangan
print(f"a - b  = {a - b}")       # 11

# Perkalian
print(f"a * b  = {a * b}")       # 60

# Pembagian (menghasilkan float)
print(f"a / b  = {a / b}")       # 3.75

# Pembagian bulat (floor division)
print(f"a // b = {a // b}")      # 3

# Modulus (sisa bagi)
print(f"a % b  = {a % b}")       # 3

# Pangkat (exponentiation)
print(f"a ** b = {a ** b}")      # 50625

print()

# --- Contoh penggunaan dalam kehidupan sehari-hari ---
print("=== CONTOH PENGGUNAAN ===")

harga = 25000
jumlah = 3
total = harga * jumlah
print(f"Harga: Rp{harga}, Jumlah: {jumlah}, Total: Rp{total}")

total_siswa = 35
kelompok = 6
per_kelompok = total_siswa // kelompok
sisa = total_siswa % kelompok
print(f"Total siswa: {total_siswa}, Jumlah kelompok: {kelompok}")
print(f"Per kelompok: {per_kelompok} siswa, Sisa: {sisa} siswa")

panjang_sisi = 5
luas_persegi = panjang_sisi ** 2
print(f"Sisi persegi: {panjang_sisi}, Luas: {luas_persegi}")
