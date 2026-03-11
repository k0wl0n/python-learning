"""
╔══════════════════════════════════════════════════╗
║   QUIZ 1: VARIABEL & TIPE DATA                  ║
║   Jalankan: python3 quiz_01_variabel_tipe_data.py║
╚══════════════════════════════════════════════════╝
"""

from base64 import b64decode as _d

score = 0
total = 0

def _j(encoded):
    return _d(encoded).decode()


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


# ============================================================
print("╔══════════════════════════════════════════════════╗")
print("║        QUIZ 1: VARIABEL & TIPE DATA             ║")
print("║        10 soal pilihan ganda + 5 tebak output    ║")
print("╚══════════════════════════════════════════════════╝")

# --- PILIHAN GANDA ---
# Jawaban di-encode base64 agar tidak mudah dibaca langsung

tanya(1,
    "Manakah yang merupakan nama variabel VALID di Python?",
    {"a": "2nama", "b": "nama-saya", "c": "nama_saya", "d": "class"},
    b"Yw==",
    "Variabel tidak boleh dimulai angka, tidak boleh pakai '-', dan 'class' adalah reserved word."
)

tanya(2,
    "Apa tipe data dari: x = 3.14",
    {"a": "int", "b": "float", "c": "str", "d": "complex"},
    b"Yg==",
    "Angka dengan titik desimal otomatis bertipe float."
)

tanya(3,
    "Apa tipe data dari: x = '123'",
    {"a": "int", "b": "float", "c": "str", "d": "list"},
    b"Yw==",
    "Apapun yang diapit tanda kutip adalah string, meskipun isinya angka."
)

tanya(4,
    "Apa tipe data dari: x = True",
    {"a": "str", "b": "int", "c": "bool", "d": "float"},
    b"Yw==",
    "True dan False adalah tipe boolean (bool)."
)

tanya(5,
    "Apa tipe data dari: x = [1, 2, 3]",
    {"a": "tuple", "b": "set", "c": "dict", "d": "list"},
    b"ZA==",
    "Tanda [ ] menandakan list."
)

tanya(6,
    "Apa tipe data dari: x = (1, 2, 3)",
    {"a": "list", "b": "tuple", "c": "set", "d": "dict"},
    b"Yg==",
    "Tanda ( ) menandakan tuple."
)

tanya(7,
    "Apa tipe data dari: x = {'a': 1, 'b': 2}",
    {"a": "set", "b": "list", "c": "dict", "d": "tuple"},
    b"Yw==",
    "Tanda { } dengan key:value menandakan dictionary."
)

tanya(8,
    "Apa hasil dari: type(10 / 3)?",
    {"a": "int", "b": "float", "c": "str", "d": "complex"},
    b"Yg==",
    "Operator / selalu menghasilkan float, meskipun hasilnya bulat."
)

tanya(9,
    "Apa hasil dari: bool(0)?",
    {"a": "True", "b": "False", "c": "0", "d": "Error"},
    b"Yg==",
    "0, '', [], None, False -> semuanya bernilai False."
)

tanya(10,
    "Mana yang BUKAN tipe data numeric di Python?",
    {"a": "int", "b": "float", "c": "complex", "d": "string"},
    b"ZA==",
    "Tipe numeric: int, float, complex. String bukan numeric."
)

# --- TEBAK OUTPUT ---

print(f"\n{'=' * 50}")
print("BAGIAN 2: TEBAK OUTPUT")
print("Ketik output yang dihasilkan kode berikut:")
print(f"{'=' * 50}")

tanya_output(11,
    "Apa output dari kode ini?",
    'x = 10\nprint(type(x).__name__)',
    b"aW50",
    "type(x).__name__ mengembalikan nama tipe sebagai string."
)

tanya_output(12,
    "Apa output dari kode ini?",
    'a = "5"\nb = 3\nprint(int(a) + b)',
    b"OA==",
    "int('5') mengkonversi string '5' menjadi integer 5, lalu 5 + 3 = 8."
)

tanya_output(13,
    "Apa output dari kode ini?",
    'x = 7\ny = 2\nprint(x // y)',
    b"Mw==",
    "// adalah floor division (pembagian bulat). 7 // 2 = 3."
)

tanya_output(14,
    "Apa output dari kode ini?",
    'a, b, c = 1, 2, 3\nprint(a + b + c)',
    b"Ng==",
    "Python mendukung multiple assignment: a=1, b=2, c=3."
)

tanya_output(15,
    "Apa output dari kode ini?",
    'x = "Python"\nprint(len(x))',
    b"Ng==",
    "len() menghitung panjang string. 'Python' = 6 karakter."
)

# --- HASIL ---
print(f"\n{'═' * 50}")
print(f"  HASIL QUIZ 1: VARIABEL & TIPE DATA")
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
