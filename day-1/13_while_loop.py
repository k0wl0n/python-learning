"""
=== WHILE LOOP ===

Struktur:
    while kondisi:
        # kode dijalankan selama kondisi True

Keyword penting:
    break    - keluar dari loop
    continue - lompat ke iterasi berikutnya
    else     - dijalankan jika loop selesai tanpa break
"""

# ============================================================
# 1. WHILE DASAR
# ============================================================
print("=" * 60)
print("1. WHILE DASAR")
print("=" * 60)

# Hitung mundur
print("Hitung mundur:")
angka = 5
while angka > 0:
    print(f"  {angka}...")
    angka -= 1
print("  GO!")
print()

# Penjumlahan
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(f"Jumlah 1 + 2 + ... + 10 = {total}")

# Cetak angka genap
print("\nAngka genap 1-20:")
n = 1
while n <= 20:
    if n % 2 == 0:
        print(f"  {n}", end="")
    n += 1
print()
print()


# ============================================================
# 2. WHILE DENGAN BREAK
# ============================================================
print("=" * 60)
print("2. WHILE DENGAN BREAK")
print("=" * 60)

# Cari angka dalam list
angka_list = [3, 7, 12, 5, 9, 18, 4, 15]
target = 18
i = 0
print(f"Cari {target} di {angka_list}")
while i < len(angka_list):
    if angka_list[i] == target:
        print(f"  Ditemukan di index {i}!")
        break
    i += 1
else:
    print(f"  {target} tidak ditemukan")
print()

# Simulasi password (tanpa input, pakai list)
percobaan_passwords = ["salah1", "salah2", "rahasia123"]
password_benar = "rahasia123"
max_percobaan = 5
percobaan = 0

print("Simulasi login:")
idx = 0
while percobaan < max_percobaan:
    if idx < len(percobaan_passwords):
        pw = percobaan_passwords[idx]
        idx += 1
    else:
        pw = "menyerah"

    percobaan += 1
    print(f"  Percobaan {percobaan}: '{pw}'", end="")

    if pw == password_benar:
        print(" -> Login berhasil!")
        break
    else:
        print(" -> Salah!")
else:
    print("  Akun terkunci! Terlalu banyak percobaan.")
print()


# ============================================================
# 3. WHILE DENGAN CONTINUE
# ============================================================
print("=" * 60)
print("3. WHILE DENGAN CONTINUE")
print("=" * 60)

# Skip angka kelipatan 3
print("Angka 1-15 (skip kelipatan 3):")
n = 0
while n < 15:
    n += 1
    if n % 3 == 0:
        continue
    print(f"  {n}", end="")
print()
print()

# Proses data, skip yang invalid
data = [10, -5, 20, 0, 15, -3, 25, -1, 30]
total = 0
count = 0
i = 0
print(f"Data: {data}")
print("Proses hanya bilangan positif:")
while i < len(data):
    if data[i] <= 0:
        print(f"  Skip: {data[i]}")
        i += 1
        continue
    total += data[i]
    count += 1
    print(f"  Proses: {data[i]}")
    i += 1
print(f"Total: {total}, Count: {count}, Rata-rata: {total / count:.1f}")
print()


# ============================================================
# 4. WHILE DENGAN ELSE
# ============================================================
print("=" * 60)
print("4. WHILE DENGAN ELSE")
print("=" * 60)

# else dijalankan jika loop selesai TANPA break
print("Contoh 1 - tanpa break (else dijalankan):")
n = 1
while n <= 5:
    print(f"  {n}", end="")
    n += 1
else:
    print("\n  -> Loop selesai normal (else dijalankan)")

print("\nContoh 2 - dengan break (else TIDAK dijalankan):")
n = 1
while n <= 5:
    if n == 3:
        print(f"\n  -> Break di n={n} (else tidak dijalankan)")
        break
    print(f"  {n}", end="")
    n += 1
else:
    print("  -> Loop selesai normal")
print()


# ============================================================
# 5. NESTED WHILE (WHILE BERSARANG)
# ============================================================
print("=" * 60)
print("5. NESTED WHILE (WHILE BERSARANG)")
print("=" * 60)

# Tabel perkalian
print("Tabel Perkalian 1-5:")
print(f"    {'':>3}", end="")
for j in range(1, 6):
    print(f"{j:>4}", end="")
print()
print("    " + "-" * 20)

i = 1
while i <= 5:
    print(f"    {i:>2} |", end="")
    j = 1
    while j <= 5:
        print(f"{i * j:>4}", end="")
        j += 1
    print()
    i += 1
print()

# Pola segitiga
print("Pola Bintang:")
baris = 1
while baris <= 5:
    print("    " + "* " * baris)
    baris += 1
print()


# ============================================================
# 6. INFINITE LOOP (LOOP TAK TERBATAS)
# ============================================================
print("=" * 60)
print("6. INFINITE LOOP (dengan break untuk keluar)")
print("=" * 60)

# Simulasi menu
pilihan_user = [2, 1, 3, 4]
idx = 0

print("=== MENU RESTORAN ===")
while True:
    print("  1. Nasi Goreng   - Rp25.000")
    print("  2. Mie Ayam      - Rp20.000")
    print("  3. Bakso         - Rp22.000")
    print("  4. Keluar")

    if idx < len(pilihan_user):
        pilih = pilihan_user[idx]
        idx += 1
    else:
        pilih = 4

    print(f"  Pilihan: {pilih}")

    if pilih == 1:
        print("  -> Nasi Goreng dipesan!\n")
    elif pilih == 2:
        print("  -> Mie Ayam dipesan!\n")
    elif pilih == 3:
        print("  -> Bakso dipesan!\n")
    elif pilih == 4:
        print("  -> Terima kasih! Sampai jumpa.\n")
        break
    else:
        print("  -> Pilihan tidak valid!\n")
print()


# ============================================================
# 7. USE CASES
# ============================================================
print("=" * 60)
print("7. USE CASES")
print("=" * 60)

# --- USE CASE 1: ATM Saldo ---
print("\n--- USE CASE 1: Simulasi ATM ---")
saldo = 1000000
transaksi = [("tarik", 300000), ("setor", 500000), ("tarik", 800000), ("tarik", 200000), ("tarik", 500000)]

idx = 0
while idx < len(transaksi):
    jenis, jumlah = transaksi[idx]
    print(f"  Saldo: Rp{saldo:>12,} | {jenis.upper()} Rp{jumlah:,}", end="")

    if jenis == "tarik":
        if saldo >= jumlah:
            saldo -= jumlah
            print(f" -> Berhasil")
        else:
            print(f" -> GAGAL (saldo tidak cukup)")
    elif jenis == "setor":
        saldo += jumlah
        print(f" -> Berhasil")

    idx += 1

print(f"  Saldo akhir: Rp{saldo:,}")

# --- USE CASE 2: Fibonacci ---
print("\n--- USE CASE 2: Fibonacci ---")
n = 15
a, b = 0, 1
fib = []
while a <= n:
    fib.append(a)
    a, b = b, a + b
print(f"Fibonacci sampai {n}: {fib}")

# --- USE CASE 3: Tebak Angka ---
print("\n--- USE CASE 3: Simulasi Tebak Angka ---")
import random
random.seed(42)
jawaban = random.randint(1, 10)
tebakan_list = [3, 7, 5, jawaban]
percobaan = 0

idx = 0
while idx < len(tebakan_list):
    tebak = tebakan_list[idx]
    percobaan += 1
    print(f"  Tebakan {percobaan}: {tebak}", end="")

    if tebak == jawaban:
        print(f" -> BENAR! Jawabannya {jawaban}. Percobaan: {percobaan}x")
        break
    elif tebak < jawaban:
        print(" -> Terlalu kecil!")
    else:
        print(" -> Terlalu besar!")
    idx += 1

# --- USE CASE 4: Collatz Conjecture ---
print("\n--- USE CASE 4: Collatz Conjecture ---")
n = 27
print(f"Mulai dari n = {n}")
steps = 0
sequence = [n]
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    sequence.append(n)
    steps += 1
print(f"Langkah: {steps}")
print(f"Sequence: {sequence[:10]}... (total {len(sequence)} angka)")
print(f"Nilai max: {max(sequence)}")

# --- USE CASE 5: Digit Sum ---
print("\n--- USE CASE 5: Digit Sum ---")
angka = 987654
print(f"Angka: {angka}")
total = 0
temp = angka
while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10
print(f"Jumlah digit: {total}")

print()
print("=" * 60)
print("Selesai! While loop sudah dicontohkan.")
