"""
╔══════════════════════════════════════════════════╗
║   QUIZ 2: OPERATOR                               ║
║   (Arithmetic, Relational, Bitwise, Assignment,   ║
║    Identity, Membership)                          ║
║   Jalankan: python3 quiz_02_operator.py           ║
╚══════════════════════════════════════════════════╝
"""

from base64 import b64decode as _d

score = 0
total = 0

def _j(e):
    return _d(e).decode()


def tanya(nomor, soal, opsi, jawaban_enc, penjelasan=""):
    global score, total
    total += 1
    jawaban_benar = _j(jawaban_enc)
    print(f"\n{'─' * 50}")
    print(f"Soal {nomor}: {soal}")
    for key, val in opsi.items():
        print(f"  {key}. {val}")
    jawab = input(f"Jawaban Anda (a/b/c/d): ").strip().lower()
    if jawab == jawaban_benar:
        score += 1
        print(f"  ✅ BENAR!")
    else:
        print(f"  ❌ SALAH! Jawaban yang benar: {jawaban_benar}")
    if penjelasan:
        print(f"  💡 {penjelasan}")


def tanya_output(nomor, soal, kode, jawaban_enc, penjelasan=""):
    global score, total
    total += 1
    jawaban_benar = _j(jawaban_enc)
    print(f"\n{'─' * 50}")
    print(f"Soal {nomor}: {soal}")
    print(f"  Kode:")
    for line in kode.split("\n"):
        print(f"    {line}")
    jawab = input(f"Jawaban Anda: ").strip()
    if jawab == jawaban_benar:
        score += 1
        print(f"  ✅ BENAR!")
    else:
        print(f"  ❌ SALAH! Jawaban yang benar: {jawaban_benar}")
    if penjelasan:
        print(f"  💡 {penjelasan}")


print("╔══════════════════════════════════════════════════╗")
print("║            QUIZ 2: OPERATOR                      ║")
print("║            20 soal                                ║")
print("╚══════════════════════════════════════════════════╝")

# --- ARITHMETIC ---
print(f"\n{'═' * 50}")
print("BAGIAN A: ARITHMETIC OPERATORS")
print(f"{'═' * 50}")

tanya_output(1, "Apa output?", "print(17 % 5)",
    b"Mg==", "% (modulus) menghitung sisa bagi. 17 / 5 = 3 sisa 2.")

tanya_output(2, "Apa output?", "print(2 ** 5)",
    b"MzI=", "** adalah pangkat. 2^5 = 32.")

tanya_output(3, "Apa output?", "print(17 // 5)",
    b"Mw==", "// adalah floor division. 17 / 5 = 3.4, dibulatkan ke bawah = 3.")

tanya_output(4, "Apa output?", "print(10 / 3)",
    b"My4zMzMzMzMzMzMzMzMzMzM1", "/ selalu menghasilkan float. Bisa juga jawab 3.333... (pembulatan Python).")

# --- RELATIONAL ---
print(f"\n{'═' * 50}")
print("BAGIAN B: RELATIONAL OPERATORS")
print(f"{'═' * 50}")

tanya_output(5, "Apa output?", "print(10 == 10.0)",
    b"VHJ1ZQ==", "Python membandingkan nilai, bukan tipe. 10 (int) == 10.0 (float) -> True.")

tanya_output(6, "Apa output?", "print(5 != 5)",
    b"RmFsc2U=", "5 sama dengan 5, jadi 5 != 5 adalah False.")

tanya_output(7, "Apa output?", 'print("abc" < "abd")',
    b"VHJ1ZQ==", "String dibandingkan per karakter (lexicographic). 'c' < 'd' -> True.")

# --- ASSIGNMENT ---
print(f"\n{'═' * 50}")
print("BAGIAN C: ASSIGNMENT OPERATORS")
print(f"{'═' * 50}")

tanya_output(8, "Apa output?", "a = 10\na += 5\na *= 2\nprint(a)",
    b"MzA=", "a = 10, lalu a += 5 -> a = 15, lalu a *= 2 -> a = 30.")

tanya_output(9, "Apa output?", "x = 20\nx //= 3\nprint(x)",
    b"Ng==", "x //= 3 artinya x = x // 3 = 20 // 3 = 6.")

tanya(10, "Apa arti dari: a %= 7",
    {"a": "a = a % 7", "b": "a = 7 % a", "c": "a = a * 7", "d": "a = a / 7"},
    b"YQ==", "a %= 7 adalah shorthand untuk a = a % 7.")

# --- BITWISE ---
print(f"\n{'═' * 50}")
print("BAGIAN D: BITWISE OPERATORS")
print(f"{'═' * 50}")

tanya_output(11, "Apa output?", "print(12 & 10)",
    b"OA==", "12 = 1100, 10 = 1010. AND: 1100 & 1010 = 1000 = 8.")

tanya_output(12, "Apa output?", "print(12 | 10)",
    b"MTQ=", "12 = 1100, 10 = 1010. OR: 1100 | 1010 = 1110 = 14.")

tanya_output(13, "Apa output?", "print(5 << 2)",
    b"MjA=", "5 = 101. Left shift 2: 10100 = 20. (Sama dengan 5 * 4).")

tanya(14, "Apa fungsi operator ^ (caret) di Python?",
    {"a": "Pangkat", "b": "Bitwise XOR", "c": "Bitwise AND", "d": "Modulus"},
    b"Yg==", "^ adalah bitwise XOR. Untuk pangkat, gunakan ** (double asterisk).")

# --- IDENTITY ---
print(f"\n{'═' * 50}")
print("BAGIAN E: IDENTITY OPERATORS")
print(f"{'═' * 50}")

tanya_output(15, "Apa output?", "a = [1, 2]\nb = [1, 2]\nprint(a == b)",
    b"VHJ1ZQ==", "== membandingkan NILAI. Nilainya sama, jadi True.")

tanya_output(16, "Apa output?", "a = [1, 2]\nb = [1, 2]\nprint(a is b)",
    b"RmFsc2U=", "'is' membandingkan OBJEK (lokasi memori). a dan b adalah objek berbeda.")

tanya(17, "Kapan sebaiknya menggunakan 'is' daripada '=='?",
    {"a": "Membandingkan angka", "b": "Membandingkan string",
     "c": "Mengecek None", "d": "Membandingkan list"},
    b"Yw==", "Gunakan 'is' untuk cek None: if x is None. Untuk nilai lain, gunakan ==.")

# --- MEMBERSHIP ---
print(f"\n{'═' * 50}")
print("BAGIAN F: MEMBERSHIP OPERATORS")
print(f"{'═' * 50}")

tanya_output(18, "Apa output?", 'print("Python" in "Belajar Python Yuk")',
    b"VHJ1ZQ==", "'in' pada string mengecek apakah substring ada di string.")

tanya_output(19, "Apa output?", 'data = {"nama": "Budi", "umur": 25}\nprint("Budi" in data)',
    b"RmFsc2U=", "'in' pada dictionary mengecek KEY, bukan value. 'Budi' adalah value.")

tanya(20, "Apa output: print(3 not in [1, 2, 3, 4])?",
    {"a": "True", "b": "False", "c": "Error", "d": "None"},
    b"Yg==", "3 ADA di list [1,2,3,4], jadi 'not in' menghasilkan False.")

# --- HASIL ---
print(f"\n{'═' * 50}")
print(f"  HASIL QUIZ 2: OPERATOR")
print(f"{'═' * 50}")
print(f"  Skor: {score}/{total}")
persen = score / total * 100
if persen >= 80:
    print(f"  Grade: A ({persen:.0f}%) - Excellent! 🎉")
elif persen >= 60:
    print(f"  Grade: B ({persen:.0f}%) - Bagus! 👍")
elif persen >= 40:
    print(f"  Grade: C ({persen:.0f}%) - Perlu belajar lagi 📖")
else:
    print(f"  Grade: D ({persen:.0f}%) - Review materi dari awal 🔄")
print(f"{'═' * 50}")
