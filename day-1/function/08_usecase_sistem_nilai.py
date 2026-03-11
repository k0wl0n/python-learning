"""
=== USE CASE: SISTEM NILAI AKADEMIK ===

Contoh nyata penggunaan function untuk sistem penilaian mahasiswa.
Mendemonstrasikan:
    - Modular function design
    - Cross function calls
    - Data processing dengan function
    - Report generation
"""


# ============================================================
# DATA
# ============================================================

DATA_MAHASISWA = [
    {"nim": "2024001", "nama": "Alice Wijaya", "jurusan": "TI",
     "nilai": {"matematika": 88, "fisika": 75, "pemrograman": 95, "basis_data": 82, "jaringan": 90}},
    {"nim": "2024002", "nama": "Bob Santoso", "jurusan": "TI",
     "nilai": {"matematika": 72, "fisika": 68, "pemrograman": 80, "basis_data": 75, "jaringan": 70}},
    {"nim": "2024003", "nama": "Charlie Pratama", "jurusan": "SI",
     "nilai": {"matematika": 95, "fisika": 90, "pemrograman": 98, "basis_data": 92, "jaringan": 88}},
    {"nim": "2024004", "nama": "Diana Putri", "jurusan": "TI",
     "nilai": {"matematika": 60, "fisika": 55, "pemrograman": 65, "basis_data": 58, "jaringan": 62}},
    {"nim": "2024005", "nama": "Edward Lim", "jurusan": "SI",
     "nilai": {"matematika": 78, "fisika": 82, "pemrograman": 85, "basis_data": 80, "jaringan": 76}},
    {"nim": "2024006", "nama": "Fiona Anggraini", "jurusan": "TI",
     "nilai": {"matematika": 45, "fisika": 50, "pemrograman": 55, "basis_data": 48, "jaringan": 42}},
]


# ============================================================
# FUNCTION: KONVERSI & KALKULASI
# ============================================================

def nilai_ke_grade(nilai):
    """Konversi nilai angka (0-100) ke grade huruf."""
    if nilai >= 85:
        return "A"
    if nilai >= 75:
        return "B"
    if nilai >= 65:
        return "C"
    if nilai >= 55:
        return "D"
    return "E"


def grade_ke_bobot(grade):
    """Konversi grade ke bobot untuk menghitung IPK."""
    return {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}.get(grade, 0.0)


def hitung_rata_rata(nilai_dict):
    """Hitung rata-rata dari dictionary nilai."""
    if not nilai_dict:
        return 0
    return sum(nilai_dict.values()) / len(nilai_dict)


def hitung_ipk(nilai_dict):
    """Hitung IPK dari dictionary nilai."""
    if not nilai_dict:
        return 0
    total_bobot = 0
    for nilai in nilai_dict.values():
        grade = nilai_ke_grade(nilai)
        total_bobot += grade_ke_bobot(grade)
    return total_bobot / len(nilai_dict)


def status_kelulusan(ipk, nilai_dict):
    """Tentukan status kelulusan."""
    if ipk < 2.0:
        return "TIDAK LULUS"
    nilai_list = list(nilai_dict.values())
    if any(n < 55 for n in nilai_list):
        return "LULUS BERSYARAT"
    return "LULUS"


def predikat(ipk):
    """Tentukan predikat kelulusan."""
    if ipk >= 3.5:
        return "Cum Laude"
    if ipk >= 3.0:
        return "Sangat Memuaskan"
    if ipk >= 2.5:
        return "Memuaskan"
    return "Cukup"


# ============================================================
# FUNCTION: PENCARIAN & FILTER
# ============================================================

def cari_mahasiswa(nim):
    """Cari mahasiswa berdasarkan NIM."""
    for mhs in DATA_MAHASISWA:
        if mhs["nim"] == nim:
            return mhs
    return None


def filter_by_jurusan(jurusan):
    """Filter mahasiswa berdasarkan jurusan."""
    return [mhs for mhs in DATA_MAHASISWA if mhs["jurusan"] == jurusan]


def filter_by_ipk(min_ipk):
    """Filter mahasiswa dengan IPK minimal tertentu."""
    return [mhs for mhs in DATA_MAHASISWA if hitung_ipk(mhs["nilai"]) >= min_ipk]


def get_top_students(n=3):
    """Ambil N mahasiswa dengan IPK tertinggi."""
    sorted_mhs = sorted(DATA_MAHASISWA, key=lambda m: hitung_ipk(m["nilai"]), reverse=True)
    return sorted_mhs[:n]


def get_matakuliah_terbaik(mhs):
    """Cari mata kuliah dengan nilai tertinggi."""
    return max(mhs["nilai"].items(), key=lambda x: x[1])


def get_matakuliah_terlemah(mhs):
    """Cari mata kuliah dengan nilai terendah."""
    return min(mhs["nilai"].items(), key=lambda x: x[1])


# ============================================================
# FUNCTION: DISPLAY / REPORT
# ============================================================

def cetak_header(judul):
    print(f"\n{'=' * 70}")
    print(f"  {judul}")
    print(f"{'=' * 70}")


def cetak_profil(mhs):
    """Cetak profil lengkap satu mahasiswa."""
    ipk = hitung_ipk(mhs["nilai"])
    rata2 = hitung_rata_rata(mhs["nilai"])
    status = status_kelulusan(ipk, mhs["nilai"])
    terbaik_mk, terbaik_val = get_matakuliah_terbaik(mhs)
    terlemah_mk, terlemah_val = get_matakuliah_terlemah(mhs)

    print(f"  NIM:      {mhs['nim']}")
    print(f"  Nama:     {mhs['nama']}")
    print(f"  Jurusan:  {mhs['jurusan']}")
    print(f"  ────────────────────────────────")

    for mk, nilai in mhs["nilai"].items():
        grade = nilai_ke_grade(nilai)
        bar = "█" * (nilai // 10)
        print(f"  {mk:<15} {nilai:>3} ({grade})  {bar}")

    print(f"  ────────────────────────────────")
    print(f"  Rata-rata:  {rata2:.1f}")
    print(f"  IPK:        {ipk:.2f}")
    print(f"  Status:     {status}")
    print(f"  Predikat:   {predikat(ipk)}")
    print(f"  Terbaik:    {terbaik_mk} ({terbaik_val})")
    print(f"  Terlemah:   {terlemah_mk} ({terlemah_val})")


def cetak_tabel_semua():
    """Cetak tabel ringkasan semua mahasiswa."""
    header = f"  {'NIM':<10} {'Nama':<20} {'Jur':<4} {'Avg':>5} {'IPK':>5} {'Status':<15} {'Predikat':<18}"
    print(header)
    print("  " + "─" * 80)

    for mhs in DATA_MAHASISWA:
        ipk = hitung_ipk(mhs["nilai"])
        rata2 = hitung_rata_rata(mhs["nilai"])
        sts = status_kelulusan(ipk, mhs["nilai"])
        pred = predikat(ipk)
        print(f"  {mhs['nim']:<10} {mhs['nama']:<20} {mhs['jurusan']:<4} {rata2:>5.1f} {ipk:>5.2f} {sts:<15} {pred:<18}")


def cetak_statistik_kelas():
    """Cetak statistik seluruh kelas."""
    semua_ipk = [hitung_ipk(mhs["nilai"]) for mhs in DATA_MAHASISWA]
    semua_rata2 = [hitung_rata_rata(mhs["nilai"]) for mhs in DATA_MAHASISWA]

    print(f"  Jumlah mahasiswa:  {len(DATA_MAHASISWA)}")
    print(f"  IPK tertinggi:     {max(semua_ipk):.2f}")
    print(f"  IPK terendah:      {min(semua_ipk):.2f}")
    print(f"  IPK rata-rata:     {sum(semua_ipk)/len(semua_ipk):.2f}")
    print(f"  Nilai rata-rata:   {sum(semua_rata2)/len(semua_rata2):.1f}")

    lulus = sum(1 for ipk in semua_ipk if ipk >= 2.0)
    print(f"  Tingkat kelulusan: {lulus}/{len(DATA_MAHASISWA)} ({lulus/len(DATA_MAHASISWA)*100:.0f}%)")


def cetak_ranking():
    """Cetak ranking mahasiswa berdasarkan IPK."""
    sorted_mhs = sorted(DATA_MAHASISWA, key=lambda m: hitung_ipk(m["nilai"]), reverse=True)
    for rank, mhs in enumerate(sorted_mhs, 1):
        ipk = hitung_ipk(mhs["nilai"])
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
        print(f"  {medal} #{rank} {mhs['nama']:<20} IPK: {ipk:.2f} ({predikat(ipk)})")


# ============================================================
# DEMO
# ============================================================

cetak_header("TABEL NILAI SEMUA MAHASISWA")
cetak_tabel_semua()

cetak_header("PROFIL DETAIL - MAHASISWA TERBAIK")
top = get_top_students(1)[0]
cetak_profil(top)

cetak_header("RANKING MAHASISWA")
cetak_ranking()

cetak_header("STATISTIK KELAS")
cetak_statistik_kelas()

cetak_header("FILTER: JURUSAN TI")
mhs_ti = filter_by_jurusan("TI")
for mhs in mhs_ti:
    ipk = hitung_ipk(mhs["nilai"])
    print(f"  {mhs['nama']:<20} IPK: {ipk:.2f}")

cetak_header("FILTER: IPK >= 3.0")
mhs_bagus = filter_by_ipk(3.0)
for mhs in mhs_bagus:
    ipk = hitung_ipk(mhs["nilai"])
    print(f"  {mhs['nama']:<20} IPK: {ipk:.2f}")

cetak_header("CARI MAHASISWA: NIM 2024003")
found = cari_mahasiswa("2024003")
if found:
    cetak_profil(found)
else:
    print("  Tidak ditemukan")

print()
print("=" * 70)
print("Selesai! Use case sistem nilai sudah dicontohkan.")
