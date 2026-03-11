"""
=== TIPE DATA PYTHON ===

Python Data Types:
├── Numeric: Integer, Float, Complex Number
├── Dictionary
├── Boolean
├── Set
└── Sequence Type: String, Tuple, List
"""

# ============================================================
# 1. NUMERIC
# ============================================================

# --- Integer ---
bilangan_bulat = 10
negatif = -5
nol = 0

print("=== INTEGER ===")
print(f"bilangan_bulat = {bilangan_bulat}, tipe: {type(bilangan_bulat)}")
print(f"negatif = {negatif}, tipe: {type(negatif)}")
print(f"nol = {nol}, tipe: {type(nol)}")
print()

# --- Float ---
desimal = 3.14
negatif_desimal = -0.5
notasi_ilmiah = 2.5e3  # 2500.0

print("=== FLOAT ===")
print(f"desimal = {desimal}, tipe: {type(desimal)}")
print(f"negatif_desimal = {negatif_desimal}, tipe: {type(negatif_desimal)}")
print(f"notasi_ilmiah = {notasi_ilmiah}, tipe: {type(notasi_ilmiah)}")
print()

# --- Complex Number ---
bilangan_kompleks = 3 + 4j
kompleks2 = complex(2, 5)  # 2 + 5j

print("=== COMPLEX NUMBER ===")
print(f"bilangan_kompleks = {bilangan_kompleks}, tipe: {type(bilangan_kompleks)}")
print(f"kompleks2 = {kompleks2}, tipe: {type(kompleks2)}")
print(f"Real part: {bilangan_kompleks.real}, Imaginary part: {bilangan_kompleks.imag}")
print()


# ============================================================
# 2. DICTIONARY
# ============================================================

mahasiswa = {
    "nama": "Budi",
    "umur": 21,
    "jurusan": "Teknik Informatika",
    "ipk": 3.75
}

print("=== DICTIONARY ===")
print(f"mahasiswa = {mahasiswa}")
print(f"Tipe: {type(mahasiswa)}")
print(f"Nama: {mahasiswa['nama']}")
print(f"Umur: {mahasiswa['umur']}")

# Menambah data baru
mahasiswa["semester"] = 5
print(f"Setelah ditambah semester: {mahasiswa}")

# Mengubah data
mahasiswa["ipk"] = 3.80
print(f"Setelah IPK diubah: {mahasiswa}")

# Menghapus data
del mahasiswa["semester"]
print(f"Setelah semester dihapus: {mahasiswa}")
print()


# ============================================================
# 3. BOOLEAN
# ============================================================

benar = True
salah = False

print("=== BOOLEAN ===")
print(f"benar = {benar}, tipe: {type(benar)}")
print(f"salah = {salah}, tipe: {type(salah)}")
print(f"10 > 5 = {10 > 5}")
print(f"10 < 5 = {10 < 5}")
print(f"10 == 10 = {10 == 10}")
print(f"bool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")
print(f'bool("") = {bool("")}')
print(f'bool("hello") = {bool("hello")}')
print()


# ============================================================
# 4. SET
# ============================================================

buah = {"apel", "jeruk", "mangga", "apel"}  # duplikat otomatis dihapus
angka_set = {1, 2, 3, 4, 5}

print("=== SET ===")
print(f"buah = {buah}, tipe: {type(buah)}")
print(f"angka_set = {angka_set}")

# Operasi Set
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"set_a = {set_a}")
print(f"set_b = {set_b}")
print(f"Union (gabungan): {set_a | set_b}")
print(f"Intersection (irisan): {set_a & set_b}")
print(f"Difference (selisih): {set_a - set_b}")

# Menambah & menghapus elemen
buah.add("semangka")
print(f"Setelah add 'semangka': {buah}")
buah.discard("jeruk")
print(f"Setelah discard 'jeruk': {buah}")
print()


# ============================================================
# 5. SEQUENCE TYPE
# ============================================================

# --- String ---
nama = "Python Programming"
kalimat = 'Belajar Python itu menyenangkan'

print("=== STRING ===")
print(f"nama = '{nama}', tipe: {type(nama)}")
print(f"Huruf pertama: {nama[0]}")
print(f"5 huruf pertama: {nama[:5]}")
print(f"Uppercase: {nama.upper()}")
print(f"Lowercase: {nama.lower()}")
print(f"Panjang string: {len(nama)}")
print(f"Replace: {nama.replace('Python', 'Java')}")
print()

# --- Tuple (tidak bisa diubah setelah dibuat) ---
koordinat = (10, 20)
warna = ("merah", "hijau", "biru")
campuran = (1, "dua", 3.0, True)

print("=== TUPLE ===")
print(f"koordinat = {koordinat}, tipe: {type(koordinat)}")
print(f"warna = {warna}")
print(f"campuran = {campuran}")
print(f"Elemen pertama warna: {warna[0]}")
print(f"Panjang tuple warna: {len(warna)}")
print(f"Jumlah elemen '1' di campuran: {campuran.count(1)}")
print()

# --- List (bisa diubah setelah dibuat) ---
angka = [1, 2, 3, 4, 5]
nama_list = ["Alice", "Bob", "Charlie"]
campuran_list = [1, "dua", 3.0, True]

print("=== LIST ===")
print(f"angka = {angka}, tipe: {type(angka)}")
print(f"nama_list = {nama_list}")
print(f"Elemen pertama: {angka[0]}")
print(f"Elemen terakhir: {angka[-1]}")

# Mengubah elemen
angka[0] = 100
print(f"Setelah angka[0] = 100: {angka}")

# Menambah elemen
angka.append(6)
print(f"Setelah append(6): {angka}")

# Menghapus elemen
angka.remove(100)
print(f"Setelah remove(100): {angka}")

# Sorting
angka.sort()
print(f"Setelah sort(): {angka}")

# Slicing
print(f"angka[1:4] = {angka[1:4]}")
print()

print("=" * 50)
print("Selesai! Semua tipe data sudah dicontohkan.")
