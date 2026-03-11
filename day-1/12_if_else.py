"""
=== IF - ELIF - ELSE (Percabangan / Conditional) ===

Struktur:
    if kondisi:
        # kode jika kondisi True
    elif kondisi_lain:
        # kode jika kondisi_lain True
    else:
        # kode jika semua kondisi False
"""

# ============================================================
# 1. IF SEDERHANA
# ============================================================
print("=" * 60)
print("1. IF SEDERHANA")
print("=" * 60)

umur = 20
if umur >= 17:
    print(f"Umur {umur}: Boleh buat SIM")

suhu = 38.5
if suhu > 37.5:
    print(f"Suhu {suhu}°C: Anda demam, istirahat yang cukup!")

nilai = 85
if nilai >= 75:
    print(f"Nilai {nilai}: Selamat, Anda LULUS!")
print()


# ============================================================
# 2. IF - ELSE
# ============================================================
print("=" * 60)
print("2. IF - ELSE")
print("=" * 60)

angka = 7
if angka % 2 == 0:
    print(f"{angka} adalah bilangan GENAP")
else:
    print(f"{angka} adalah bilangan GANJIL")

saldo = 50000
harga = 75000
if saldo >= harga:
    print(f"Saldo Rp{saldo:,} cukup untuk beli barang Rp{harga:,}")
else:
    kurang = harga - saldo
    print(f"Saldo Rp{saldo:,} tidak cukup, kurang Rp{kurang:,}")

password = "abc123"
if len(password) >= 8:
    print("Password cukup kuat")
else:
    print(f"Password terlalu pendek ({len(password)} karakter, minimal 8)")
print()


# ============================================================
# 3. IF - ELIF - ELSE
# ============================================================
print("=" * 60)
print("3. IF - ELIF - ELSE")
print("=" * 60)

# --- Sistem Grading ---
nilai = 82
print(f"Nilai: {nilai}")
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"
print(f"Grade: {grade}")
print()

# --- Kategori Umur ---
umur = 25
print(f"Umur: {umur}")
if umur < 5:
    kategori = "Balita"
elif umur < 12:
    kategori = "Anak-anak"
elif umur < 18:
    kategori = "Remaja"
elif umur < 60:
    kategori = "Dewasa"
else:
    kategori = "Lansia"
print(f"Kategori: {kategori}")
print()

# --- BMI Calculator ---
berat = 70    # kg
tinggi = 1.75  # meter
bmi = berat / (tinggi ** 2)

print(f"Berat: {berat}kg, Tinggi: {tinggi}m")
print(f"BMI: {bmi:.1f}")
if bmi < 18.5:
    print("Status: Kurus")
elif bmi < 25:
    print("Status: Normal")
elif bmi < 30:
    print("Status: Gemuk")
else:
    print("Status: Obesitas")
print()


# ============================================================
# 4. NESTED IF (IF BERSARANG)
# ============================================================
print("=" * 60)
print("4. NESTED IF (IF BERSARANG)")
print("=" * 60)

# --- Login System ---
username = "admin"
password = "rahasia123"
is_active = True

input_user = "admin"
input_pass = "rahasia123"

print(f"Input: user='{input_user}', pass='{input_pass}'")
if input_user == username:
    if input_pass == password:
        if is_active:
            print("Login berhasil! Selamat datang, admin.")
        else:
            print("Akun Anda dinonaktifkan. Hubungi admin.")
    else:
        print("Password salah!")
else:
    print("Username tidak ditemukan!")
print()

# --- Tiket Bioskop ---
umur = 15
hari = "Sabtu"
print(f"Umur: {umur}, Hari: {hari}")
if umur >= 13:
    if hari in ["Sabtu", "Minggu"]:
        harga = 50000
    else:
        harga = 35000
    print(f"Harga tiket: Rp{harga:,}")
else:
    print("Maaf, film ini untuk usia 13+")
print()


# ============================================================
# 5. KONDISI DENGAN OPERATOR LOGIKA
# ============================================================
print("=" * 60)
print("5. KONDISI DENGAN OPERATOR LOGIKA (and, or, not)")
print("=" * 60)

# and - semua kondisi harus True
umur = 25
punya_sim = True
print(f"Umur: {umur}, Punya SIM: {punya_sim}")
if umur >= 17 and punya_sim:
    print("Boleh mengemudi")
else:
    print("Tidak boleh mengemudi")

# or - salah satu kondisi True sudah cukup
hari = "Minggu"
libur_nasional = False
print(f"\nHari: {hari}, Libur Nasional: {libur_nasional}")
if hari == "Minggu" or libur_nasional:
    print("Hari ini libur!")
else:
    print("Hari ini hari kerja")

# not - membalik kondisi
hujan = False
print(f"\nHujan: {hujan}")
if not hujan:
    print("Cuaca cerah, ayo jalan-jalan!")
else:
    print("Bawa payung!")

# Kombinasi
suhu = 28
cerah = True
angin_kencang = False
print(f"\nSuhu: {suhu}°C, Cerah: {cerah}, Angin kencang: {angin_kencang}")
if cerah and suhu > 25 and not angin_kencang:
    print("Cuaca sempurna untuk piknik!")
print()


# ============================================================
# 6. KONDISI DENGAN 'in' DAN 'is'
# ============================================================
print("=" * 60)
print("6. KONDISI DENGAN 'in' DAN 'is'")
print("=" * 60)

# in - cek keanggotaan
buah_tersedia = ["apel", "jeruk", "mangga", "pisang"]
pesanan = "mangga"
print(f"Buah tersedia: {buah_tersedia}")
if pesanan in buah_tersedia:
    print(f"'{pesanan}' tersedia!")
else:
    print(f"'{pesanan}' tidak tersedia")

# is None - cek None
data = None
print(f"\ndata = {data}")
if data is None:
    print("Data belum diisi")
else:
    print(f"Data: {data}")
print()


# ============================================================
# 7. USE CASES
# ============================================================
print("=" * 60)
print("7. USE CASES")
print("=" * 60)

# --- USE CASE 1: Kalkulator Sederhana ---
print("\n--- USE CASE 1: Kalkulator Sederhana ---")
a, b, operasi = 15, 4, "/"
print(f"{a} {operasi} {b} = ", end="")
if operasi == "+":
    print(a + b)
elif operasi == "-":
    print(a - b)
elif operasi == "*":
    print(a * b)
elif operasi == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error: Tidak bisa bagi dengan 0!")
elif operasi == "**":
    print(a ** b)
else:
    print(f"Operasi '{operasi}' tidak dikenal")

# --- USE CASE 2: Tarif Listrik ---
print("\n--- USE CASE 2: Tarif Listrik ---")
kwh = 350
print(f"Pemakaian: {kwh} kWh")
if kwh <= 100:
    tagihan = kwh * 500
elif kwh <= 200:
    tagihan = (100 * 500) + ((kwh - 100) * 750)
elif kwh <= 500:
    tagihan = (100 * 500) + (100 * 750) + ((kwh - 200) * 1000)
else:
    tagihan = (100 * 500) + (100 * 750) + (300 * 1000) + ((kwh - 500) * 1500)
print(f"Tagihan: Rp{tagihan:,}")

# --- USE CASE 3: Validasi Input ---
print("\n--- USE CASE 3: Validasi Input ---")
email = "user@example.com"
print(f"Email: '{email}'")
if not email:
    print("Error: Email tidak boleh kosong")
elif "@" not in email:
    print("Error: Email harus mengandung @")
elif "." not in email.split("@")[1]:
    print("Error: Domain email tidak valid")
elif len(email) < 5:
    print("Error: Email terlalu pendek")
else:
    print("Email valid!")

# --- USE CASE 4: Diskon Belanja ---
print("\n--- USE CASE 4: Diskon Belanja ---")
total_belanja = 350000
is_member = True
print(f"Total: Rp{total_belanja:,}, Member: {is_member}")

if is_member:
    if total_belanja >= 500000:
        diskon = 0.20
    elif total_belanja >= 200000:
        diskon = 0.10
    else:
        diskon = 0.05
else:
    if total_belanja >= 500000:
        diskon = 0.10
    elif total_belanja >= 300000:
        diskon = 0.05
    else:
        diskon = 0

potongan = int(total_belanja * diskon)
bayar = total_belanja - potongan
print(f"Diskon: {int(diskon * 100)}% = Rp{potongan:,}")
print(f"Bayar: Rp{bayar:,}")

# --- USE CASE 5: Tahun Kabisat ---
print("\n--- USE CASE 5: Tahun Kabisat ---")
tahun = 2024
print(f"Tahun: {tahun}")
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat")
else:
    print(f"{tahun} bukan tahun kabisat")

# --- USE CASE 6: FizzBuzz ---
print("\n--- USE CASE 6: FizzBuzz (1-20) ---")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

print()
print("=" * 60)
print("Selesai! If-Else sudah dicontohkan.")
