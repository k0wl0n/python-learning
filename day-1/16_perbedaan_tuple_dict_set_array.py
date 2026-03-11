"""
=== PERBEDAAN TUPLE, DICTIONARY, SET, dan ARRAY (LIST) ===

╔═══════════════╦══════════════╦══════════════╦══════════════╦══════════════╗
║               ║    LIST      ║    TUPLE     ║  DICTIONARY  ║     SET      ║
╠═══════════════╬══════════════╬══════════════╬══════════════╬══════════════╣
║ Simbol        ║  [ ]         ║  ( )         ║  { key:val } ║  { }         ║
║ Bisa diubah?  ║  Ya (mutable)║  Tidak       ║  Ya (mutable)║  Ya (mutable)║
║ Urutan?       ║  Ya (ordered)║  Ya (ordered)║  Ya (3.7+)   ║  Tidak       ║
║ Duplikat?     ║  Boleh       ║  Boleh       ║  Key unik    ║  Tidak boleh ║
║ Indexing?     ║  Ya [0],[1]  ║  Ya [0],[1]  ║  Via key     ║  Tidak bisa  ║
║ Kapan pakai?  ║  Data umum   ║  Data tetap  ║  Key-Value   ║  Data unik   ║
╚═══════════════╩══════════════╩══════════════╩══════════════╩══════════════╝
"""

# ============================================================
# 1. CARA MEMBUAT
# ============================================================
print("=" * 60)
print("1. CARA MEMBUAT")
print("=" * 60)

# LIST - pakai [ ]
# Gunakan saat: butuh koleksi data yang bisa diubah-ubah
my_list = [1, 2, 3, 4, 5]

# TUPLE - pakai ( )
# Gunakan saat: data tidak boleh berubah (koordinat, config, konstanta)
my_tuple = (1, 2, 3, 4, 5)

# DICTIONARY - pakai { key: value }
# Gunakan saat: butuh pasangan label-nilai (seperti database record)
my_dict = {"nama": "Budi", "umur": 25, "kota": "Jakarta"}

# SET - pakai { } tanpa key:value
# Gunakan saat: butuh data unik, cek keanggotaan cepat, operasi himpunan
my_set = {1, 2, 3, 4, 5}

print(f"List:       {my_list}       -> type: {type(my_list).__name__}")
print(f"Tuple:      {my_tuple}       -> type: {type(my_tuple).__name__}")
print(f"Dictionary: {my_dict} -> type: {type(my_dict).__name__}")
print(f"Set:        {my_set}       -> type: {type(my_set).__name__}")
print()


# ============================================================
# 2. MUTABLE vs IMMUTABLE (Bisa diubah vs Tidak)
# ============================================================
print("=" * 60)
print("2. MUTABLE vs IMMUTABLE")
print("=" * 60)

# LIST - MUTABLE (bisa diubah)
# Cocok untuk: daftar belanja, todo list, data yang sering berubah
daftar = [10, 20, 30]
daftar[0] = 99                     # bisa ubah elemen
daftar.append(40)                  # bisa tambah elemen
print(f"List  (mutable):   {daftar}  -> bisa diubah")

# TUPLE - IMMUTABLE (tidak bisa diubah)
# Cocok untuk: koordinat, warna RGB, data yang harus tetap
data = (10, 20, 30)
try:
    data[0] = 99                   # akan ERROR!
except TypeError as e:
    print(f"Tuple (immutable): {data}     -> ERROR: {e}")

# DICTIONARY - MUTABLE (bisa diubah)
# Cocok untuk: profil user, config aplikasi, data dengan label
info = {"nama": "Andi"}
info["umur"] = 20                  # bisa tambah key baru
info["nama"] = "Budi"             # bisa ubah value
print(f"Dict  (mutable):   {info}  -> bisa diubah")

# SET - MUTABLE (bisa diubah, tapi elemennya harus immutable)
# Cocok untuk: tag, kategori, filter duplikat
angka = {1, 2, 3}
angka.add(4)                       # bisa tambah
angka.discard(1)                   # bisa hapus
print(f"Set   (mutable):   {angka}        -> bisa diubah, tapi TANPA duplikat")
print()


# ============================================================
# 3. ORDERED vs UNORDERED (Berurutan vs Tidak)
# ============================================================
print("=" * 60)
print("3. ORDERED vs UNORDERED")
print("=" * 60)

# LIST & TUPLE - ORDERED (urutan terjaga, bisa di-index)
# Artinya: elemen pertama yang dimasukkan tetap di posisi pertama
print("List  [0]:", [10, 20, 30][0])     # bisa akses via index
print("Tuple [1]:", (10, 20, 30)[1])     # bisa akses via index

# DICTIONARY - ORDERED (sejak Python 3.7+)
# Urutan insertion terjaga, tapi akses via KEY bukan index
profil = {"a": 1, "b": 2, "c": 3}
print(f"Dict key 'b': {profil['b']}")     # akses via key

# SET - UNORDERED (tidak ada urutan, tidak bisa di-index)
# Artinya: tidak bisa prediksi urutan elemen
warna = {"merah", "hijau", "biru"}
print(f"Set: {warna}")                     # urutan bisa berubah-ubah
try:
    print(warna[0])                        # akan ERROR!
except TypeError as e:
    print(f"Set[0] -> ERROR: {e}")
print()


# ============================================================
# 4. DUPLIKAT
# ============================================================
print("=" * 60)
print("4. DUPLIKAT")
print("=" * 60)

# LIST - BOLEH duplikat
# Berguna saat: perlu hitung frekuensi, data bisa sama
list_dup = [1, 2, 2, 3, 3, 3]
print(f"List  {list_dup}  -> duplikat DIPERBOLEHKAN")

# TUPLE - BOLEH duplikat
tuple_dup = (1, 2, 2, 3, 3, 3)
print(f"Tuple {tuple_dup}  -> duplikat DIPERBOLEHKAN")

# DICTIONARY - KEY harus unik (value boleh duplikat)
# Key terakhir yang menang jika ada duplikat
dict_dup = {"a": 1, "b": 2, "a": 99}     # key 'a' ditimpa
print(f"Dict  {dict_dup}      -> key HARUS unik (yang terakhir menang)")

# SET - TIDAK BOLEH duplikat (otomatis dihapus)
# Berguna saat: butuh data unik
set_dup = {1, 2, 2, 3, 3, 3}
print(f"Set   {set_dup}          -> duplikat OTOMATIS dihapus")
print()


# ============================================================
# 5. OPERASI UMUM - PERBANDINGAN
# ============================================================
print("=" * 60)
print("5. OPERASI UMUM - PERBANDINGAN")
print("=" * 60)

print("\n--- MENAMBAH ELEMEN ---")

# List: append, insert, extend
fruits = ["apel"]
fruits.append("jeruk")             # tambah di akhir
fruits.insert(0, "mangga")        # tambah di posisi tertentu
print(f"List  append/insert: {fruits}")

# Tuple: tidak bisa! harus buat baru
t = (1, 2)
t = t + (3,)                      # buat tuple BARU dengan concatenation
print(f"Tuple concatenation: {t}  (buat objek baru)")

# Dict: tambah key baru
d = {"nama": "Andi"}
d["umur"] = 20                    # langsung assign key baru
print(f"Dict  tambah key:    {d}")

# Set: add
s = {1, 2}
s.add(3)                          # tambah elemen
print(f"Set   add:           {s}")

print("\n--- MENGHAPUS ELEMEN ---")

# List: remove, pop, del
fruits.remove("jeruk")            # hapus by value
print(f"List  remove:  {fruits}")

# Tuple: tidak bisa hapus elemen!
print(f"Tuple: TIDAK BISA hapus elemen (immutable)")

# Dict: del, pop
d.pop("umur")                     # hapus by key
print(f"Dict  pop:     {d}")

# Set: discard, remove
s.discard(2)                      # hapus by value (aman jika tidak ada)
print(f"Set   discard: {s}")

print("\n--- MENGECEK KEANGGOTAAN (in) ---")
# Semua support 'in', tapi SET paling CEPAT
print(f"'apel' in list  {fruits}:  {'apel' in fruits}")
print(f"2 in tuple {(1,2,3)}:        {2 in (1, 2, 3)}")
print(f"'nama' in dict {d}:   {'nama' in d}")  # cek KEY, bukan value
print(f"3 in set {s}:              {3 in {1, 3}}")
print()


# ============================================================
# 6. PERFORMA - KAPAN PAKAI YANG MANA?
# ============================================================
print("=" * 60)
print("6. PERFORMA & KAPAN PAKAI?")
print("=" * 60)

import time

# Benchmark: cek keanggotaan
n = 1_000_000
test_list = list(range(n))
test_set = set(range(n))
target = n - 1  # elemen terakhir (worst case untuk list)

# List search
start = time.perf_counter()
_ = target in test_list
list_time = time.perf_counter() - start

# Set search
start = time.perf_counter()
_ = target in test_set
set_time = time.perf_counter() - start

print(f"Cek keanggotaan {n:,} elemen:")
print(f"  List: {list_time:.6f} detik")
print(f"  Set:  {set_time:.6f} detik")
print(f"  Set {list_time / set_time:.0f}x lebih cepat untuk pencarian!")

import sys
print(f"\nUkuran memori 1000 elemen:")
l = list(range(1000))
t = tuple(range(1000))
s = set(range(1000))
print(f"  List:  {sys.getsizeof(l):>6} bytes")
print(f"  Tuple: {sys.getsizeof(t):>6} bytes  (lebih hemat dari list)")
print(f"  Set:   {sys.getsizeof(s):>6} bytes  (lebih boros, tapi cari cepat)")
print()


# ============================================================
# 7. USE CASE: KAPAN PAKAI YANG MANA?
# ============================================================
print("=" * 60)
print("7. USE CASES - KAPAN PAKAI YANG MANA?")
print("=" * 60)

# ─────────────────────────────────────────────
# LIST -> Data yang bisa berubah, perlu urutan
# ─────────────────────────────────────────────
print("\n--- LIST: Daftar Todo ---")
# Pakai list karena: todo bisa ditambah, dihapus, diubah, urutan penting
todo = []
todo.append("Belajar Python")
todo.append("Buat project")
todo.append("Review code")
todo.insert(1, "Baca dokumentasi")

for i, task in enumerate(todo, 1):
    print(f"  {i}. {task}")

todo.remove("Baca dokumentasi")   # selesai, hapus
print(f"  Setelah selesai 1 task: {todo}")


# ─────────────────────────────────────────────
# TUPLE -> Data tetap, tidak boleh berubah
# ─────────────────────────────────────────────
print("\n--- TUPLE: Koordinat & Konstanta ---")
# Pakai tuple karena: koordinat tidak boleh berubah
lokasi_kantor = (-6.2088, 106.8456)    # latitude, longitude Jakarta
warna_rgb = (255, 128, 0)              # orange
hari_kerja = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat")
http_status = (200, "OK")

print(f"  Lokasi kantor: {lokasi_kantor}")
print(f"  Warna orange RGB: {warna_rgb}")
print(f"  Hari kerja: {hari_kerja}")
print(f"  HTTP Status: {http_status}")

# Tuple bisa jadi key dictionary (list tidak bisa!)
jarak = {
    ("Jakarta", "Bandung"): 150,
    ("Jakarta", "Surabaya"): 780,
    ("Bandung", "Yogya"): 420,
}
print(f"  Jarak Jakarta-Bandung: {jarak[('Jakarta', 'Bandung')]} km")


# ─────────────────────────────────────────────
# DICTIONARY -> Data dengan label (key-value)
# ─────────────────────────────────────────────
print("\n--- DICTIONARY: Profil & Database Record ---")
# Pakai dict karena: setiap data punya label/nama
mahasiswa = {
    "nim": "2024001",
    "nama": "Budi Santoso",
    "jurusan": "Teknik Informatika",
    "semester": 3,
    "ipk": 3.75,
    "aktif": True,
}

print(f"  Profil Mahasiswa:")
for key, val in mahasiswa.items():
    print(f"    {key:<10}: {val}")

# Dict untuk config
config = {
    "debug": False,
    "port": 8080,
    "host": "localhost",
    "db_name": "myapp",
}
print(f"\n  Config: {config}")

# Dict untuk counting
teks = "abracadabra"
counter = {}
for char in teks:
    counter[char] = counter.get(char, 0) + 1
print(f"\n  Counting '{teks}': {counter}")


# ─────────────────────────────────────────────
# SET -> Data unik, operasi himpunan
# ─────────────────────────────────────────────
print("\n--- SET: Data Unik & Operasi Himpunan ---")
# Pakai set karena: butuh data unik, operasi union/intersection

# Hapus duplikat
pesanan = ["kopi", "teh", "kopi", "jus", "teh", "kopi"]
unik = set(pesanan)
print(f"  Pesanan: {pesanan}")
print(f"  Unik:    {unik}")

# Operasi himpunan
python_devs = {"Alice", "Bob", "Charlie", "Diana"}
java_devs = {"Bob", "Diana", "Eve", "Frank"}

print(f"\n  Python devs: {python_devs}")
print(f"  Java devs:   {java_devs}")
print(f"  Bisa keduanya (intersection): {python_devs & java_devs}")
print(f"  Semua developer (union):      {python_devs | java_devs}")
print(f"  Hanya Python (difference):    {python_devs - java_devs}")
print(f"  Hanya salah satu (xor):       {python_devs ^ java_devs}")

# Cek tag/permission
user_roles = {"admin", "editor"}
required = {"admin"}
print(f"\n  User roles: {user_roles}")
print(f"  Required:   {required}")
print(f"  Punya akses: {required.issubset(user_roles)}")


# ============================================================
# 8. KONVERSI ANTAR TIPE
# ============================================================
print("\n" + "=" * 60)
print("8. KONVERSI ANTAR TIPE")
print("=" * 60)

data_list = [1, 2, 3, 2, 1]
print(f"Awal (list):    {data_list}")

# List -> Tuple
data_tuple = tuple(data_list)
print(f"-> Tuple:       {data_tuple}")

# List -> Set (duplikat hilang)
data_set = set(data_list)
print(f"-> Set:         {data_set}")

# Set -> List (bisa diurutkan)
kembali_list = sorted(list(data_set))
print(f"-> List sorted: {kembali_list}")

# Dict keys/values -> List
info = {"a": 1, "b": 2, "c": 3}
print(f"\nDict:   {info}")
print(f"Keys:   {list(info.keys())}")
print(f"Values: {list(info.values())}")
print(f"Items:  {list(info.items())}")

# List of tuples -> Dict
pairs = [("nama", "Andi"), ("umur", 25), ("kota", "Jakarta")]
dari_pairs = dict(pairs)
print(f"\nList of tuples: {pairs}")
print(f"-> Dict:        {dari_pairs}")


# ============================================================
# 9. RANGKUMAN SINGKAT
# ============================================================
print("\n" + "=" * 60)
print("9. RANGKUMAN - CHEAT SHEET")
print("=" * 60)

print("""
┌──────────────┬────────────────────────────────────────────┐
│  LIST [ ]    │  Data umum yang bisa berubah               │
│              │  -> todo list, daftar belanja, antrian      │
│              │  -> perlu urutan & index                    │
│              │  -> boleh duplikat                          │
├──────────────┼────────────────────────────────────────────┤
│  TUPLE ( )   │  Data tetap yang TIDAK boleh berubah       │
│              │  -> koordinat, RGB, config konstanta        │
│              │  -> lebih hemat memori dari list            │
│              │  -> bisa jadi key dictionary                │
├──────────────┼────────────────────────────────────────────┤
│  DICT {k:v}  │  Data dengan LABEL (key-value pair)        │
│              │  -> profil user, database record, config    │
│              │  -> akses cepat via key                     │
│              │  -> key harus unik & immutable              │
├──────────────┼────────────────────────────────────────────┤
│  SET { }     │  Data UNIK tanpa duplikat                  │
│              │  -> hapus duplikat, cek keanggotaan cepat   │
│              │  -> operasi himpunan (union, intersection)  │
│              │  -> tidak ada urutan & index                │
└──────────────┴────────────────────────────────────────────┘

Aturan sederhana:
  - Butuh ubah data + urutan?        -> LIST
  - Data tidak boleh berubah?        -> TUPLE
  - Butuh pasangan label-nilai?      -> DICTIONARY
  - Butuh data unik / operasi set?   -> SET
""")
