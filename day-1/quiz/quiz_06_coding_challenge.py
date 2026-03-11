"""
╔══════════════════════════════════════════════════╗
║   QUIZ 6: CODING CHALLENGE                       ║
║   Tulis kode untuk menyelesaikan soal!           ║
║   Jalankan: python3 quiz_06_coding_challenge.py  ║
╚══════════════════════════════════════════════════╝

INSTRUKSI:
    - Di bawah setiap soal, ada function kosong yang harus Anda isi
    - Ganti 'pass' dengan kode jawaban Anda
    - Jalankan file ini untuk mengecek jawaban otomatis
    - Setiap soal memiliki beberapa test case
    - Expected values di-encode agar tidak bisa dilihat langsung
"""

from base64 import b64decode as _d
import json

score = 0
total_tests = 0


def _j(e):
    """Decode base64 lalu parse JSON untuk mendapatkan expected value."""
    return json.loads(_d(e).decode())


def cek(nama_soal, fungsi, test_cases_enc):
    """Jalankan test cases untuk sebuah soal. Expected di-encode base64."""
    global score, total_tests
    print(f"\n{'─' * 50}")
    print(f"  {nama_soal}")
    print(f"{'─' * 50}")
    lulus = 0
    gagal = 0
    for args, expected_enc in test_cases_enc:
        total_tests += 1
        expected = _j(expected_enc)
        try:
            if isinstance(args, tuple):
                result = fungsi(*args)
            else:
                result = fungsi(args)

            if result == expected:
                lulus += 1
                score += 1
                print(f"  ✅ {nama_soal}({args}) = {result}")
            else:
                gagal += 1
                print(f"  ❌ {nama_soal}({args}) = {result}, expected: {expected}")
        except Exception as e:
            gagal += 1
            print(f"  ❌ {nama_soal}({args}) -> ERROR: {e}")

    status = "PASSED ✅" if gagal == 0 else f"FAILED ({gagal} gagal) ❌"
    print(f"  Hasil: {lulus}/{lulus + gagal} test - {status}")


# ============================================================
# SOAL 1: Genap atau Ganjil
# ============================================================
# Buat function yang menerima angka dan mengembalikan
# "genap" jika genap, "ganjil" jika ganjil
# ============================================================

def genap_ganjil(n):
    # Ternary operator: cek modulus 2
    return "genap" if n % 2 == 0 else "ganjil"


cek("Soal 1: genap_ganjil", genap_ganjil, [
    (2, b"ImdlbmFwIg=="), (7, b"ImdhbmppbCI="), (0, b"ImdlbmFwIg=="),
    (-3, b"ImdhbmppbCI="), (100, b"ImdlbmFwIg=="),
])


# ============================================================
# SOAL 2: Hitung Huruf Vokal
# ============================================================
# Buat function yang menghitung jumlah huruf vokal (a, i, u, e, o)
# dalam sebuah string (case insensitive)
# ============================================================

def hitung_vokal(teks):
    # Set vokal, string method .lower(), sum + generator
    vokal = "aiueo"
    return sum(1 for c in teks.lower() if c in vokal)


cek("Soal 2: hitung_vokal", hitung_vokal, [
    ("hello", b"Mg=="), ("PYTHON", b"MQ=="), ("aeiou", b"NQ=="),
    ("bcd", b"MA=="), ("Belajar Python", b"NA=="),
])


# ============================================================
# SOAL 3: Balik String
# ============================================================
# Buat function yang membalik string
# Contoh: "hello" -> "olleh"
# ============================================================

def balik_string(teks):
    # String slicing dengan step -1 membalik string
    return teks[::-1]


cek("Soal 3: balik_string", balik_string, [
    ("hello", b"Im9sbGVoIg=="), ("Python", b"Im5vaHR5UCI="),
    ("12345", b"IjU0MzIxIg=="), ("a", b"ImEi"), ("", b"IiI="),
])


# ============================================================
# SOAL 4: Nilai Maksimum
# ============================================================
# Buat function yang mencari nilai terbesar dari sebuah list
# TANPA menggunakan fungsi max() bawaan
# ============================================================

def cari_max(data):
    # Tanpa max() bawaan: asumsikan elemen pertama sebagai max, loop selebihnya
    maksimum = data[0]
    for angka in data[1:]:
        if angka > maksimum:
            maksimum = angka
    return maksimum


cek("Soal 4: cari_max", cari_max, [
    ([3, 1, 4, 1, 5], b"NQ=="), ([10], b"MTA="),
    ([-3, -1, -4], b"LTE="), ([100, 99, 98], b"MTAw"),
])


# ============================================================
# SOAL 5: Hapus Duplikat (Jaga Urutan)
# ============================================================
# Buat function yang menghapus elemen duplikat dari list
# sambil menjaga urutan asli
# Contoh: [1, 2, 2, 3, 1] -> [1, 2, 3]
# ============================================================

def hapus_duplikat(data):
    # Set untuk tracking yang sudah dilihat, list untuk jaga urutan
    sudah_ada = set()
    hasil = []
    for item in data:
        if item not in sudah_ada:
            sudah_ada.add(item)
            hasil.append(item)
    return hasil


cek("Soal 5: hapus_duplikat", hapus_duplikat, [
    ([1, 2, 2, 3, 1], b"WzEsIDIsIDNd"),
    ([1, 1, 1], b"WzFd"),
    ([1, 2, 3], b"WzEsIDIsIDNd"),
    ([], b"W10="),
])


# ============================================================
# SOAL 6: FizzBuzz
# ============================================================
# Buat function yang menerima angka n dan mengembalikan list:
# - "Fizz" jika kelipatan 3
# - "Buzz" jika kelipatan 5
# - "FizzBuzz" jika kelipatan 3 DAN 5
# - angka itu sendiri (string) jika bukan keduanya
# Contoh: fizzbuzz(5) -> ["1", "2", "Fizz", "4", "Buzz"]
# ============================================================

def fizzbuzz(n):
    # Cek kelipatan 15 dulu (FizzBuzz), baru 3, baru 5
    hasil = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            hasil.append("FizzBuzz")
        elif i % 3 == 0:
            hasil.append("Fizz")
        elif i % 5 == 0:
            hasil.append("Buzz")
        else:
            hasil.append(str(i))
    return hasil


cek("Soal 6: fizzbuzz", fizzbuzz, [
    (5, b"WyIxIiwgIjIiLCAiRml6eiIsICI0IiwgIkJ1enoiXQ=="),
    (3, b"WyIxIiwgIjIiLCAiRml6eiJd"),
    (15, b"WyIxIiwgIjIiLCAiRml6eiIsICI0IiwgIkJ1enoiLCAiRml6eiIsICI3IiwgIjgiLCAiRml6eiIsICJCdXp6IiwgIjExIiwgIkZpenoiLCAiMTMiLCAiMTQiLCAiRml6ekJ1enoiXQ=="),
])


# ============================================================
# SOAL 7: Hitung Kata
# ============================================================
# Buat function yang menghitung frekuensi setiap kata dalam string
# Return dictionary {kata: jumlah}
# Contoh: "hi hi hello" -> {"hi": 2, "hello": 1}
# ============================================================

def hitung_kata(teks):
    # String kosong → dict kosong, else split + hitung frekuensi
    if not teks:
        return {}
    frekuensi = {}
    for kata in teks.split():
        frekuensi[kata] = frekuensi.get(kata, 0) + 1
    return frekuensi


cek("Soal 7: hitung_kata", hitung_kata, [
    ("hi hi hello", b"eyJoaSI6IDIsICJoZWxsbyI6IDF9"),
    ("a b a b a", b"eyJhIjogMywgImIiOiAyfQ=="),
    ("python", b"eyJweXRob24iOiAxfQ=="),
    ("", b"e30="),
])


# ============================================================
# SOAL 8: Celsius ke Fahrenheit (List)
# ============================================================
# Buat function yang menerima list suhu Celsius
# dan mengembalikan list suhu dalam Fahrenheit
# Rumus: F = C * 9/5 + 32
# Bulatkan ke 1 desimal
# ============================================================

def celsius_list_ke_fahrenheit(celsius_list):
    # Rumus F = C * 9/5 + 32, list comprehension + round 1 desimal
    return [round(c * 9 / 5 + 32, 1) for c in celsius_list]


cek("Soal 8: celsius_ke_fahrenheit", celsius_list_ke_fahrenheit, [
    ([0, 100], b"WzMyLjAsIDIxMi4wXQ=="),
    ([37], b"Wzk4LjZd"),
    ([-40], b"Wy00MC4wXQ=="),
])


# ============================================================
# SOAL 9: Flatten Nested List
# ============================================================
# Buat function yang meratakan nested list 2 level menjadi 1 level
# Contoh: [[1, 2], [3, 4], [5]] -> [1, 2, 3, 4, 5]
# ============================================================

def flatten(nested):
    # Nested list comprehension: loop sublist, lalu loop item di dalamnya
    return [item for sublist in nested for item in sublist]


cek("Soal 9: flatten", flatten, [
    ([[1, 2], [3, 4], [5]], b"WzEsIDIsIDMsIDQsIDVd"),
    ([[1], [2], [3]], b"WzEsIDIsIDNd"),
    ([[], [1, 2], []], b"WzEsIDJd"),
    ([], b"W10="),
])


# ============================================================
# SOAL 10: Grading System
# ============================================================
# Buat function yang menerima list nilai (angka)
# dan mengembalikan dictionary berisi:
# - "grades": list grade (A>=85, B>=75, C>=65, D>=55, E<55)
# - "avg": rata-rata (bulatkan 1 desimal)
# - "highest": nilai tertinggi
# - "lowest": nilai terendah
# - "pass_count": jumlah yang lulus (grade A, B, atau C)
# ============================================================

def grading(nilai_list):
    # Helper: tentukan grade satu nilai (if/elif/else)
    def get_grade(n):
        if n >= 85:
            return "A"
        elif n >= 75:
            return "B"
        elif n >= 65:
            return "C"
        elif n >= 55:
            return "D"
        else:
            return "E"

    grades = [get_grade(n) for n in nilai_list]
    avg = round(sum(nilai_list) / len(nilai_list), 1)
    pass_count = sum(1 for g in grades if g in {"A", "B", "C"})

    return {
        "grades": grades,
        "avg": avg,
        "highest": max(nilai_list),
        "lowest": min(nilai_list),
        "pass_count": pass_count,
    }


cek("Soal 10: grading", grading, [
    ([90, 80, 70, 60, 50], b"eyJncmFkZXMiOiBbIkEiLCAiQiIsICJDIiwgIkQiLCAiRSJdLCAiYXZnIjogNzAuMCwgImhpZ2hlc3QiOiA5MCwgImxvd2VzdCI6IDUwLCAicGFzc19jb3VudCI6IDN9"),
    ([100, 85], b"eyJncmFkZXMiOiBbIkEiLCAiQSJdLCAiYXZnIjogOTIuNSwgImhpZ2hlc3QiOiAxMDAsICJsb3dlc3QiOiA4NSwgInBhc3NfY291bnQiOiAyfQ=="),
])


# ============================================================
# HASIL AKHIR
# ============================================================
print(f"\n{'═' * 50}")
print(f"  HASIL QUIZ 6: CODING CHALLENGE")
print(f"{'═' * 50}")
print(f"  Test lulus: {score}/{total_tests}")

if total_tests > 0:
    persen = score / total_tests * 100
    if persen == 100:
        print(f"  PERFECT SCORE! ({persen:.0f}%) 🏆🎉")
    elif persen >= 80:
        print(f"  Grade: A ({persen:.0f}%) - Excellent! 🎉")
    elif persen >= 60:
        print(f"  Grade: B ({persen:.0f}%) - Bagus! 👍")
    elif persen >= 40:
        print(f"  Grade: C ({persen:.0f}%) - Perlu belajar lagi 📖")
    elif persen > 0:
        print(f"  Grade: D ({persen:.0f}%) - Ayo coba lagi! 💪")
    else:
        print(f"  Skor 0% - Isi kode di setiap function, ganti 'pass'! 📝")
else:
    print(f"  Tidak ada test yang berjalan")

print(f"""
{'═' * 50}
  PETUNJUK:
  - Buka file ini di editor
  - Ganti 'pass' di setiap function dengan kode Anda
  - Jalankan ulang untuk cek jawaban
  - Contoh:

    def genap_ganjil(n):
        return "genap" if n % 2 == 0 else "ganjil"

{'═' * 50}""")
