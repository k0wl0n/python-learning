"""
=== BUILT-IN FUNCTIONS PYTHON ===

Python menyediakan banyak fungsi bawaan yang bisa langsung digunakan
tanpa perlu import module apapun.

Berikut contoh penggunaan built-in functions yang paling sering dipakai.
"""

# ============================================================
# KONVERSI TIPE DATA
# ============================================================
print("=== KONVERSI TIPE DATA ===")

# int() - konversi ke integer
print(f"int('10')     = {int('10')}")
print(f"int(3.9)      = {int(3.9)}")

# float() - konversi ke float
print(f"float('3.14') = {float('3.14')}")
print(f"float(10)     = {float(10)}")

# str() - konversi ke string
print(f"str(100)      = '{str(100)}'")
print(f"str(3.14)     = '{str(3.14)}'")

# bool() - konversi ke boolean
print(f"bool(1)       = {bool(1)}")
print(f"bool(0)       = {bool(0)}")
print(f"bool('')      = {bool('')}")
print(f"bool('hello') = {bool('hello')}")

# list(), tuple(), set(), dict()
print(f"list('abc')       = {list('abc')}")
print(f"tuple([1, 2, 3])  = {tuple([1, 2, 3])}")
print(f"set([1, 2, 2, 3]) = {set([1, 2, 2, 3])}")
print(f"dict(a=1, b=2)    = {dict(a=1, b=2)}")

# complex() - bilangan kompleks
print(f"complex(3, 4)     = {complex(3, 4)}")

# frozenset() - set yang tidak bisa diubah
print(f"frozenset([1,2,3]) = {frozenset([1, 2, 3])}")
print()


# ============================================================
# MATEMATIKA
# ============================================================
print("=== MATEMATIKA ===")

# abs() - nilai absolut
print(f"abs(-10)     = {abs(-10)}")
print(f"abs(5)       = {abs(5)}")

# round() - pembulatan
print(f"round(3.7)   = {round(3.7)}")
print(f"round(3.14159, 2) = {round(3.14159, 2)}")

# pow() - pangkat
print(f"pow(2, 3)    = {pow(2, 3)}")
print(f"pow(2, 3, 5) = {pow(2, 3, 5)}")  # (2^3) % 5

# divmod() - hasil bagi dan sisa
print(f"divmod(17, 5) = {divmod(17, 5)}")  # (3, 2)

# min(), max(), sum()
angka = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"angka = {angka}")
print(f"min(angka)   = {min(angka)}")
print(f"max(angka)   = {max(angka)}")
print(f"sum(angka)   = {sum(angka)}")
print()


# ============================================================
# INPUT / OUTPUT
# ============================================================
print("=== INPUT / OUTPUT ===")

# print() - menampilkan output
print("Hello, World!")
print("A", "B", "C", sep="-")       # separator
print("Tanpa newline", end=" | ")
print("Lanjutan")

# input() - menerima input dari user (dikomentari agar bisa jalan otomatis)
# nama = input("Masukkan nama: ")
# print(f"Halo, {nama}!")
print("input('Masukkan nama: ') -> menerima input dari keyboard")
print()


# ============================================================
# TIPE & INFORMASI OBJEK
# ============================================================
print("=== TIPE & INFORMASI OBJEK ===")

# type() - cek tipe data
print(f"type(10)       = {type(10)}")
print(f"type('hello')  = {type('hello')}")
print(f"type([1,2])    = {type([1, 2])}")

# isinstance() - cek apakah objek merupakan instance dari tipe tertentu
print(f"isinstance(10, int)    = {isinstance(10, int)}")
print(f"isinstance('hi', str)  = {isinstance('hi', str)}")
print(f"isinstance(10, str)    = {isinstance(10, str)}")

# issubclass()
print(f"issubclass(bool, int)  = {issubclass(bool, int)}")

# id() - identitas objek (alamat memori)
x = 42
print(f"id(42) = {id(x)}")

# callable() - cek apakah objek bisa dipanggil
print(f"callable(print)  = {callable(print)}")
print(f"callable(42)     = {callable(42)}")

# len() - panjang objek
print(f"len('python')   = {len('python')}")
print(f"len([1,2,3,4])  = {len([1, 2, 3, 4])}")
print()


# ============================================================
# ITERASI & SEQUENCE
# ============================================================
print("=== ITERASI & SEQUENCE ===")

# range() - membuat urutan angka
print(f"list(range(5))       = {list(range(5))}")
print(f"list(range(2, 8))    = {list(range(2, 8))}")
print(f"list(range(0, 10, 2)) = {list(range(0, 10, 2))}")

# enumerate() - iterasi dengan index
buah = ["apel", "jeruk", "mangga"]
print("enumerate(buah):")
for i, b in enumerate(buah):
    print(f"  index {i}: {b}")

# zip() - menggabungkan beberapa iterable
nama = ["Alice", "Bob", "Charlie"]
nilai = [85, 92, 78]
print("zip(nama, nilai):")
for n, v in zip(nama, nilai):
    print(f"  {n}: {v}")

# sorted() - mengurutkan
data = [5, 2, 8, 1, 9]
print(f"sorted({data})              = {sorted(data)}")
print(f"sorted({data}, reverse=True) = {sorted(data, reverse=True)}")

# reversed() - membalik urutan
print(f"list(reversed({data}))       = {list(reversed(data))}")

# map() - terapkan fungsi ke setiap elemen
angka = [1, 2, 3, 4, 5]
kuadrat = list(map(lambda x: x ** 2, angka))
print(f"map(lambda x: x**2, {angka}) = {kuadrat}")

# filter() - filter elemen berdasarkan kondisi
genap = list(filter(lambda x: x % 2 == 0, angka))
print(f"filter(genap, {angka})        = {genap}")

# all() dan any()
semua_benar = [True, True, True]
ada_benar = [False, True, False]
semua_salah = [False, False, False]
print(f"all({semua_benar}) = {all(semua_benar)}")
print(f"any({ada_benar})   = {any(ada_benar)}")
print(f"all({semua_salah}) = {all(semua_salah)}")

# next() dan iter()
my_iter = iter([10, 20, 30])
print(f"next(iter([10,20,30])) = {next(my_iter)}")
print(f"next(...)              = {next(my_iter)}")
print()


# ============================================================
# STRING & REPRESENTASI
# ============================================================
print("=== STRING & REPRESENTASI ===")

# repr() - representasi string dari objek
print(f"repr('hello')  = {repr('hello')}")
print(f"repr(42)       = {repr(42)}")

# ascii() - representasi ASCII
print(f"ascii('Café')  = {ascii('Café')}")

# format() - format nilai
print(f"format(255, 'b')  = {format(255, 'b')}")   # binary
print(f"format(255, 'x')  = {format(255, 'x')}")   # hex
print(f"format(255, 'o')  = {format(255, 'o')}")    # octal

# chr() dan ord() - karakter <-> kode ASCII
print(f"chr(65)  = '{chr(65)}'")
print(f"chr(97)  = '{chr(97)}'")
print(f"ord('A') = {ord('A')}")
print(f"ord('a') = {ord('a')}")
print()


# ============================================================
# BILANGAN (NUMBER SYSTEMS)
# ============================================================
print("=== BILANGAN (NUMBER SYSTEMS) ===")

# bin() - ke binary
print(f"bin(10)  = {bin(10)}")

# oct() - ke octal
print(f"oct(10)  = {oct(10)}")

# hex() - ke hexadecimal
print(f"hex(255) = {hex(255)}")
print()


# ============================================================
# ATRIBUT & OBJEK
# ============================================================
print("=== ATRIBUT & OBJEK ===")

# getattr(), setattr(), hasattr(), delattr()
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

mobil = Mobil("Toyota", "Merah")
print(f"getattr(mobil, 'merk')   = {getattr(mobil, 'merk')}")
print(f"hasattr(mobil, 'warna')  = {hasattr(mobil, 'warna')}")
print(f"hasattr(mobil, 'tahun')  = {hasattr(mobil, 'tahun')}")

setattr(mobil, 'tahun', 2024)
print(f"Setelah setattr 'tahun': {mobil.tahun}")

# dir() - daftar atribut & method objek
print(f"dir([])[:5] = {dir([])[:5]} ...")  # 5 pertama saja

# hash()
print(f"hash('python') = {hash('python')}")
print()


# ============================================================
# LAINNYA
# ============================================================
print("=== LAINNYA ===")

# eval() - evaluasi ekspresi string
hasil = eval("2 + 3 * 4")
print(f"eval('2 + 3 * 4') = {hasil}")

# exec() - eksekusi kode string
exec("x = 10 + 20")

# vars() - dictionary dari atribut objek
print(f"vars(mobil) = {vars(mobil)}")

# help() - menampilkan dokumentasi (dikomentari karena interaktif)
# help(print)
print("help(print) -> menampilkan dokumentasi fungsi print")

# globals() dan locals()
print(f"'angka' in globals() = {'angka' in globals()}")

# open() - membuka file (contoh konsep saja)
print("open('file.txt', 'r') -> membuka file untuk dibaca")

# breakpoint() - untuk debugging (dikomentari)
# breakpoint()
print("breakpoint() -> menghentikan eksekusi untuk debugging")

print()
print("=" * 50)
print("Selesai! Built-in functions sudah dicontohkan.")
