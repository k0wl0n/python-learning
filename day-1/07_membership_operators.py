"""
=== MEMBERSHIP OPERATORS (Operator Keanggotaan) ===

Operator    Deskripsi
in          Mengembalikan True jika nilai ditemukan dalam sequence
not in      Mengembalikan True jika nilai TIDAK ditemukan dalam sequence

Bisa digunakan pada: String, List, Tuple, Set, Dictionary
"""

print("=== MEMBERSHIP OPERATORS ===")
print()

# --- Pada List ---
print("--- Pada List ---")
buah = ["apel", "jeruk", "mangga", "pisang"]
print(f"buah = {buah}")
print(f"'apel' in buah      -> {'apel' in buah}")          # True
print(f"'durian' in buah    -> {'durian' in buah}")         # False
print(f"'durian' not in buah -> {'durian' not in buah}")    # True
print()

# --- Pada String ---
print("--- Pada String ---")
kalimat = "Belajar Python itu menyenangkan"
print(f"kalimat = '{kalimat}'")
print(f"'Python' in kalimat      -> {'Python' in kalimat}")         # True
print(f"'Java' in kalimat        -> {'Java' in kalimat}")           # False
print(f"'Java' not in kalimat    -> {'Java' not in kalimat}")       # True
print()

# --- Pada Tuple ---
print("--- Pada Tuple ---")
angka = (1, 2, 3, 4, 5)
print(f"angka = {angka}")
print(f"3 in angka     -> {3 in angka}")          # True
print(f"10 in angka    -> {10 in angka}")          # False
print(f"10 not in angka -> {10 not in angka}")     # True
print()

# --- Pada Set ---
print("--- Pada Set ---")
warna = {"merah", "hijau", "biru"}
print(f"warna = {warna}")
print(f"'merah' in warna    -> {'merah' in warna}")        # True
print(f"'kuning' in warna   -> {'kuning' in warna}")       # False
print()

# --- Pada Dictionary (mengecek KEY, bukan value) ---
print("--- Pada Dictionary ---")
mahasiswa = {"nama": "Budi", "umur": 21, "jurusan": "TI"}
print(f"mahasiswa = {mahasiswa}")
print(f"'nama' in mahasiswa    -> {'nama' in mahasiswa}")        # True (key ada)
print(f"'Budi' in mahasiswa    -> {'Budi' in mahasiswa}")        # False (itu value, bukan key)
print(f"'alamat' not in mahasiswa -> {'alamat' not in mahasiswa}")  # True
print()

# --- Contoh penggunaan ---
print("=== CONTOH PENGGUNAAN ===")

menu = ["nasi goreng", "mie ayam", "bakso", "soto"]
pesanan = "bakso"

if pesanan in menu:
    print(f"'{pesanan}' tersedia di menu!")
else:
    print(f"Maaf, '{pesanan}' tidak tersedia.")

email = "user@example.com"
if "@" in email:
    print(f"'{email}' adalah format email yang valid (mengandung @)")
else:
    print(f"'{email}' bukan format email yang valid")

kata_terlarang = ["spam", "iklan", "promo"]
pesan = "Ini adalah pesan biasa"
ada_kata_terlarang = any(kata in pesan.lower() for kata in kata_terlarang)
print(f"Pesan: '{pesan}'")
print(f"Mengandung kata terlarang: {ada_kata_terlarang}")
