"""
=== ARRAY LENGKAP - BANYAK CONTOH & USE CASES ===

Python punya 3 cara utama untuk bekerja dengan array:
1. List       - paling umum, fleksibel, bisa campur tipe data
2. array.array - dari module array, satu tipe data saja, lebih hemat memori
3. numpy.ndarray - untuk komputasi numerik berat (perlu install numpy)

File ini fokus pada List dan array.array.
"""

from array import array

# ============================================================
# BAGIAN 1: MEMBUAT ARRAY / LIST
# ============================================================
print("=" * 60)
print("BAGIAN 1: MEMBUAT ARRAY / LIST")
print("=" * 60)

# --- Berbagai cara membuat list ---
kosong = []
angka = [1, 2, 3, 4, 5]
campuran = [1, "dua", 3.0, True, None]
nested = [[1, 2], [3, 4], [5, 6]]
dari_range = list(range(1, 11))
dari_string = list("Hello")
pengulangan = [0] * 10
comprehension = [x ** 2 for x in range(1, 6)]

print(f"kosong         = {kosong}")
print(f"angka          = {angka}")
print(f"campuran       = {campuran}")
print(f"nested         = {nested}")
print(f"dari_range     = {dari_range}")
print(f"dari_string    = {dari_string}")
print(f"pengulangan    = {pengulangan}")
print(f"comprehension  = {comprehension}")
print()

# --- Membuat array.array ---
arr_int = array('i', [10, 20, 30, 40, 50])
arr_float = array('f', [1.1, 2.2, 3.3])
arr_double = array('d', [1.111, 2.222, 3.333])
arr_dari_range = array('i', range(1, 11))

print(f"arr_int        = {arr_int}")
print(f"arr_float      = {arr_float}")
print(f"arr_double     = {arr_double}")
print(f"arr_dari_range = {arr_dari_range}")
print()


# ============================================================
# BAGIAN 2: MENGAKSES ELEMEN (INDEXING & SLICING)
# ============================================================
print("=" * 60)
print("BAGIAN 2: MENGAKSES ELEMEN")
print("=" * 60)

buah = ["apel", "jeruk", "mangga", "pisang", "semangka", "durian"]
print(f"buah = {buah}")
print()

# Indexing
print(f"buah[0]   = '{buah[0]}'")       # pertama
print(f"buah[2]   = '{buah[2]}'")       # ketiga
print(f"buah[-1]  = '{buah[-1]}'")      # terakhir
print(f"buah[-2]  = '{buah[-2]}'")      # kedua dari belakang

# Slicing [start:stop:step]
print(f"buah[1:4]   = {buah[1:4]}")     # index 1,2,3
print(f"buah[:3]    = {buah[:3]}")       # 3 pertama
print(f"buah[3:]    = {buah[3:]}")       # dari index 3 sampai akhir
print(f"buah[::2]   = {buah[::2]}")     # lompat 2
print(f"buah[::-1]  = {buah[::-1]}")    # balik urutan

# Nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nmatrix = {matrix}")
print(f"matrix[0]    = {matrix[0]}")
print(f"matrix[1][2] = {matrix[1][2]}")   # baris 1, kolom 2 = 6
print(f"matrix[2][0] = {matrix[2][0]}")   # baris 2, kolom 0 = 7
print()


# ============================================================
# BAGIAN 3: MENAMBAH ELEMEN
# ============================================================
print("=" * 60)
print("BAGIAN 3: MENAMBAH ELEMEN")
print("=" * 60)

hewan = ["kucing", "anjing"]
print(f"Awal: {hewan}")

# append() - tambah di akhir
hewan.append("kelinci")
print(f"append('kelinci'):       {hewan}")

# insert() - tambah di posisi tertentu
hewan.insert(1, "hamster")
print(f"insert(1, 'hamster'):    {hewan}")

# insert di awal
hewan.insert(0, "ikan")
print(f"insert(0, 'ikan'):       {hewan}")

# extend() - tambah banyak elemen
hewan.extend(["burung", "kura-kura"])
print(f"extend(['burung',..]):   {hewan}")

# Concatenation dengan +
hewan_baru = hewan + ["iguana"]
print(f"hewan + ['iguana']:      {hewan_baru}")

# Menggunakan += (sama dengan extend)
hewan += ["ular"]
print(f"hewan += ['ular']:       {hewan}")

# Menyisipkan list ke dalam list
hewan[2:2] = ["bebek", "angsa"]
print(f"hewan[2:2] = [...]:      {hewan}")
print()


# ============================================================
# BAGIAN 4: MENGHAPUS ELEMEN
# ============================================================
print("=" * 60)
print("BAGIAN 4: MENGHAPUS ELEMEN")
print("=" * 60)

angka = [10, 20, 30, 40, 50, 30, 60]
print(f"Awal: {angka}")

# remove() - hapus elemen pertama yang cocok
angka.remove(30)
print(f"remove(30):   {angka}")    # hanya 30 pertama yang dihapus

# pop() - hapus berdasarkan index, return elemennya
dihapus = angka.pop()
print(f"pop():        {angka} (dihapus: {dihapus})")

dihapus = angka.pop(1)
print(f"pop(1):       {angka} (dihapus: {dihapus})")

# del - hapus berdasarkan index atau slice
del angka[0]
print(f"del angka[0]: {angka}")

# Hapus range dengan slice
angka2 = [1, 2, 3, 4, 5, 6, 7, 8]
del angka2[2:5]
print(f"del angka2[2:5]: {angka2}")   # [1, 2, 6, 7, 8]

# clear() - hapus semua elemen
sementara = [1, 2, 3]
sementara.clear()
print(f"clear():      {sementara}")
print()


# ============================================================
# BAGIAN 5: MENGUBAH ELEMEN
# ============================================================
print("=" * 60)
print("BAGIAN 5: MENGUBAH ELEMEN")
print("=" * 60)

warna = ["merah", "hijau", "biru", "kuning", "ungu"]
print(f"Awal: {warna}")

# Ubah satu elemen
warna[1] = "emas"
print(f"warna[1] = 'emas':    {warna}")

# Ubah beberapa elemen sekaligus
warna[2:4] = ["perak", "perunggu"]
print(f"warna[2:4] = [...]:   {warna}")

# Ubah dengan jumlah berbeda (bisa memperpanjang/memperpendek)
warna[1:3] = ["hitam", "putih", "abu-abu"]
print(f"warna[1:3] = [3 item]: {warna}")
print()


# ============================================================
# BAGIAN 6: MENCARI & MENGURUTKAN
# ============================================================
print("=" * 60)
print("BAGIAN 6: MENCARI & MENGURUTKAN")
print("=" * 60)

nilai = [85, 92, 78, 95, 88, 72, 95, 100]
print(f"nilai = {nilai}")

# Mencari
print(f"95 in nilai       = {95 in nilai}")
print(f"60 in nilai       = {60 in nilai}")
print(f"nilai.index(95)   = {nilai.index(95)}")       # posisi pertama
print(f"nilai.count(95)   = {nilai.count(95)}")        # jumlah kemunculan
print(f"min(nilai)        = {min(nilai)}")
print(f"max(nilai)        = {max(nilai)}")
print(f"sum(nilai)        = {sum(nilai)}")
print(f"len(nilai)        = {len(nilai)}")
print(f"Rata-rata         = {sum(nilai) / len(nilai):.2f}")

# Mengurutkan
print(f"\nsorted(nilai)             = {sorted(nilai)}")
print(f"sorted(nilai, reverse=True) = {sorted(nilai, reverse=True)}")

nilai_copy = nilai.copy()
nilai_copy.sort()
print(f"nilai.sort()              = {nilai_copy}")

nilai_copy.reverse()
print(f"Setelah reverse()         = {nilai_copy}")
print()


# ============================================================
# BAGIAN 7: LIST COMPREHENSION
# ============================================================
print("=" * 60)
print("BAGIAN 7: LIST COMPREHENSION")
print("=" * 60)

# Kuadrat
kuadrat = [x ** 2 for x in range(1, 11)]
print(f"Kuadrat 1-10:   {kuadrat}")

# Genap saja
genap = [x for x in range(1, 21) if x % 2 == 0]
print(f"Genap 1-20:     {genap}")

# Ganjil saja
ganjil = [x for x in range(1, 21) if x % 2 != 0]
print(f"Ganjil 1-20:    {ganjil}")

# Dengan kondisi if-else
label = ["genap" if x % 2 == 0 else "ganjil" for x in range(1, 6)]
print(f"Label 1-5:      {label}")

# Huruf besar
nama_list = ["alice", "bob", "charlie"]
upper_list = [nama.upper() for nama in nama_list]
print(f"Upper:          {upper_list}")

# Flatten nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for baris in matrix for item in baris]
print(f"Flatten matrix: {flat}")

# Filter dan transformasi
harga = [15000, 25000, 8000, 50000, 12000, 35000]
mahal = [h for h in harga if h > 20000]
print(f"Harga > 20000:  {mahal}")

diskon = [int(h * 0.9) for h in harga]
print(f"Diskon 10%:     {diskon}")
print()


# ============================================================
# BAGIAN 8: COPY ARRAY
# ============================================================
print("=" * 60)
print("BAGIAN 8: COPY ARRAY")
print("=" * 60)

# Shallow copy vs reference
asli = [1, 2, 3, 4, 5]
referensi = asli           # hanya referensi, bukan copy
copy_slice = asli[:]       # shallow copy via slicing
copy_method = asli.copy()  # shallow copy via method
copy_list = list(asli)     # shallow copy via constructor

referensi[0] = 999
print(f"asli setelah referensi[0]=999: {asli}")  # ikut berubah!

copy_method[0] = 888
print(f"asli setelah copy[0]=888:      {asli}")  # tidak berubah

# Deep copy untuk nested list
import copy
nested_asli = [[1, 2], [3, 4]]
shallow = nested_asli.copy()
deep = copy.deepcopy(nested_asli)

nested_asli[0][0] = 999
print(f"\nnested_asli = {nested_asli}")
print(f"shallow     = {shallow}")    # ikut berubah!
print(f"deep        = {deep}")       # tidak berubah
print()


# ============================================================
# BAGIAN 9: USE CASES
# ============================================================
print("=" * 60)
print("BAGIAN 9: USE CASES (CONTOH KASUS)")
print("=" * 60)

# --- USE CASE 1: Daftar Belanja ---
print("\n--- USE CASE 1: Daftar Belanja ---")
belanja = []
belanja.append({"item": "Beras", "harga": 65000, "qty": 2})
belanja.append({"item": "Telur", "harga": 28000, "qty": 1})
belanja.append({"item": "Minyak", "harga": 35000, "qty": 1})
belanja.append({"item": "Gula", "harga": 15000, "qty": 3})

total = 0
print(f"{'No':<4} {'Item':<12} {'Harga':>10} {'Qty':>5} {'Subtotal':>12}")
print("-" * 45)
for i, item in enumerate(belanja, 1):
    subtotal = item["harga"] * item["qty"]
    total += subtotal
    print(f"{i:<4} {item['item']:<12} Rp{item['harga']:>8,} {item['qty']:>5} Rp{subtotal:>10,}")
print("-" * 45)
print(f"{'TOTAL':>17} {'':>16} Rp{total:>10,}")

# --- USE CASE 2: Sistem Nilai Mahasiswa ---
print("\n--- USE CASE 2: Sistem Nilai Mahasiswa ---")
nilai_mhs = [
    {"nama": "Alice", "nilai": [85, 90, 78, 92]},
    {"nama": "Bob", "nilai": [70, 65, 80, 75]},
    {"nama": "Charlie", "nilai": [95, 88, 92, 98]},
    {"nama": "Diana", "nilai": [60, 55, 70, 65]},
]

print(f"{'Nama':<12} {'Nilai':<25} {'Rata-rata':>10} {'Grade':>6}")
print("-" * 55)
for mhs in nilai_mhs:
    rata2 = sum(mhs["nilai"]) / len(mhs["nilai"])
    if rata2 >= 85:
        grade = "A"
    elif rata2 >= 75:
        grade = "B"
    elif rata2 >= 65:
        grade = "C"
    else:
        grade = "D"
    print(f"{mhs['nama']:<12} {str(mhs['nilai']):<25} {rata2:>10.2f} {grade:>6}")

# --- USE CASE 3: Stack (LIFO) ---
print("\n--- USE CASE 3: Stack (LIFO) ---")
stack = []
for item in ["halaman_utama", "produk", "detail_produk", "checkout"]:
    stack.append(item)
    print(f"  Push: {item:<20} Stack: {stack}")

print("  --- User menekan tombol Back ---")
while stack:
    halaman = stack.pop()
    print(f"  Pop:  {halaman:<20} Stack: {stack}")

# --- USE CASE 4: Queue (FIFO) ---
print("\n--- USE CASE 4: Queue (FIFO) ---")
antrian = []
for orang in ["Pak Budi", "Bu Siti", "Mas Andi", "Mbak Rina"]:
    antrian.append(orang)
    print(f"  Masuk: {orang:<12} Antrian: {antrian}")

print("  --- Mulai dilayani ---")
while antrian:
    dilayani = antrian.pop(0)
    print(f"  Layani: {dilayani:<12} Sisa: {antrian}")

# --- USE CASE 5: Sensor Data (array.array) ---
print("\n--- USE CASE 5: Sensor Data (array.array) ---")
suhu_harian = array('f', [28.5, 29.1, 30.2, 27.8, 31.5, 29.9, 28.3])
hari = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]

print("Suhu harian minggu ini:")
for h, s in zip(hari, suhu_harian):
    bar = "█" * int(s - 25)
    print(f"  {h}: {s:.1f}°C {bar}")

suhu_list = suhu_harian.tolist()
print(f"\n  Rata-rata: {sum(suhu_list) / len(suhu_list):.1f}°C")
print(f"  Tertinggi: {max(suhu_list):.1f}°C")
print(f"  Terendah:  {min(suhu_list):.1f}°C")

# --- USE CASE 6: Matrix Operations ---
print("\n--- USE CASE 6: Matrix Operations ---")
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

penjumlahan = [[matrix_a[i][j] + matrix_b[i][j] for j in range(2)] for i in range(2)]
print(f"Matrix A: {matrix_a}")
print(f"Matrix B: {matrix_b}")
print(f"A + B:    {penjumlahan}")

transpose = [[matrix_a[j][i] for j in range(2)] for i in range(2)]
print(f"Transpose A: {transpose}")

# --- USE CASE 7: Frequency Counter ---
print("\n--- USE CASE 7: Frequency Counter ---")
kata = "abracadabra"
huruf_unik = sorted(set(kata))
print(f"Kata: '{kata}'")
for h in huruf_unik:
    jumlah = kata.count(h)
    bar = "■" * jumlah
    print(f"  '{h}': {jumlah}x {bar}")

print()
print("=" * 60)
print("Selesai! Array lengkap sudah dicontohkan.")
