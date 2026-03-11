"""
=== BUILT-IN METHODS - STRING OPERATIONS ===

String di Python memiliki banyak method bawaan yang dikelompokkan menjadi:
1. General Operations    - split, isalpha, isdigit, *
2. Capitalization        - upper, lower, title, capitalize
3. Concatenation         - join, +
4. Searching             - find, index, rfind, rindex, startswith, endswith, replace, strip, rstrip
"""

nama = " denny chandra "

print("=== STRING METHOD ===")
print(f"nama = '{nama}'")
print()


# ============================================================
# 1. GENERAL OPERATIONS
# ============================================================
print("=== GENERAL OPERATIONS ===")

# split() - memecah string menjadi list berdasarkan separator
kalimat = "Belajar Python itu menyenangkan"
print(f"'{kalimat}'.split()       = {kalimat.split()}")
print(f"'a-b-c-d'.split('-')     = {'a-b-c-d'.split('-')}")
print(f"'satu,dua,tiga'.split(',') = {'satu,dua,tiga'.split(',')}")

# isalpha() - True jika semua karakter adalah huruf
print(f"'hello'.isalpha()   = {'hello'.isalpha()}")       # True
print(f"'hello1'.isalpha()  = {'hello1'.isalpha()}")      # False
print(f"'hello world'.isalpha() = {'hello world'.isalpha()}")  # False (ada spasi)

# isdigit() - True jika semua karakter adalah angka
print(f"'12345'.isdigit()   = {'12345'.isdigit()}")       # True
print(f"'123a5'.isdigit()   = {'123a5'.isdigit()}")       # False
print(f"'3.14'.isdigit()    = {'3.14'.isdigit()}")        # False (ada titik)

# * (repetisi) - mengulang string
print(f"'ha' * 3   = {'ha' * 3}")
print(f"'-' * 20   = {'-' * 20}")
print()


# ============================================================
# 2. CAPITALIZATION OPERATIONS
# ============================================================
print("=== CAPITALIZATION OPERATIONS ===")

teks = "belajar python programming"

# upper() - semua huruf besar
print(f"'{teks}'.upper()      = '{teks.upper()}'")

# lower() - semua huruf kecil
teks_besar = "HELLO WORLD"
print(f"'{teks_besar}'.lower() = '{teks_besar.lower()}'")

# title() - huruf pertama setiap kata jadi besar
print(f"'{teks}'.title()      = '{teks.title()}'")

# capitalize() - huruf pertama string saja yang besar
print(f"'{teks}'.capitalize() = '{teks.capitalize()}'")

# Contoh dengan variabel nama
print(f"nama.strip().title()  = '{nama.strip().title()}'")
print()


# ============================================================
# 3. CONCATENATION OPERATIONS
# ============================================================
print("=== CONCATENATION OPERATIONS ===")

# join() - menggabungkan list menjadi string
kata_list = ["Belajar", "Python", "itu", "seru"]
hasil_join = " ".join(kata_list)
print(f"' '.join({kata_list}) = '{hasil_join}'")

print(f"'-'.join(['a','b','c'])  = {'-'.join(['a', 'b', 'c'])}")
print(f"', '.join(['x','y','z']) = {', '.join(['x', 'y', 'z'])}")

# + (concatenation) - menggabungkan dua string
depan = "Hello"
belakang = "World"
gabung = depan + " " + belakang
print(f"'{depan}' + ' ' + '{belakang}' = '{gabung}'")
print()


# ============================================================
# 4. SEARCHING OPERATIONS
# ============================================================
print("=== SEARCHING OPERATIONS ===")

teks = "Python Programming is awesome, Python is fun"
print(f"teks = '{teks}'")
print()

# find() - cari posisi substring, return -1 jika tidak ditemukan
print(f"teks.find('Python')      = {teks.find('Python')}")        # 0
print(f"teks.find('is')          = {teks.find('is')}")            # posisi pertama
print(f"teks.find('Java')        = {teks.find('Java')}")          # -1

# index() - seperti find(), tapi raise ValueError jika tidak ditemukan
print(f"teks.index('Python')     = {teks.index('Python')}")       # 0
try:
    teks.index('Java')
except ValueError as e:
    print(f"teks.index('Java')       -> ValueError: {e}")

# rfind() - cari dari kanan
print(f"teks.rfind('Python')     = {teks.rfind('Python')}")       # posisi Python terakhir

# rindex() - seperti rfind(), tapi raise ValueError
print(f"teks.rindex('Python')    = {teks.rindex('Python')}")

# startswith() - cek apakah string dimulai dengan substring
print(f"teks.startswith('Python')  = {teks.startswith('Python')}")   # True
print(f"teks.startswith('Java')    = {teks.startswith('Java')}")     # False

# endswith() - cek apakah string diakhiri dengan substring
print(f"teks.endswith('fun')     = {teks.endswith('fun')}")        # True
print(f"teks.endswith('boring')  = {teks.endswith('boring')}")     # False

# replace() - mengganti substring
baru = teks.replace("Python", "Java")
print(f"teks.replace('Python', 'Java') = '{baru}'")

# strip() - hapus whitespace di awal dan akhir
spasi = "   Hello World   "
print(f"'{spasi}'.strip()  = '{spasi.strip()}'")
print(f"'{spasi}'.lstrip() = '{spasi.lstrip()}'")

# rstrip() - hapus whitespace di akhir saja
print(f"'{spasi}'.rstrip() = '{spasi.rstrip()}'")
print()


# ============================================================
# CONTOH PENGGUNAAN DENGAN VARIABEL nama
# ============================================================
print("=== CONTOH DENGAN VARIABEL nama ===")
print(f"nama asli          = '{nama}'")
print(f"nama.strip()       = '{nama.strip()}'")
print(f"nama.strip().upper() = '{nama.strip().upper()}'")
print(f"nama.strip().title() = '{nama.strip().title()}'")
print(f"nama.strip().split() = {nama.strip().split()}")
print(f"nama.find('chandra') = {nama.find('chandra')}")
print(f"nama.replace('denny', 'john') = '{nama.replace('denny', 'john')}'")

print()
print("=" * 50)
print("Selesai! String built-in methods sudah dicontohkan.")
