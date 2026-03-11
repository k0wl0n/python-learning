"""
╔══════════════════════════════════════════════════╗
║   QUIZ 3: STRING METHODS & OPERATIONS            ║
║   Jalankan: python3 quiz_03_string_method.py     ║
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
print("║         QUIZ 3: STRING METHODS                   ║")
print("║         15 soal                                   ║")
print("╚══════════════════════════════════════════════════╝")

tanya_output(1, "Apa output?",
    'nama = "python"\nprint(nama.upper())',
    b"UFlUSE9O", "upper() mengubah semua huruf menjadi huruf besar.")

tanya_output(2, "Apa output?",
    'teks = "Hello World"\nprint(teks.lower())',
    b"aGVsbG8gd29ybGQ=", "lower() mengubah semua huruf menjadi huruf kecil.")

tanya_output(3, "Apa output?",
    'teks = "belajar python programming"\nprint(teks.title())',
    b"QmVsYWphciBQeXRob24gUHJvZ3JhbW1pbmc=",
    "title() membuat huruf pertama setiap kata menjadi besar.")

tanya_output(4, "Apa output?",
    'teks = "  hello  "\nprint(teks.strip())',
    b"aGVsbG8=", "strip() menghapus whitespace di awal dan akhir string.")

tanya_output(5, "Apa output?",
    'print("a-b-c-d".split("-"))',
    b"WydhJywgJ2InLCAnYycsICdkJ10=",
    "split('-') memecah string berdasarkan delimiter '-'.")

tanya_output(6, "Apa output?",
    'print("-".join(["x", "y", "z"]))',
    b"eC15LXo=", "join() menggabungkan list menjadi string dengan separator '-'.")

tanya_output(7, "Apa output?",
    'teks = "Python Programming"\nprint(teks.find("gram"))',
    b"MTE=", "find() mengembalikan index pertama substring ditemukan.")

tanya_output(8, "Apa output?",
    'teks = "Hello World"\nprint(teks.replace("World", "Python"))',
    b"SGVsbG8gUHl0aG9u", "replace() mengganti substring lama dengan yang baru.")

tanya(9, "Apa perbedaan find() dan index()?",
    {"a": "Tidak ada perbedaan",
     "b": "find() return -1 jika tidak ditemukan, index() raise Error",
     "c": "find() lebih cepat",
     "d": "index() hanya untuk list"},
    b"Yg==",
    "find() return -1, index() raise ValueError jika substring tidak ditemukan.")

tanya_output(10, "Apa output?",
    'print("hello123".isalpha())',
    b"RmFsc2U=",
    "isalpha() return True hanya jika SEMUA karakter adalah huruf. '123' bukan huruf.")

tanya_output(11, "Apa output?",
    'print("12345".isdigit())',
    b"VHJ1ZQ==", "isdigit() return True jika semua karakter adalah angka.")

tanya_output(12, "Apa output?",
    'teks = "Python"\nprint(teks[0] + teks[-1])',
    b"UG4=", "teks[0] = 'P' (pertama), teks[-1] = 'n' (terakhir). Digabung = 'Pn'.")

tanya_output(13, "Apa output?",
    'teks = "Hello"\nprint(teks[::-1])',
    b"b2xsZUg=", "[::-1] membalik urutan string.")

tanya(14, "Apa hasil dari: 'Python'.startswith('Py')?",
    {"a": "True", "b": "False", "c": "Error", "d": "'Py'"},
    b"YQ==",
    "startswith() mengecek apakah string dimulai dengan substring tertentu.")

tanya_output(15, "Apa output?",
    'print("ha" * 3)',
    b"aGFoYWhh", "Operator * pada string mengulang string sejumlah n kali.")

# --- HASIL ---
print(f"\n{'═' * 50}")
print(f"  HASIL QUIZ 3: STRING METHODS")
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
