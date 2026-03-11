"""
╔══════════════════════════════════════════════════╗
║   QUIZ 5: IF-ELSE, WHILE, FOR, TERNARY          ║
║   Jalankan: python3 quiz_05_if_else_loop_ternary.py ║
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
print("║   QUIZ 5: IF-ELSE, WHILE, FOR, TERNARY           ║")
print("║   20 soal                                         ║")
print("╚══════════════════════════════════════════════════╝")

# --- IF ELSE ---
print(f"\n{'═' * 50}")
print("BAGIAN A: IF - ELIF - ELSE")
print(f"{'═' * 50}")

tanya_output(1, "Apa output?",
    'x = 15\nif x > 20:\n    print("A")\nelif x > 10:\n    print("B")\nelse:\n    print("C")',
    b"Qg==", "x=15: 15 > 20? Tidak. 15 > 10? Ya -> print 'B'.")

tanya_output(2, "Apa output?",
    'x = 5\nif x > 0:\n    if x > 10:\n        print("besar")\n    else:\n        print("kecil")',
    b"a2VjaWw=", "x=5: 5 > 0? Ya. 5 > 10? Tidak -> else -> 'kecil'.")

tanya_output(3, "Apa output?",
    'x = 10\ny = 20\nif x > 5 and y < 15:\n    print("A")\nelse:\n    print("B")',
    b"Qg==", "x > 5 = True, tapi y < 15 = False. True and False = False -> else -> 'B'.")

tanya_output(4, "Apa output?",
    'x = 0\nif x:\n    print("truthy")\nelse:\n    print("falsy")',
    b"ZmFsc3k=", "0 adalah falsy di Python. if 0: = if False:.")

tanya(5, "Apa output: print('A') if True else print('B')?",
    {"a": "A", "b": "B", "c": "True", "d": "Error"},
    b"YQ==", "Kondisi True, jadi ekspresi pertama dijalankan -> print('A').")

# --- FOR LOOP ---
print(f"\n{'═' * 50}")
print("BAGIAN B: FOR LOOP")
print(f"{'═' * 50}")

tanya_output(6, "Apa output?",
    'total = 0\nfor i in range(5):\n    total += i\nprint(total)',
    b"MTA=", "range(5) = 0,1,2,3,4. Total = 0+1+2+3+4 = 10.")

tanya_output(7, "Apa output?",
    'for i in range(3):\n    if i == 1:\n        continue\n    print(i, end="")',
    b"MDI=", "i=0: print 0. i=1: continue (skip). i=2: print 2. Output: 02.")

tanya_output(8, "Apa output?",
    'for i in range(5):\n    if i == 3:\n        break\n    print(i, end="")',
    b"MDEy", "i=0,1,2: print. i=3: break (keluar loop). Output: 012.")

tanya_output(9, "Apa output?",
    'print([x**2 for x in range(4)])',
    b"WzAsIDEsIDQsIDld", "List comprehension: [0^2, 1^2, 2^2, 3^2] = [0, 1, 4, 9].")

tanya(10, "Apa fungsi enumerate() pada for loop?",
    {"a": "Mengurutkan data", "b": "Memberikan index + value",
     "c": "Menghitung jumlah iterasi", "d": "Membalik urutan"},
    b"Yg==", "enumerate() mengembalikan (index, value) untuk setiap iterasi.")

# --- WHILE LOOP ---
print(f"\n{'═' * 50}")
print("BAGIAN C: WHILE LOOP")
print(f"{'═' * 50}")

tanya_output(11, "Apa output?",
    'x = 10\nwhile x > 0:\n    x -= 3\nprint(x)',
    b"LTI=", "10->7->4->1->(-2). Saat x=-2, kondisi x > 0 False, keluar loop.")

tanya_output(12, "Apa output?",
    'i = 0\nwhile i < 5:\n    i += 1\n    if i == 3:\n        break\nprint(i)',
    b"Mw==", "i: 1, 2, 3 (break). Saat i=3, keluar loop. print(i) = 3.")

tanya(13, "Kapan blok 'else' pada while loop TIDAK dijalankan?",
    {"a": "Selalu dijalankan", "b": "Jika loop selesai normal",
     "c": "Jika loop keluar dengan break", "d": "Jika ada continue"},
    b"Yw==", "while...else: blok else TIDAK dijalankan jika loop keluar dengan break.")

tanya_output(14, "Berapa kali loop ini berjalan?",
    'count = 0\nwhile count < 3:\n    count += 1\nprint(count)',
    b"Mw==", "Loop berjalan 3 kali (count: 0->1, 1->2, 2->3). print(count) = 3.")

tanya(15, "Apa yang terjadi jika while True: tanpa break?",
    {"a": "Error", "b": "Loop berjalan sekali", "c": "Infinite loop", "d": "Return None"},
    b"Yw==", "while True: tanpa break = infinite loop (tidak pernah berhenti).")

# --- TERNARY ---
print(f"\n{'═' * 50}")
print("BAGIAN D: TERNARY OPERATOR")
print(f"{'═' * 50}")

tanya_output(16, "Apa output?",
    'x = 7\nhasil = "genap" if x % 2 == 0 else "ganjil"\nprint(hasil)',
    b"Z2Fuamls", "7 % 2 = 1 (bukan 0), jadi kondisi False -> 'ganjil'.")

tanya_output(17, "Apa output?",
    'umur = 20\nstatus = "dewasa" if umur >= 17 else "anak"\nprint(status)',
    b"ZGV3YXNh", "20 >= 17 = True -> 'dewasa'.")

tanya_output(18, "Apa output?",
    'data = [x if x > 0 else 0 for x in [-3, 5, -1, 8]]\nprint(data)',
    b"WzAsIDUsIDAsIDhd",
    "Ternary dalam list comprehension: negatif jadi 0, positif tetap.")

tanya(19, "Mana syntax ternary yang BENAR?",
    {"a": "kondisi ? nilai_true : nilai_false",
     "b": "nilai_true if kondisi else nilai_false",
     "c": "if kondisi then nilai_true else nilai_false",
     "d": "kondisi and nilai_true or nilai_false"},
    b"Yg==", "Python ternary: nilai_true if kondisi else nilai_false.")

tanya_output(20, "Apa output?",
    'n = 85\ng = "A" if n >= 90 else "B" if n >= 80 else "C"\nprint(g)',
    b"Qg==", "85 >= 90? Tidak. 85 >= 80? Ya -> 'B'. Nested ternary.")

# --- HASIL ---
print(f"\n{'═' * 50}")
print(f"  HASIL QUIZ 5: IF-ELSE, LOOP, TERNARY")
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
