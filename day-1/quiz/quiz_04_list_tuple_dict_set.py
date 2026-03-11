"""
╔══════════════════════════════════════════════════╗
║   QUIZ 4: LIST, TUPLE, DICTIONARY, SET           ║
║   Jalankan: python3 quiz_04_list_tuple_dict_set.py║
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
print("║     QUIZ 4: LIST, TUPLE, DICTIONARY, SET         ║")
print("║     20 soal                                       ║")
print("╚══════════════════════════════════════════════════╝")

# --- LIST ---
print(f"\n{'═' * 50}")
print("BAGIAN A: LIST")
print(f"{'═' * 50}")

tanya_output(1, "Apa output?",
    'buah = ["apel", "jeruk", "mangga"]\nbuah.append("pisang")\nprint(len(buah))',
    b"NA==", "Awalnya 3 elemen, append menambah 1, jadi total 4.")

tanya_output(2, "Apa output?",
    'angka = [10, 20, 30, 40, 50]\nprint(angka[1:4])',
    b"WzIwLCAzMCwgNDBd", "Slicing [1:4] mengambil index 1, 2, 3 (stop tidak termasuk).")

tanya_output(3, "Apa output?",
    'data = [3, 1, 4, 1, 5]\ndata.sort()\nprint(data)',
    b"WzEsIDEsIDMsIDQsIDVd", "sort() mengurutkan list dari kecil ke besar (in-place).")

tanya_output(4, "Apa output?",
    'a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)',
    b"WzEsIDIsIDMsIDRd",
    "b = a hanya membuat referensi, bukan copy. Keduanya menunjuk objek yang sama.")

tanya(5, "Bagaimana cara membuat COPY list yang benar?",
    {"a": "b = a", "b": "b = a.copy()", "c": "b = a.append()", "d": "b = a.sort()"},
    b"Yg==", "a.copy() atau a[:] membuat shallow copy. b = a hanya referensi.")

# --- TUPLE ---
print(f"\n{'═' * 50}")
print("BAGIAN B: TUPLE")
print(f"{'═' * 50}")

tanya(6, "Apa yang terjadi jika kita mengubah elemen tuple?",
    {"a": "Berhasil diubah", "b": "TypeError", "c": "None", "d": "Diam-diam diabaikan"},
    b"Yg==", "Tuple bersifat immutable. Mengubah elemen akan raise TypeError.")

tanya_output(7, "Apa output?",
    'data = (10, 20, 30, 20, 10)\nprint(data.count(20))',
    b"Mg==", "count() menghitung jumlah kemunculan elemen. 20 muncul 2 kali.")

tanya(8, "Keunggulan tuple dibanding list?",
    {"a": "Bisa diubah", "b": "Lebih banyak method",
     "c": "Lebih hemat memori & bisa jadi key dict", "d": "Lebih banyak fitur"},
    b"Yw==", "Tuple lebih hemat memori dan bisa jadi key dictionary (karena immutable).")

tanya_output(9, "Apa output?",
    'x, y, z = (1, 2, 3)\nprint(y)',
    b"Mg==", "Tuple unpacking: x=1, y=2, z=3.")

# --- DICTIONARY ---
print(f"\n{'═' * 50}")
print("BAGIAN C: DICTIONARY")
print(f"{'═' * 50}")

tanya_output(10, "Apa output?",
    'data = {"nama": "Budi", "umur": 25}\nprint(data["nama"])',
    b"QnVkaQ==", "Akses value di dictionary menggunakan key.")

tanya_output(11, "Apa output?",
    'data = {"a": 1, "b": 2, "c": 3}\nprint(list(data.keys()))',
    b"WydhJywgJ2InLCAnYydd", "keys() mengembalikan semua key dalam dictionary.")

tanya_output(12, "Apa output?",
    'data = {"x": 10}\ndata["y"] = 20\nprint(len(data))',
    b"Mg==", "Menambah key baru 'y'. Sekarang ada 2 pasangan key-value.")

tanya(13, "Apa yang terjadi jika kita akses key yang tidak ada: data['z']?",
    {"a": "Return None", "b": "Return 0", "c": "KeyError", "d": "Return False"},
    b"Yw==",
    "Akses key yang tidak ada = KeyError. Gunakan data.get('z') untuk aman (return None).")

tanya_output(14, "Apa output?",
    'data = {"a": 1, "b": 2}\nprint(data.get("c", 0))',
    b"MA==", "get() dengan default value. Key 'c' tidak ada, jadi return default 0.")

# --- SET ---
print(f"\n{'═' * 50}")
print("BAGIAN D: SET")
print(f"{'═' * 50}")

tanya_output(15, "Apa output?",
    'data = {1, 2, 2, 3, 3, 3}\nprint(len(data))',
    b"Mw==", "Set otomatis menghapus duplikat. Tersisa {1, 2, 3} = 3 elemen.")

tanya_output(16, "Apa output?",
    'a = {1, 2, 3}\nb = {2, 3, 4}\nprint(a & b)',
    b"ezIsIDN9", "& adalah intersection (irisan). Elemen yang ada di KEDUA set.")

tanya_output(17, "Apa output?",
    'a = {1, 2, 3}\nb = {2, 3, 4}\nprint(a - b)',
    b"ezF9", "- adalah difference. Elemen yang ada di a tapi TIDAK di b.")

tanya(18, "Bisa tidak mengakses elemen set dengan index? Contoh: my_set[0]",
    {"a": "Bisa", "b": "Tidak bisa, TypeError", "c": "Return None", "d": "Return elemen pertama"},
    b"Yg==", "Set tidak terurut (unordered), jadi tidak mendukung indexing.")

# --- PERBANDINGAN ---
print(f"\n{'═' * 50}")
print("BAGIAN E: PERBANDINGAN")
print(f"{'═' * 50}")

tanya(19, "Data structure mana yang paling CEPAT untuk mengecek keanggotaan (membership test)?",
    {"a": "List", "b": "Tuple", "c": "Dictionary", "d": "Set"},
    b"ZA==", "Set dan dict menggunakan hash table, pencarian O(1). List/tuple O(n).")

tanya(20, "Mana yang BENAR tentang perbedaan list, tuple, dict, set?",
    {"a": "List immutable, tuple mutable",
     "b": "Set boleh duplikat, list tidak",
     "c": "Dict pakai key:value, set hanya value",
     "d": "Tuple bisa di-index, dict bisa di-index angka"},
    b"Yw==",
    "Dict = key:value pair, Set = hanya value unik. List & tuple mutable/immutable (bukan sebaliknya).")

# --- HASIL ---
print(f"\n{'═' * 50}")
print(f"  HASIL QUIZ 4: LIST, TUPLE, DICTIONARY, SET")
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
