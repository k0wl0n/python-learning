"""
=== CARA MEMBUAT FUNCTION ===

Syntax:
    def nama_function(parameter):
        '''docstring (opsional)'''
        # kode
        return hasil

Aturan penamaan:
    - Gunakan huruf kecil + underscore (snake_case)
    - Nama harus deskriptif: hitung_luas(), cek_genap(), format_rupiah()
    - Hindari nama 1 huruf kecuali untuk loop: def f() ❌ -> def format_nama() ✅
"""


# ============================================================
# 1. FUNCTION PALING SEDERHANA (tanpa parameter, tanpa return)
# ============================================================
print("=" * 60)
print("1. FUNCTION SEDERHANA")
print("=" * 60)


def salam():
    """Menampilkan sapaan sederhana."""
    print("Halo! Selamat belajar Python!")


def garis():
    """Menampilkan garis pemisah."""
    print("-" * 40)


def info_app():
    """Menampilkan informasi aplikasi."""
    print("Aplikasi Belajar Python v1.0")
    print("Dibuat oleh: Tim TPCC")
    print("Tahun: 2026")


# Cara memanggil (akses) function: tulis nama lalu ()
salam()
garis()
info_app()
garis()
print()


# ============================================================
# 2. FUNCTION DENGAN PARAMETER
# ============================================================
print("=" * 60)
print("2. FUNCTION DENGAN PARAMETER")
print("=" * 60)


def sapa(nama):
    """Menyapa seseorang berdasarkan nama."""
    print(f"Halo, {nama}! Apa kabar?")


def sapa_lengkap(nama, waktu):
    """Menyapa dengan waktu."""
    print(f"Selamat {waktu}, {nama}!")


# Memanggil dengan argument
sapa("Budi")
sapa("Rina")
sapa_lengkap("Budi", "Pagi")
sapa_lengkap("Rina", "Malam")
print()


# ============================================================
# 3. FUNCTION DENGAN RETURN
# ============================================================
print("=" * 60)
print("3. FUNCTION DENGAN RETURN")
print("=" * 60)


def tambah(a, b):
    """Menjumlahkan dua angka."""
    return a + b


def luas_persegi(sisi):
    """Menghitung luas persegi."""
    return sisi * sisi


def luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran."""
    return 3.14159 * jari_jari ** 2


# Return value bisa disimpan ke variabel
hasil = tambah(5, 3)
print(f"tambah(5, 3) = {hasil}")

luas = luas_persegi(4)
print(f"luas_persegi(4) = {luas}")

luas_l = luas_lingkaran(7)
print(f"luas_lingkaran(7) = {luas_l:.2f}")

# Return value bisa langsung dipakai
print(f"tambah(10, 20) + tambah(30, 40) = {tambah(10, 20) + tambah(30, 40)}")
print()


# ============================================================
# 4. FUNCTION DENGAN DEFAULT PARAMETER
# ============================================================
print("=" * 60)
print("4. FUNCTION DENGAN DEFAULT PARAMETER")
print("=" * 60)


def sapa_default(nama, waktu="Pagi"):
    """Menyapa, default waktu = Pagi jika tidak diisi."""
    print(f"Selamat {waktu}, {nama}!")


def buat_kopi(jenis="hitam", gula=1, susu=False):
    """Membuat kopi dengan resep tertentu."""
    resep = f"Kopi {jenis}, gula {gula} sendok"
    if susu:
        resep += ", pakai susu"
    return resep


sapa_default("Budi")                  # pakai default waktu
sapa_default("Budi", "Sore")         # override default
print()

print(buat_kopi())                     # semua default
print(buat_kopi("latte", 2, True))    # override semua
print(buat_kopi(gula=0))              # hanya override gula (keyword argument)
print(buat_kopi(susu=True))           # hanya override susu
print()


# ============================================================
# 5. FUNCTION DENGAN DOCSTRING
# ============================================================
print("=" * 60)
print("5. FUNCTION DENGAN DOCSTRING")
print("=" * 60)


def hitung_bmi(berat, tinggi):
    """
    Menghitung Body Mass Index (BMI).

    Parameter:
        berat (float): Berat badan dalam kg
        tinggi (float): Tinggi badan dalam meter

    Return:
        float: Nilai BMI

    Contoh:
        >>> hitung_bmi(70, 1.75)
        22.86
    """
    return berat / (tinggi ** 2)


bmi = hitung_bmi(70, 1.75)
print(f"BMI = {bmi:.2f}")

# Cara melihat docstring
print(f"\nDocstring dari hitung_bmi:")
print(hitung_bmi.__doc__)
print()


# ============================================================
# 6. SCOPE VARIABEL (Local vs Global)
# ============================================================
print("=" * 60)
print("6. SCOPE VARIABEL")
print("=" * 60)

pesan_global = "Saya variabel GLOBAL"


def contoh_scope():
    pesan_local = "Saya variabel LOCAL"
    print(f"  Di dalam function: {pesan_local}")
    print(f"  Di dalam function: {pesan_global}")  # bisa akses global


contoh_scope()
print(f"  Di luar function: {pesan_global}")
# print(pesan_local)  # ERROR! variabel lokal tidak bisa diakses di luar

# Mengubah variabel global dari dalam function
counter = 0


def tambah_counter():
    global counter  # deklarasi global
    counter += 1


print(f"\n  counter sebelum: {counter}")
tambah_counter()
tambah_counter()
tambah_counter()
print(f"  counter sesudah 3x dipanggil: {counter}")
print()


# ============================================================
# 7. FUNCTION SEBAGAI OBJEK
# ============================================================
print("=" * 60)
print("7. FUNCTION SEBAGAI OBJEK")
print("=" * 60)


def kuadrat(x):
    return x ** 2


def kubik(x):
    return x ** 3


# Function bisa disimpan ke variabel
operasi = kuadrat
print(f"operasi(5) = {operasi(5)}")  # memanggil kuadrat via variabel

operasi = kubik
print(f"operasi(5) = {operasi(5)}")  # sekarang memanggil kubik

# Function bisa disimpan di list
fungsi_list = [kuadrat, kubik, abs]
for fn in fungsi_list:
    print(f"  {fn.__name__}(-3) = {fn(-3)}")

# Function bisa jadi argument function lain
def terapkan(func, nilai):
    """Menerapkan function ke suatu nilai."""
    return func(nilai)


print(f"\nterapkan(kuadrat, 4) = {terapkan(kuadrat, 4)}")
print(f"terapkan(kubik, 3)   = {terapkan(kubik, 3)}")
print(f"terapkan(abs, -10)   = {terapkan(abs, -10)}")

print()
print("=" * 60)
print("Selesai! Cara membuat function sudah dicontohkan.")
