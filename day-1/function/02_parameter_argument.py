"""
=== PARAMETER & ARGUMENT (Detail) ===

Istilah:
    - PARAMETER: variabel di definisi function  -> def sapa(nama):
    - ARGUMENT:  nilai yang dikirim saat panggil -> sapa("Budi")

Jenis parameter:
    1. Positional parameter
    2. Default parameter
    3. *args     (variabel jumlah argument)
    4. **kwargs  (variabel jumlah keyword argument)
    5. Keyword-only parameter
    6. Positional-only parameter
"""


# ============================================================
# 1. POSITIONAL ARGUMENT
# ============================================================
print("=" * 60)
print("1. POSITIONAL ARGUMENT")
print("=" * 60)


def perkenalan(nama, umur, kota):
    """Urutan argument harus sesuai urutan parameter."""
    print(f"  Nama: {nama}, Umur: {umur}, Kota: {kota}")


# Positional: urutan harus tepat
perkenalan("Budi", 25, "Jakarta")
perkenalan("Rina", 22, "Bandung")

# Keyword argument: bisa acak urutan
perkenalan(kota="Surabaya", nama="Andi", umur=30)

# Campuran: positional dulu, baru keyword
perkenalan("Diana", umur=28, kota="Yogya")
print()


# ============================================================
# 2. DEFAULT PARAMETER
# ============================================================
print("=" * 60)
print("2. DEFAULT PARAMETER")
print("=" * 60)


def buat_akun(username, role="user", aktif=True):
    """Parameter dengan default tidak wajib diisi."""
    status = "Aktif" if aktif else "Nonaktif"
    print(f"  User: {username}, Role: {role}, Status: {status}")


buat_akun("admin", "superadmin")      # override role
buat_akun("budi")                      # pakai semua default
buat_akun("charlie", aktif=False)      # override aktif saja
buat_akun("diana", role="editor")      # override role saja
print()

# PENTING: Default parameter dievaluasi sekali saat definisi!
# Jangan pakai mutable object (list, dict) sebagai default
def tambah_item_SALAH(item, daftar=[]):
    """JANGAN seperti ini! list default di-share antar panggilan."""
    daftar.append(item)
    return daftar


def tambah_item_BENAR(item, daftar=None):
    """Cara yang benar: gunakan None lalu buat list baru."""
    if daftar is None:
        daftar = []
    daftar.append(item)
    return daftar


print("Default mutable (SALAH):")
print(f"  {tambah_item_SALAH('a')}")  # ['a']
print(f"  {tambah_item_SALAH('b')}")  # ['a', 'b'] -- BUG!

print("Default None (BENAR):")
print(f"  {tambah_item_BENAR('a')}")  # ['a']
print(f"  {tambah_item_BENAR('b')}")  # ['b'] -- benar!
print()


# ============================================================
# 3. *args (Variable Positional Arguments)
# ============================================================
print("=" * 60)
print("3. *args (Jumlah argument tidak terbatas)")
print("=" * 60)


def jumlahkan(*angka):
    """Menerima berapa pun argument, dikemas jadi tuple."""
    print(f"  args = {angka} (type: {type(angka).__name__})")
    return sum(angka)


print(f"  jumlahkan(1, 2) = {jumlahkan(1, 2)}")
print(f"  jumlahkan(1, 2, 3, 4, 5) = {jumlahkan(1, 2, 3, 4, 5)}")
print(f"  jumlahkan(10) = {jumlahkan(10)}")
print()


def cetak_menu(judul, *items):
    """Parameter biasa + *args."""
    print(f"  === {judul} ===")
    for i, item in enumerate(items, 1):
        print(f"    {i}. {item}")


cetak_menu("MAKANAN", "Nasi Goreng", "Mie Ayam", "Bakso", "Soto")
cetak_menu("MINUMAN", "Es Teh", "Kopi")
print()

# Unpack list/tuple ke *args
angka_list = [10, 20, 30, 40]
print(f"  Unpack list: jumlahkan(*{angka_list}) = {jumlahkan(*angka_list)}")
print()


# ============================================================
# 4. **kwargs (Variable Keyword Arguments)
# ============================================================
print("=" * 60)
print("4. **kwargs (Keyword argument tidak terbatas)")
print("=" * 60)


def cetak_profil(**data):
    """Menerima keyword argument berapa pun, dikemas jadi dict."""
    print(f"  kwargs = {data} (type: {type(data).__name__})")
    for key, value in data.items():
        print(f"    {key}: {value}")


cetak_profil(nama="Budi", umur=25, kota="Jakarta")
print()
cetak_profil(nama="Rina", jurusan="TI", ipk=3.8, semester=5)
print()


def buat_html_tag(tag, teks, **atribut):
    """Parameter biasa + **kwargs."""
    attrs = " ".join(f'{k}="{v}"' for k, v in atribut.items())
    if attrs:
        return f"<{tag} {attrs}>{teks}</{tag}>"
    return f"<{tag}>{teks}</{tag}>"


print(buat_html_tag("p", "Hello World"))
print(buat_html_tag("a", "Klik sini", href="https://python.org", target="_blank"))
print(buat_html_tag("div", "Konten", id="main", style="color:red"))
print()

# Unpack dict ke **kwargs
config = {"host": "localhost", "port": 8080, "debug": True}
cetak_profil(**config)
print()


# ============================================================
# 5. KOMBINASI SEMUA JENIS PARAMETER
# ============================================================
print("=" * 60)
print("5. KOMBINASI SEMUA JENIS PARAMETER")
print("=" * 60)


def super_function(wajib, default="nilai_default", *args, **kwargs):
    """
    Urutan parameter:
    1. Positional (wajib)
    2. Default
    3. *args
    4. **kwargs
    """
    print(f"  wajib   = {wajib}")
    print(f"  default = {default}")
    print(f"  args    = {args}")
    print(f"  kwargs  = {kwargs}")
    print()


super_function("A")
super_function("A", "B")
super_function("A", "B", "C", "D", "E")
super_function("A", "B", "C", x=1, y=2)
print()


# ============================================================
# 6. KEYWORD-ONLY PARAMETER (setelah *)
# ============================================================
print("=" * 60)
print("6. KEYWORD-ONLY PARAMETER")
print("=" * 60)


def format_harga(harga, *, mata_uang="Rp", ribuan=True):
    """
    Parameter setelah * HARUS dipanggil sebagai keyword argument.
    Berguna untuk memaksa pemanggil eksplisit.
    """
    if ribuan:
        return f"{mata_uang}{harga:,.0f}"
    return f"{mata_uang}{harga}"


print(format_harga(50000))
print(format_harga(50000, mata_uang="$"))
print(format_harga(50000, mata_uang="€", ribuan=False))

# format_harga(50000, "$")  # ERROR! mata_uang harus keyword
print()


# ============================================================
# 7. TYPE HINTS (Petunjuk Tipe Data)
# ============================================================
print("=" * 60)
print("7. TYPE HINTS")
print("=" * 60)


def hitung_diskon(harga: float, persen: float = 10.0) -> float:
    """Type hints tidak memaksa tipe, tapi membantu dokumentasi & IDE."""
    return harga * (1 - persen / 100)


def gabung_nama(depan: str, belakang: str) -> str:
    return f"{depan} {belakang}"


def cari_index(data: list[int], target: int) -> int | None:
    """Return int jika ditemukan, None jika tidak."""
    try:
        return data.index(target)
    except ValueError:
        return None


print(f"hitung_diskon(100000, 15) = {hitung_diskon(100000, 15):,.0f}")
print(f"gabung_nama('Budi', 'Santoso') = '{gabung_nama('Budi', 'Santoso')}'")
print(f"cari_index([10,20,30], 20) = {cari_index([10, 20, 30], 20)}")
print(f"cari_index([10,20,30], 99) = {cari_index([10, 20, 30], 99)}")

print()
print("=" * 60)
print("Selesai! Parameter & argument sudah dicontohkan.")
