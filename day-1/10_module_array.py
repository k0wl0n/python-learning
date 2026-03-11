"""
=== CONTOH MENGGUNAKAN MODULE: ARRAY ===

- Modul array mendefinisikan tipe objek yang secara ringkas dapat mewakili
  array nilai dasar: characters, integers, angka floating point.
- Array sangat mirip dengan lists, kecuali bahwa jenis objek yang disimpan
  di dalamnya dibatasi.
- Tipe ditentukan pada waktu pembuatan objek dengan menggunakan kode tipe.

Tipe Pada Array:
Type code | C Type              | Python Type        | Min size (bytes)
----------|---------------------|--------------------|------------------
'b'       | signed char         | int                | 1
'B'       | unsigned char       | int                | 1
'u'       | wchar_t             | Unicode character  | 2
'h'       | signed short        | int                | 2
'H'       | unsigned short      | int                | 2
'i'       | signed int          | int                | 2
'I'       | unsigned int        | int                | 2
'l'       | signed long         | int                | 4
'L'       | unsigned long       | int                | 4
'q'       | signed long long    | int                | 8
'Q'       | unsigned long long  | int                | 8
'f'       | float               | float              | 4
'd'       | double              | float              | 8
"""

from array import array

# ============================================================
# 1. MEMBUAT ARRAY
# ============================================================
print("=== MEMBUAT ARRAY ===")

# Array integer (type code 'i')
myarray = array('i', [5, 6, 7, 2, 3, 5])
print(f"myarray = array('i', [5,6,7,2,3,5])")
print(f"myarray = {myarray}")
print(f"Type: {type(myarray)}")
print()

# Array dengan tipe berbeda
arr_signed_char = array('b', [1, 2, -3, 4])       # signed char
arr_float = array('f', [1.5, 2.3, 3.7])            # float
arr_double = array('d', [1.1, 2.2, 3.3])           # double

print(f"array('b', [1,2,-3,4])   = {arr_signed_char}")
print(f"array('f', [1.5,2.3,3.7]) = {arr_float}")
print(f"array('d', [1.1,2.2,3.3]) = {arr_double}")
print()


# ============================================================
# 2. MENGAKSES ELEMEN
# ============================================================
print("=== MENGAKSES ELEMEN ===")

print(f"myarray = {myarray}")
print(f"myarray[0]  = {myarray[0]}")    # elemen pertama
print(f"myarray[2]  = {myarray[2]}")    # elemen ketiga
print(f"myarray[-1] = {myarray[-1]}")   # elemen terakhir
print(f"myarray[1:4] = {myarray[1:4]}") # slicing
print()


# ============================================================
# 3. MENAMBAH ELEMEN
# ============================================================
print("=== MENAMBAH ELEMEN ===")

print(f"Sebelum: {myarray}")

# append() - tambah 1 elemen di akhir
myarray.append(10)
print(f"Setelah append(10):    {myarray}")

# extend() - tambah beberapa elemen
myarray.extend([20, 30])
print(f"Setelah extend([20,30]): {myarray}")

# insert() - tambah elemen di posisi tertentu
myarray.insert(0, 99)
print(f"Setelah insert(0, 99): {myarray}")
print()


# ============================================================
# 4. MENGHAPUS ELEMEN
# ============================================================
print("=== MENGHAPUS ELEMEN ===")

print(f"Sebelum: {myarray}")

# remove() - hapus elemen pertama yang ditemukan dengan nilai tertentu
myarray.remove(99)
print(f"Setelah remove(99):  {myarray}")

# pop() - hapus elemen di index tertentu (default: terakhir)
elemen = myarray.pop()
print(f"Setelah pop():       {myarray} (dihapus: {elemen})")

elemen = myarray.pop(0)
print(f"Setelah pop(0):      {myarray} (dihapus: {elemen})")
print()


# ============================================================
# 5. OPERASI LAINNYA
# ============================================================
print("=== OPERASI LAINNYA ===")

arr = array('i', [5, 3, 8, 1, 9, 2])
print(f"arr = {arr}")

# count() - hitung jumlah kemunculan
arr2 = array('i', [1, 2, 3, 2, 2, 4])
print(f"array('i', [1,2,3,2,2,4]).count(2) = {arr2.count(2)}")

# index() - cari posisi elemen
print(f"arr.index(8) = {arr.index(8)}")

# reverse() - balik urutan
arr.reverse()
print(f"Setelah reverse(): {arr}")

# tolist() - konversi ke list
daftar = arr.tolist()
print(f"arr.tolist() = {daftar}, type: {type(daftar)}")

# buffer_info() - info alamat memori dan jumlah elemen
print(f"arr.buffer_info() = {arr.buffer_info()}")

# typecode - kode tipe array
print(f"arr.typecode = '{arr.typecode}'")

# itemsize - ukuran satu elemen dalam bytes
print(f"arr.itemsize = {arr.itemsize} bytes")
print()


# ============================================================
# 6. PERBEDAAN ARRAY vs LIST
# ============================================================
print("=== PERBEDAAN ARRAY vs LIST ===")

# List bisa menyimpan tipe data campuran
my_list = [1, "dua", 3.0, True]
print(f"List (campuran): {my_list}")

# Array hanya bisa menyimpan satu tipe data
my_arr = array('i', [1, 2, 3, 4])
print(f"Array (int saja): {my_arr}")

try:
    my_arr.append(3.5)  # akan error karena bukan integer
except TypeError as e:
    print(f"array('i').append(3.5) -> TypeError: {e}")

print()

# Perbandingan ukuran memori
import sys
list_angka = list(range(1000))
arr_angka = array('i', range(1000))
print(f"Ukuran list 1000 elemen:  {sys.getsizeof(list_angka)} bytes")
print(f"Ukuran array 1000 elemen: {sys.getsizeof(arr_angka)} bytes")
print("Array lebih hemat memori dibandingkan list!")

print()
print("=" * 50)
print("Selesai! Module array sudah dicontohkan.")
