"""
=== HELPERS.PY ===

File ini berisi kumpulan function yang bisa di-import dari file lain.
Ini adalah contoh cara membuat MODULE / LIBRARY sendiri.

Cara import dari file lain:
    from helpers import format_rupiah, hitung_diskon
    import helpers
"""


# ============================================================
# FORMATTING FUNCTIONS
# ============================================================

def format_rupiah(angka):
    """Format angka ke format Rupiah."""
    return f"Rp{angka:,.0f}"


def format_persen(angka):
    """Format angka ke persen."""
    return f"{angka:.1f}%"


def format_nama(nama):
    """Bersihkan dan kapitalkan nama."""
    return nama.strip().title()


# ============================================================
# MATH / CALCULATION FUNCTIONS
# ============================================================

def hitung_diskon(harga, persen):
    """Hitung harga setelah diskon."""
    potongan = harga * persen / 100
    return harga - potongan


def hitung_pajak(harga, persen=11):
    """Hitung pajak dari harga."""
    return harga * persen / 100


def hitung_bmi(berat, tinggi):
    """Hitung BMI. Tinggi dalam meter."""
    return berat / (tinggi ** 2)


def celcius_ke_fahrenheit(celcius):
    """Konversi Celcius ke Fahrenheit."""
    return (celcius * 9 / 5) + 32


def fahrenheit_ke_celcius(fahrenheit):
    """Konversi Fahrenheit ke Celcius."""
    return (fahrenheit - 32) * 5 / 9


# ============================================================
# VALIDATION FUNCTIONS
# ============================================================

def is_valid_email(email):
    """Cek apakah email valid (sederhana)."""
    if not email or not isinstance(email, str):
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    if not parts[0] or not parts[1]:
        return False
    if "." not in parts[1]:
        return False
    return True


def is_valid_phone(phone):
    """Cek apakah nomor telepon valid (Indonesia)."""
    cleaned = phone.replace("-", "").replace(" ", "")
    if not cleaned.startswith(("08", "+62", "62")):
        return False
    digits = cleaned.lstrip("+")
    return digits.isdigit() and 10 <= len(digits) <= 14


def is_strong_password(password):
    """Cek kekuatan password. Return (bool, pesan)."""
    if len(password) < 8:
        return False, "Minimal 8 karakter"
    if not any(c.isupper() for c in password):
        return False, "Harus ada huruf besar"
    if not any(c.islower() for c in password):
        return False, "Harus ada huruf kecil"
    if not any(c.isdigit() for c in password):
        return False, "Harus ada angka"
    return True, "Password kuat"


# ============================================================
# DATA PROCESSING FUNCTIONS
# ============================================================

def hitung_statistik(data):
    """Hitung statistik dasar dari list angka."""
    if not data:
        return None
    return {
        "count": len(data),
        "sum": sum(data),
        "min": min(data),
        "max": max(data),
        "avg": sum(data) / len(data),
    }


def cari_item(data_list, key, value):
    """Cari item dalam list of dict berdasarkan key-value."""
    for item in data_list:
        if item.get(key) == value:
            return item
    return None


def filter_data(data_list, key, kondisi):
    """Filter list of dict berdasarkan kondisi (function)."""
    return [item for item in data_list if kondisi(item.get(key))]


# ============================================================
# GRADE / RATING FUNCTIONS
# ============================================================

def nilai_ke_grade(nilai):
    """Konversi nilai angka ke grade huruf."""
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    elif nilai >= 60:
        return "D"
    return "E"


def grade_ke_bobot(grade):
    """Konversi grade huruf ke bobot angka."""
    bobot = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}
    return bobot.get(grade, 0.0)


# Agar bisa di-test langsung: python helpers.py
if __name__ == "__main__":
    print("=== Testing helpers.py ===")
    print(f"format_rupiah(50000) = {format_rupiah(50000)}")
    print(f"hitung_diskon(100000, 20) = {format_rupiah(hitung_diskon(100000, 20))}")
    print(f"is_valid_email('test@mail.com') = {is_valid_email('test@mail.com')}")
    print(f"nilai_ke_grade(85) = {nilai_ke_grade(85)}")
    print("Semua test OK!")
