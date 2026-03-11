"""
=== RETURN VALUE (Nilai Kembali) ===

- Function bisa mengembalikan nilai dengan keyword 'return'
- Tanpa return, function mengembalikan None
- Bisa return banyak nilai sekaligus (tuple)
- Return langsung menghentikan eksekusi function
"""


# ============================================================
# 1. RETURN DASAR
# ============================================================
print("=" * 60)
print("1. RETURN DASAR")
print("=" * 60)


# Tanpa return -> None
def tanpa_return():
    x = 10 + 20


# Dengan return
def dengan_return():
    return 10 + 20


hasil1 = tanpa_return()
hasil2 = dengan_return()
print(f"tanpa_return()  = {hasil1}  (type: {type(hasil1).__name__})")
print(f"dengan_return() = {hasil2} (type: {type(hasil2).__name__})")
print()


# ============================================================
# 2. RETURN MENGHENTIKAN FUNCTION
# ============================================================
print("=" * 60)
print("2. RETURN MENGHENTIKAN FUNCTION")
print("=" * 60)


def cek_umur(umur):
    """Return langsung menghentikan function."""
    if umur < 0:
        return "ERROR: Umur tidak boleh negatif"
    if umur < 17:
        return "Anak-anak"
    if umur < 60:
        return "Dewasa"
    return "Lansia"
    print("Baris ini TIDAK AKAN pernah dieksekusi")


for u in [-1, 10, 25, 70]:
    print(f"  umur {u:>3}: {cek_umur(u)}")
print()


# ============================================================
# 3. RETURN MULTIPLE VALUES (Tuple)
# ============================================================
print("=" * 60)
print("3. RETURN MULTIPLE VALUES")
print("=" * 60)


def hitung_statistik(data):
    """Mengembalikan banyak nilai sekaligus sebagai tuple."""
    minimum = min(data)
    maximum = max(data)
    rata2 = sum(data) / len(data)
    total = sum(data)
    jumlah = len(data)
    return minimum, maximum, rata2, total, jumlah


nilai = [85, 92, 78, 95, 88, 72, 90]

# Cara 1: Terima sebagai tuple
result = hitung_statistik(nilai)
print(f"Sebagai tuple: {result}")

# Cara 2: Unpacking (direkomendasikan)
min_val, max_val, avg, total, count = hitung_statistik(nilai)
print(f"Min: {min_val}, Max: {max_val}, Avg: {avg:.1f}, Total: {total}, Count: {count}")
print()


def bagi(a, b):
    """Return hasil bagi dan sisa bagi."""
    if b == 0:
        return None, None
    return a // b, a % b


hasil, sisa = bagi(17, 5)
print(f"17 / 5 = {hasil} sisa {sisa}")

hasil, sisa = bagi(10, 0)
print(f"10 / 0 = {hasil} (pembagian dengan nol)")
print()


# ============================================================
# 4. RETURN DICTIONARY
# ============================================================
print("=" * 60)
print("4. RETURN DICTIONARY")
print("=" * 60)


def analisis_teks(teks):
    """Return dictionary berisi hasil analisis teks."""
    kata_list = teks.split()
    return {
        "teks_asli": teks,
        "jumlah_karakter": len(teks),
        "jumlah_kata": len(kata_list),
        "jumlah_kalimat": teks.count(".") + teks.count("!") + teks.count("?"),
        "huruf_besar": sum(1 for c in teks if c.isupper()),
        "huruf_kecil": sum(1 for c in teks if c.islower()),
        "kata_terpanjang": max(kata_list, key=len),
    }


hasil = analisis_teks("Python adalah bahasa pemrograman. Python sangat populer!")
print("Hasil analisis:")
for key, val in hasil.items():
    print(f"  {key}: {val}")
print()


# ============================================================
# 5. RETURN LIST
# ============================================================
print("=" * 60)
print("5. RETURN LIST")
print("=" * 60)


def bilangan_prima(batas):
    """Return list bilangan prima sampai batas tertentu."""
    prima = []
    for num in range(2, batas + 1):
        is_prima = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prima = False
                break
        if is_prima:
            prima.append(num)
    return prima


def filter_genap(data):
    """Return hanya bilangan genap."""
    return [x for x in data if x % 2 == 0]


def urutkan_desc(data):
    """Return data terurut dari besar ke kecil (tanpa mengubah aslinya)."""
    return sorted(data, reverse=True)


print(f"Prima sampai 30:     {bilangan_prima(30)}")
print(f"Genap dari [1..10]:  {filter_genap(list(range(1, 11)))}")
print(f"Urut desc [5,2,8,1]: {urutkan_desc([5, 2, 8, 1])}")
print()


# ============================================================
# 6. RETURN FUNCTION (Higher-Order Function)
# ============================================================
print("=" * 60)
print("6. RETURN FUNCTION")
print("=" * 60)


def buat_pengali(faktor):
    """Return sebuah function baru."""
    def pengali(x):
        return x * faktor
    return pengali


kali2 = buat_pengali(2)
kali5 = buat_pengali(5)
kali10 = buat_pengali(10)

print(f"kali2(7)  = {kali2(7)}")
print(f"kali5(7)  = {kali5(7)}")
print(f"kali10(7) = {kali10(7)}")


def buat_formatter(prefix, suffix=""):
    """Return function formatter custom."""
    def formatter(value):
        return f"{prefix}{value}{suffix}"
    return formatter


format_rupiah = buat_formatter("Rp", ",-")
format_dollar = buat_formatter("$")
format_persen = buat_formatter("", "%")

print(f"\n{format_rupiah(50000)}")
print(format_dollar(100))
print(format_persen(85))
print()


# ============================================================
# 7. EARLY RETURN PATTERN (Guard Clause)
# ============================================================
print("=" * 60)
print("7. EARLY RETURN (Guard Clause)")
print("=" * 60)


# Tanpa early return (nested if - sulit dibaca)
def proses_pesanan_v1(pesanan):
    if pesanan is not None:
        if pesanan.get("item"):
            if pesanan.get("qty", 0) > 0:
                if pesanan.get("harga", 0) > 0:
                    return f"OK: {pesanan['qty']}x {pesanan['item']}"
                else:
                    return "ERROR: Harga tidak valid"
            else:
                return "ERROR: Qty tidak valid"
        else:
            return "ERROR: Item kosong"
    else:
        return "ERROR: Pesanan None"


# Dengan early return (guard clause - lebih bersih)
def proses_pesanan_v2(pesanan):
    if pesanan is None:
        return "ERROR: Pesanan None"
    if not pesanan.get("item"):
        return "ERROR: Item kosong"
    if pesanan.get("qty", 0) <= 0:
        return "ERROR: Qty tidak valid"
    if pesanan.get("harga", 0) <= 0:
        return "ERROR: Harga tidak valid"

    return f"OK: {pesanan['qty']}x {pesanan['item']}"


test_cases = [
    None,
    {},
    {"item": "Nasi", "qty": 0, "harga": 15000},
    {"item": "Nasi", "qty": 2, "harga": 15000},
]

print("Guard clause pattern:")
for p in test_cases:
    print(f"  {str(p):<45} -> {proses_pesanan_v2(p)}")

print()
print("=" * 60)
print("Selesai! Return value sudah dicontohkan.")
