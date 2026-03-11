"""
=== CROSS FILE FUNCTION (Import Function dari File Lain) ===

Ada beberapa cara import function dari file lain:

1. import nama_file                        -> akses via nama_file.function()
2. from nama_file import function          -> akses langsung function()
3. from nama_file import func1, func2      -> import beberapa
4. from nama_file import *                 -> import semua (tidak direkomendasikan)
5. import nama_file as alias               -> akses via alias.function()

PENTING:
- File yang di-import harus di folder yang sama, atau di Python path
- Nama file = nama module (tanpa .py)
- File helpers.py di folder yang sama -> import helpers
"""

# ============================================================
# CARA 1: import seluruh module
# ============================================================
print("=" * 60)
print("CARA 1: import helpers")
print("=" * 60)

import helpers

# Akses function via nama_module.nama_function
print(helpers.format_rupiah(1500000))
print(helpers.format_persen(85.5))
print(helpers.format_nama("  budi santoso  "))
print()


# ============================================================
# CARA 2: from module import specific functions
# ============================================================
print("=" * 60)
print("CARA 2: from helpers import ...")
print("=" * 60)

from helpers import hitung_diskon, hitung_pajak, format_rupiah

# Akses langsung tanpa prefix module
harga = 500000
diskon = 20
harga_diskon = hitung_diskon(harga, diskon)
pajak = hitung_pajak(harga_diskon)
total = harga_diskon + pajak

print(f"Harga awal:     {format_rupiah(harga)}")
print(f"Diskon {diskon}%:      {format_rupiah(harga - harga_diskon)}")
print(f"Harga diskon:   {format_rupiah(harga_diskon)}")
print(f"Pajak:          {format_rupiah(pajak)}")
print(f"Total:          {format_rupiah(total)}")
print()


# ============================================================
# CARA 3: import dengan alias
# ============================================================
print("=" * 60)
print("CARA 3: import helpers as h")
print("=" * 60)

import helpers as h

print(f"BMI(70kg, 1.75m) = {h.hitung_bmi(70, 1.75):.1f}")
print(f"37°C = {h.celcius_ke_fahrenheit(37):.1f}°F")
print(f"100°F = {h.fahrenheit_ke_celcius(100):.1f}°C")
print()


# ============================================================
# CARA 4: Import validation functions
# ============================================================
print("=" * 60)
print("CARA 4: Menggunakan Validation Functions")
print("=" * 60)

from helpers import is_valid_email, is_valid_phone, is_strong_password

# Test email validation
emails = ["user@email.com", "invalid-email", "test@", "@domain.com", "a@b.c"]
print("Email validation:")
for email in emails:
    valid = is_valid_email(email)
    status = "✅ Valid" if valid else "❌ Invalid"
    print(f"  {email:<20} -> {status}")

# Test phone validation
phones = ["08123456789", "+6281234567890", "12345", "081-234-567"]
print("\nPhone validation:")
for phone in phones:
    valid = is_valid_phone(phone)
    status = "✅ Valid" if valid else "❌ Invalid"
    print(f"  {phone:<20} -> {status}")

# Test password validation
passwords = ["123", "password", "Password1", "Ab1cdefgh"]
print("\nPassword validation:")
for pw in passwords:
    valid, pesan = is_strong_password(pw)
    status = f"✅ {pesan}" if valid else f"❌ {pesan}"
    print(f"  {pw:<15} -> {status}")
print()


# ============================================================
# CARA 5: Import data processing functions
# ============================================================
print("=" * 60)
print("CARA 5: Data Processing dari helpers")
print("=" * 60)

from helpers import hitung_statistik, cari_item, filter_data, nilai_ke_grade

# Statistik
nilai = [85, 92, 78, 95, 88, 72, 90, 65, 80]
stats = hitung_statistik(nilai)
print(f"Data:  {nilai}")
print(f"Stats: {stats}")
print()

# Cari item
mahasiswa = [
    {"nim": "001", "nama": "Alice", "ipk": 3.8},
    {"nim": "002", "nama": "Bob", "ipk": 3.2},
    {"nim": "003", "nama": "Charlie", "ipk": 3.5},
]

result = cari_item(mahasiswa, "nim", "002")
print(f"Cari NIM 002: {result}")

result = cari_item(mahasiswa, "nama", "Diana")
print(f"Cari Diana:   {result}")
print()

# Filter data
ipk_tinggi = filter_data(mahasiswa, "ipk", lambda x: x >= 3.5)
print(f"IPK >= 3.5: {ipk_tinggi}")

# Grade
print("\nNilai -> Grade:")
for n in [95, 82, 71, 63, 45]:
    print(f"  {n} -> {nilai_ke_grade(n)}")


# ============================================================
# BONUS: __name__ == "__main__"
# ============================================================
print("\n" + "=" * 60)
print("BONUS: __name__ == '__main__'")
print("=" * 60)

print(f"""
Saat menjalankan file ini langsung:
    python 06_cross_file_function.py
    -> __name__ = '__main__'

Saat file ini di-import dari file lain:
    import 06_cross_file_function
    -> __name__ = '06_cross_file_function'

Di helpers.py ada:
    if __name__ == "__main__":
        # kode ini HANYA jalan kalau helpers.py dijalankan langsung
        # TIDAK jalan kalau helpers.py di-import

Ini berguna untuk:
  - Menulis test di dalam file module
  - Membedakan behavior saat import vs saat run langsung
""")

print("=" * 60)
print("Selesai! Cross file function sudah dicontohkan.")
