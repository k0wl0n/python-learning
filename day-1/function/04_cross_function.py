"""
=== CROSS FUNCTION (Function Memanggil Function Lain) ===

Function bisa memanggil function lain di dalam body-nya.
Ini adalah dasar dari pemrograman modular:
    - Pecah masalah besar jadi function kecil-kecil
    - Setiap function punya 1 tugas (Single Responsibility)
    - Function kecil bisa dipakai ulang (Reusability)
"""


# ============================================================
# 1. FUNCTION MEMANGGIL FUNCTION LAIN (Dasar)
# ============================================================
print("=" * 60)
print("1. CROSS FUNCTION DASAR")
print("=" * 60)


def kuadrat(x):
    return x ** 2


def jumlah_kuadrat(a, b):
    """Memanggil function kuadrat() di dalamnya."""
    return kuadrat(a) + kuadrat(b)


print(f"kuadrat(3) = {kuadrat(3)}")
print(f"kuadrat(4) = {kuadrat(4)}")
print(f"jumlah_kuadrat(3, 4) = {jumlah_kuadrat(3, 4)}")  # 9 + 16 = 25
print()


# ============================================================
# 2. CHAIN OF FUNCTIONS (Rantai Function)
# ============================================================
print("=" * 60)
print("2. CHAIN OF FUNCTIONS")
print("=" * 60)


def bersihkan(teks):
    """Step 1: Bersihkan whitespace."""
    return teks.strip()


def kapitalkan(teks):
    """Step 2: Kapitalkan setiap kata."""
    return teks.title()


def tambah_sapaan(nama):
    """Step 3: Tambah sapaan."""
    return f"Halo, {nama}! Selamat datang."


def proses_nama(raw_input):
    """Merangkai 3 function menjadi satu pipeline."""
    bersih = bersihkan(raw_input)
    kapital = kapitalkan(bersih)
    hasil = tambah_sapaan(kapital)
    return hasil


# Setiap function bisa dipakai sendiri-sendiri
print(f"bersihkan('  hello  ') = '{bersihkan('  hello  ')}'")
print(f"kapitalkan('budi santoso') = '{kapitalkan('budi santoso')}'")
print()

# Atau dirangkai
print(proses_nama("  budi santoso  "))
print(proses_nama("  rina permata sari  "))
print()


# ============================================================
# 3. HELPER FUNCTIONS (Fungsi Pembantu)
# ============================================================
print("=" * 60)
print("3. HELPER FUNCTIONS")
print("=" * 60)


# --- Helper functions ---
def is_valid_email(email):
    """Cek apakah email valid (sederhana)."""
    return "@" in email and "." in email.split("@")[-1]


def is_strong_password(password):
    """Cek apakah password kuat."""
    if len(password) < 8:
        return False, "Minimal 8 karakter"
    if not any(c.isupper() for c in password):
        return False, "Harus ada huruf besar"
    if not any(c.isdigit() for c in password):
        return False, "Harus ada angka"
    return True, "Password kuat"


def format_rupiah(angka):
    """Format angka ke Rupiah."""
    return f"Rp{angka:,.0f}"


# --- Function utama yang menggunakan helpers ---
def registrasi(nama, email, password):
    """Function utama yang memanggil helper functions."""
    print(f"  Registrasi: {nama}")

    # Pakai helper is_valid_email
    if not is_valid_email(email):
        print(f"    ❌ Email '{email}' tidak valid")
        return False

    # Pakai helper is_strong_password
    kuat, pesan = is_strong_password(password)
    if not kuat:
        print(f"    ❌ Password lemah: {pesan}")
        return False

    print(f"    ✅ Registrasi berhasil!")
    return True


registrasi("Budi", "budi@email.com", "Rahasia123")
registrasi("Rina", "rina-email", "Rahasia123")
registrasi("Andi", "andi@mail.com", "123")
print()


# ============================================================
# 4. FUNCTION COMPOSITION (Komposisi)
# ============================================================
print("=" * 60)
print("4. FUNCTION COMPOSITION")
print("=" * 60)


def hitung_subtotal(harga, qty):
    return harga * qty


def hitung_diskon(subtotal, persen_diskon):
    return subtotal * persen_diskon / 100


def hitung_pajak(subtotal, persen_pajak=10):
    return subtotal * persen_pajak / 100


def format_struk(item, subtotal, diskon, pajak, total):
    """Menampilkan struk belanja."""
    print(f"  Item:     {item}")
    print(f"  Subtotal: {format_rupiah(subtotal)}")
    print(f"  Diskon:   -{format_rupiah(diskon)}")
    print(f"  Pajak:    +{format_rupiah(pajak)}")
    print(f"  ─────────────────")
    print(f"  TOTAL:    {format_rupiah(total)}")


def proses_pembelian(item, harga, qty, persen_diskon=0):
    """Function utama yang mengkomposisikan semua function."""
    subtotal = hitung_subtotal(harga, qty)
    diskon = hitung_diskon(subtotal, persen_diskon)
    setelah_diskon = subtotal - diskon
    pajak = hitung_pajak(setelah_diskon)
    total = setelah_diskon + pajak
    format_struk(item, subtotal, diskon, pajak, total)
    return total


print("Struk Belanja:")
proses_pembelian("Laptop ASUS", 8500000, 1, persen_diskon=15)
print()


# ============================================================
# 5. RECURSIVE FUNCTION (Fungsi Memanggil Dirinya Sendiri)
# ============================================================
print("=" * 60)
print("5. RECURSIVE FUNCTION")
print("=" * 60)


def faktorial(n):
    """n! = n * (n-1) * (n-2) * ... * 1"""
    if n <= 1:        # base case (kondisi berhenti)
        return 1
    return n * faktorial(n - 1)  # recursive case


def fibonacci(n):
    """Menghitung bilangan fibonacci ke-n."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def hitung_mundur(n):
    """Hitung mundur dari n sampai 0."""
    if n < 0:
        print("  GO!")
        return
    print(f"  {n}...")
    hitung_mundur(n - 1)


print(f"faktorial(5) = 5! = {faktorial(5)}")
print(f"faktorial(10) = 10! = {faktorial(10)}")
print()

print("Fibonacci ke-0 sampai ke-10:")
fib = [fibonacci(i) for i in range(11)]
print(f"  {fib}")
print()

hitung_mundur(5)
print()


# ============================================================
# 6. DECORATOR (Function Membungkus Function)
# ============================================================
print("=" * 60)
print("6. DECORATOR")
print("=" * 60)

import time


def timer(func):
    """Decorator: mengukur waktu eksekusi function."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  ⏱ {func.__name__} selesai dalam {elapsed:.6f} detik")
        return result
    return wrapper


def logger(func):
    """Decorator: mencatat pemanggilan function."""
    def wrapper(*args, **kwargs):
        print(f"  📝 Memanggil {func.__name__}(args={args}, kwargs={kwargs})")
        result = func(*args, **kwargs)
        print(f"  📝 {func.__name__} return: {result}")
        return result
    return wrapper


@timer
def hitung_berat(jumlah):
    """Function dengan decorator @timer."""
    total = sum(range(jumlah))
    return total


@logger
def tambah(a, b):
    return a + b


print("Dengan @timer:")
hitung_berat(1_000_000)
print()

print("Dengan @logger:")
tambah(10, 20)

print()
print("=" * 60)
print("Selesai! Cross function sudah dicontohkan.")
