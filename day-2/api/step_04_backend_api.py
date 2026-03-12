"""
╔══════════════════════════════════════════════════════════════╗
║   STEP 4: BACKEND API NILAI MAHASISWA                        ║
║   Flask REST API + MySQL Database                            ║
╠══════════════════════════════════════════════════════════════╣
║   CARA MENJALANKAN:                                          ║
║     1. Jalankan MySQL: cd day-2 && docker compose up -d      ║
║     2. Install deps: pip install flask mysql-connector-python ║
║     3. Jalankan server: python3 step_04_backend_api.py       ║
║     4. Test API: python3 test_api.py  (di terminal lain)     ║
╠══════════════════════════════════════════════════════════════╣
║   KONSEP PYTHON YANG DIPAKAI:                                ║
║     ✅ Variables & tipe data                                 ║
║     ✅ Dictionary (setiap mahasiswa)                         ║
║     ✅ Tuple (GRADE_CONFIG, return values)                   ║
║     ✅ f-string (pesan error & response)                     ║
║     ✅ Type casting (int(), float())                         ║
║     ✅ Comparison & logical operators                        ║
║     ✅ if/elif/else (grade)                                  ║
║     ✅ Ternary operator (status lulus)                       ║
║     ✅ String methods (.lower(), .strip())                   ║
║     ✅ os.getenv() (environment variable)                    ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
from decimal import Decimal
from datetime import datetime

import mysql.connector
from mysql.connector import pooling, Error as MySQLError
from flask import Flask, request, jsonify

app = Flask(__name__)

# ============================================================
# KONFIGURASI GRADE - TUPLE (IMMUTABLE)
# ============================================================
# Pakai tuple karena konfigurasi ini TIDAK BOLEH diubah saat runtime.
GRADE_CONFIG = (
    (85, "A"),
    (70, "B"),
    (55, "C"),
    (40, "D"),
    (0,  "E"),
)

# ============================================================
# KONFIGURASI DATABASE
# ============================================================
# os.getenv() → baca dari environment variable, fallback ke default.
# Best practice: jangan hard-code credential di kode.
DB_CONFIG = {
    "host":     os.getenv("DB_HOST",     "127.0.0.1"),
    "port":     int(os.getenv("DB_PORT", "3306")),
    "user":     os.getenv("DB_USER",     "devuser"),
    "password": os.getenv("DB_PASSWORD", "devpassword"),
    "database": os.getenv("DB_NAME",     "nilai_mahasiswa"),
}

# Connection Pool: koneksi dibuat sekali, di-reuse → lebih efisien
# pool_size=5 → maksimal 5 koneksi bersamaan
_pool = None


def get_pool():
    """Lazy init: buat pool hanya saat pertama kali dibutuhkan."""
    global _pool
    if _pool is None:
        _pool = pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            **DB_CONFIG          # unpack dict sebagai keyword arguments
        )
    return _pool


def get_db():
    """Ambil koneksi dari pool. Selalu panggil conn.close() setelah selesai."""
    return get_pool().get_connection()


# ============================================================
# HELPER: KONVERSI ROW → DICT
# ============================================================

def row_to_dict(cursor, row) -> dict:
    """
    Konversi satu row MySQL (tuple) ke dictionary.
    - cursor.description → metadata kolom (nama, tipe, dll)
    - Decimal → float  agar JSON serializable
    - datetime → string ISO 8601
    """
    columns = [col[0] for col in cursor.description]   # list comprehension
    result  = {}
    for col, val in zip(columns, row):                 # zip: pasangkan nama+nilai
        if isinstance(val, Decimal):
            result[col] = float(val)                   # type casting
        elif isinstance(val, datetime):
            result[col] = val.isoformat()              # datetime → string
        else:
            result[col] = val
    return result


def rows_to_list(cursor, rows) -> list:
    """Konversi banyak rows ke list of dict."""
    return [row_to_dict(cursor, row) for row in rows]  # list comprehension


# ============================================================
# HELPER: RESPONSE & VALIDASI
# ============================================================

def response_ok(data=None, message="OK", status_code=200):
    """Helper membuat response sukses yang konsisten."""
    return jsonify({"success": True, "message": message, "data": data}), status_code


def response_err(message, status_code=400):
    """Helper membuat response error yang konsisten."""
    return jsonify({"success": False, "message": message, "data": None}), status_code


def validasi_nilai(label: str, nilai) -> str | None:
    """
    Validasi satu nilai: harus float dan 0-100.
    Return error string atau None jika valid.
    """
    try:
        nilai_float = float(nilai)             # type casting
    except (TypeError, ValueError):
        return f"{label} harus berupa angka"
    if not (0 <= nilai_float <= 100):          # comparison operator
        return f"{label} harus antara 0 dan 100"
    return None


# ============================================================
# REFERENSI LOGIKA BISNIS
# (Sekarang dihandle oleh MySQL GENERATED COLUMNS di init.sql,
#  tapi tetap disimpan di sini sebagai referensi & dokumentasi)
# ============================================================

def hitung_nilai_akhir(nilai_tugas: float, nilai_uts: float, nilai_uas: float) -> float:
    """Hitung nilai akhir: tugas*30% + uts*30% + uas*40%."""
    return round((nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4), 2)


def tentukan_grade(nilai_akhir: float) -> str:
    """Tentukan grade menggunakan GRADE_CONFIG (tuple)."""
    for batas, grade in GRADE_CONFIG:
        if nilai_akhir >= batas:
            return grade
    return "E"


def tentukan_status(grade: str) -> str:
    """Tentukan status lulus menggunakan ternary operator."""
    tidak_lulus = {"D", "E"}                   # set literal
    return "TIDAK LULUS" if grade in tidak_lulus else "LULUS"


# ============================================================
# ENDPOINT 0: Welcome
# GET /
# ============================================================

@app.route("/")
def welcome():
    """GET / → informasi API."""
    return response_ok(
        data={
            "nama_api": "API Nilai Mahasiswa",
            "versi":    "2.0.0",
            "database": f"MySQL @ {DB_CONFIG['host']}:{DB_CONFIG['port']}",
            "endpoints": [
                "GET    /mahasiswa",
                "GET    /mahasiswa?sort=nilai_akhir&order=desc",
                "GET    /mahasiswa?grade=A",
                "GET    /mahasiswa/<id>",
                "POST   /mahasiswa",
                "PUT    /mahasiswa/<id>",
                "DELETE /mahasiswa/<id>",
                "GET    /mahasiswa/statistik",
                "GET    /mahasiswa/search?nama=keyword",
            ]
        },
        message="Selamat datang di API Nilai Mahasiswa (MySQL)"
    )


# ============================================================
# ENDPOINT 1: GET SEMUA MAHASISWA
# GET /mahasiswa
# GET /mahasiswa?sort=nilai_akhir&order=desc
# GET /mahasiswa?grade=A
# ============================================================

@app.route("/mahasiswa", methods=["GET"])
def get_semua_mahasiswa():
    """
    GET /mahasiswa
    Mengambil semua data mahasiswa.
    Opsional: ?sort=nilai_akhir&order=desc&grade=A
    """
    sort_by      = request.args.get("sort",  None)
    order        = request.args.get("order", "asc")
    filter_grade = request.args.get("grade", None)

    # Whitelist kolom yang boleh di-sort → cegah SQL injection
    valid_sort = {"nilai_akhir", "nama", "nim", "id"}
    if sort_by and sort_by not in valid_sort:
        return response_err(f"sort harus salah satu dari: {', '.join(valid_sort)}")

    # Bangun query secara dinamis
    sql    = "SELECT * FROM mahasiswa"
    params = []

    if filter_grade:
        sql += " WHERE grade = %s"
        params.append(filter_grade.upper())    # string method

    if sort_by:
        # ORDER BY tidak bisa pakai %s → aman karena sudah divalidasi whitelist
        direction = "DESC" if order.lower() == "desc" else "ASC"
        sql += f" ORDER BY {sort_by} {direction}"

    conn   = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        rows  = cursor.fetchall()
        hasil = rows_to_list(cursor, rows)
    finally:
        cursor.close()
        conn.close()    # kembalikan koneksi ke pool

    return response_ok(
        data=hasil,
        message=f"{len(hasil)} mahasiswa ditemukan"
    )


# ============================================================
# ENDPOINT 2: GET STATISTIK
# GET /mahasiswa/statistik
# PENTING: Dideklarasikan SEBELUM /mahasiswa/<id>
# ============================================================

@app.route("/mahasiswa/statistik", methods=["GET"])
def get_statistik():
    """GET /mahasiswa/statistik → statistik keseluruhan."""
    conn   = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM mahasiswa")
        jumlah = cursor.fetchone()[0]

        if jumlah == 0:
            return response_ok(
                data={"jumlah_mahasiswa": 0},
                message="Belum ada data mahasiswa"
            )

        cursor.execute("SELECT * FROM mahasiswa")
        rows  = cursor.fetchall()
        semua = rows_to_list(cursor, rows)
    finally:
        cursor.close()
        conn.close()

    # Hitung statistik dengan Python (list comprehension + built-in)
    semua_nilai  = [m["nilai_akhir"] for m in semua]
    rata_rata    = round(sum(semua_nilai) / len(semua_nilai), 2)
    jumlah_lulus = sum(1 for m in semua if m["status"] == "LULUS")
    mhs_terbaik  = max(semua, key=lambda m: m["nilai_akhir"])
    mhs_terendah = min(semua, key=lambda m: m["nilai_akhir"])

    # Distribusi grade menggunakan dictionary + loop
    distribusi_grade = {}
    for mhs in semua:
        grade = mhs["grade"]
        distribusi_grade[grade] = distribusi_grade.get(grade, 0) + 1

    urutan_grade    = [g for _, g in GRADE_CONFIG]     # ["A","B","C","D","E"]
    distribusi_urut = {g: distribusi_grade.get(g, 0) for g in urutan_grade}

    return response_ok(data={
        "jumlah_mahasiswa":      jumlah,
        "rata_rata_nilai_akhir": rata_rata,
        "nilai_tertinggi":       max(semua_nilai),
        "nilai_terendah":        min(semua_nilai),
        "mahasiswa_terbaik":     f"{mhs_terbaik['nama']} ({mhs_terbaik['nilai_akhir']})",
        "mahasiswa_terendah":    f"{mhs_terendah['nama']} ({mhs_terendah['nilai_akhir']})",
        "jumlah_lulus":          jumlah_lulus,
        "jumlah_tidak_lulus":    jumlah - jumlah_lulus,
        "persen_lulus":          f"{round(jumlah_lulus / jumlah * 100, 1)}%",
        "distribusi_grade":      distribusi_urut,
    }, message="Statistik berhasil dihitung")


# ============================================================
# ENDPOINT 3: SEARCH MAHASISWA
# GET /mahasiswa/search?nama=keyword
# PENTING: Dideklarasikan SEBELUM /mahasiswa/<id>
# ============================================================

@app.route("/mahasiswa/search", methods=["GET"])
def search_mahasiswa():
    """GET /mahasiswa/search?nama=keyword → cari nama (partial, case insensitive)."""
    keyword = request.args.get("nama", "").strip()   # string method

    if not keyword:
        return response_err("Parameter 'nama' wajib diisi")

    conn   = get_db()
    cursor = conn.cursor()
    try:
        # LIKE dengan %s → parameterized query, aman dari SQL injection
        cursor.execute(
            "SELECT * FROM mahasiswa WHERE nama LIKE %s",
            (f"%{keyword}%",)    # tuple, % adalah wildcard LIKE
        )
        rows  = cursor.fetchall()
        hasil = rows_to_list(cursor, rows)
    finally:
        cursor.close()
        conn.close()

    return response_ok(
        data=hasil,
        message=f"{len(hasil)} mahasiswa ditemukan dengan keyword '{keyword}'"
    )


# ============================================================
# ENDPOINT 4: GET MAHASISWA BY ID
# GET /mahasiswa/<id>
# ============================================================

@app.route("/mahasiswa/<int:id>", methods=["GET"])
def get_mahasiswa_by_id(id):
    """
    GET /mahasiswa/<id>
    <int:id> → Flask otomatis konversi ke integer (type casting).
    """
    conn   = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM mahasiswa WHERE id = %s", (id,))
        row = cursor.fetchone()
        mhs = row_to_dict(cursor, row) if row else None
    finally:
        cursor.close()
        conn.close()

    if mhs is None:
        return response_err(f"Mahasiswa dengan ID {id} tidak ditemukan", 404)

    return response_ok(data=mhs, message="Mahasiswa ditemukan")


# ============================================================
# ENDPOINT 5: TAMBAH MAHASISWA
# POST /mahasiswa
# ============================================================

@app.route("/mahasiswa", methods=["POST"])
def tambah_mahasiswa():
    """
    POST /mahasiswa
    Request body (JSON):
    { "nama": "Alice", "nim": "2024007", "nilai_tugas": 85, "nilai_uts": 80, "nilai_uas": 90 }
    """
    body = request.get_json()
    if not body:
        return response_err("Request body harus berupa JSON")

    # Ambil field dari body menggunakan dictionary .get()
    nama        = body.get("nama", "")
    nim         = body.get("nim",  "")
    nilai_tugas = body.get("nilai_tugas")
    nilai_uts   = body.get("nilai_uts")
    nilai_uas   = body.get("nilai_uas")

    # Validasi field wajib: logical operator not + or
    if not nama or not nim:
        return response_err("Field 'nama' dan 'nim' wajib diisi")

    nama = nama.strip()   # string method
    nim  = nim.strip()

    if not nama or not nim:
        return response_err("Nama dan NIM tidak boleh hanya spasi")

    # Validasi nilai: loop tuple untuk cek semua field sekaligus
    for label, nilai in (("nilai_tugas", nilai_tugas),
                          ("nilai_uts",   nilai_uts),
                          ("nilai_uas",   nilai_uas)):
        if nilai is None:
            return response_err(f"Field '{label}' wajib diisi")
        err = validasi_nilai(label, nilai)
        if err:
            return response_err(err)

    conn   = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO mahasiswa (nama, nim, nilai_tugas, nilai_uts, nilai_uas) "
            "VALUES (%s, %s, %s, %s, %s)",
            (nama, nim, float(nilai_tugas), float(nilai_uts), float(nilai_uas))
        )
        conn.commit()
        new_id = cursor.lastrowid    # ID auto_increment yang baru dibuat

        # Ambil data lengkap termasuk GENERATED COLUMNS (nilai_akhir, grade, status)
        cursor.execute("SELECT * FROM mahasiswa WHERE id = %s", (new_id,))
        mahasiswa_baru = row_to_dict(cursor, cursor.fetchone())

    except MySQLError as e:
        conn.rollback()
        if e.errno == 1062:          # Duplicate entry → NIM sudah ada
            return response_err(f"NIM '{nim}' sudah terdaftar", 409)
        return response_err(f"Database error: {e.msg}", 500)
    finally:
        cursor.close()
        conn.close()

    return response_ok(
        data=mahasiswa_baru,
        message=f"Mahasiswa '{nama}' berhasil ditambahkan dengan grade {mahasiswa_baru['grade']}",
        status_code=201
    )


# ============================================================
# ENDPOINT 6: UPDATE MAHASISWA
# PUT /mahasiswa/<id>
# ============================================================

@app.route("/mahasiswa/<int:id>", methods=["PUT"])
def update_mahasiswa(id):
    """
    PUT /mahasiswa/<id>
    Partial update: semua field opsional.
    """
    body = request.get_json()
    if not body:
        return response_err("Request body harus berupa JSON")

    conn   = get_db()
    cursor = conn.cursor()
    try:
        # Cek ID ada dulu
        cursor.execute("SELECT id FROM mahasiswa WHERE id = %s", (id,))
        if not cursor.fetchone():
            return response_err(f"Mahasiswa ID {id} tidak ditemukan", 404)

        # Bangun SET clause secara dinamis (partial update)
        set_parts = []
        params    = []

        if "nama" in body:
            nama_baru = body["nama"].strip()
            if not nama_baru:
                return response_err("Nama tidak boleh kosong")
            set_parts.append("nama = %s")
            params.append(nama_baru)

        # Loop tuple untuk validasi & append field nilai
        for field in ("nilai_tugas", "nilai_uts", "nilai_uas"):
            if field in body and body[field] is not None:
                err = validasi_nilai(field, body[field])
                if err:
                    return response_err(err)
                set_parts.append(f"{field} = %s")
                params.append(float(body[field]))

        if not set_parts:
            return response_err("Tidak ada field yang diupdate")

        params.append(id)    # untuk WHERE id = %s
        cursor.execute(
            f"UPDATE mahasiswa SET {', '.join(set_parts)} WHERE id = %s",
            params
        )
        conn.commit()

        # Ambil data terbaru (MySQL otomatis hitung ulang generated columns)
        cursor.execute("SELECT * FROM mahasiswa WHERE id = %s", (id,))
        mhs = row_to_dict(cursor, cursor.fetchone())

    except MySQLError as e:
        conn.rollback()
        return response_err(f"Database error: {e.msg}", 500)
    finally:
        cursor.close()
        conn.close()

    return response_ok(
        data=mhs,
        message=f"Mahasiswa ID {id} berhasil diupdate"
    )


# ============================================================
# ENDPOINT 7: HAPUS MAHASISWA
# DELETE /mahasiswa/<id>
# ============================================================

@app.route("/mahasiswa/<int:id>", methods=["DELETE"])
def hapus_mahasiswa(id):
    """DELETE /mahasiswa/<id> → hapus mahasiswa berdasarkan ID."""
    conn   = get_db()
    cursor = conn.cursor()
    try:
        # Ambil data dulu sebelum dihapus (untuk isi response)
        cursor.execute("SELECT * FROM mahasiswa WHERE id = %s", (id,))
        row = cursor.fetchone()
        if not row:
            return response_err(f"Mahasiswa ID {id} tidak ditemukan", 404)

        mhs = row_to_dict(cursor, row)

        cursor.execute("DELETE FROM mahasiswa WHERE id = %s", (id,))
        conn.commit()

    except MySQLError as e:
        conn.rollback()
        return response_err(f"Database error: {e.msg}", 500)
    finally:
        cursor.close()
        conn.close()

    return response_ok(
        data=mhs,
        message=f"Mahasiswa '{mhs['nama']}' (ID {id}) berhasil dihapus"
    )


# ============================================================
# ERROR HANDLERS
# ============================================================

@app.errorhandler(404)
def not_found(e):
    return response_err(f"Endpoint '{request.path}' tidak ditemukan", 404)


@app.errorhandler(405)
def method_not_allowed(e):
    return response_err(
        f"Method '{request.method}' tidak diizinkan di endpoint ini", 405
    )


@app.errorhandler(500)
def internal_error(e):
    return response_err("Terjadi kesalahan di server", 500)


# ============================================================
# MAIN: Jalankan server
# ============================================================

if __name__ == "__main__":
    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║       API NILAI MAHASISWA - Flask + MySQL            ║")
    print("╠══════════════════════════════════════════════════════╣")
    print(f"║  Server:   http://localhost:5001                     ║")
    print(f"║  Database: MySQL @ {DB_CONFIG['host']}:{DB_CONFIG['port']}                    ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║  ENDPOINTS:                                          ║")
    print("║  GET    /                          → info API        ║")
    print("║  GET    /mahasiswa                 → semua data      ║")
    print("║  GET    /mahasiswa?sort=nilai_akhir&order=desc       ║")
    print("║  GET    /mahasiswa?grade=A         → filter grade    ║")
    print("║  GET    /mahasiswa/statistik       → statistik       ║")
    print("║  GET    /mahasiswa/search?nama=xx  → cari nama       ║")
    print("║  GET    /mahasiswa/<id>            → by ID           ║")
    print("║  POST   /mahasiswa                 → tambah baru     ║")
    print("║  PUT    /mahasiswa/<id>            → update          ║")
    print("║  DELETE /mahasiswa/<id>            → hapus           ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()

    debug = os.getenv("FLASK_DEBUG", "true").lower() in ("true", "1", "yes")
    app.run(debug=debug, host="0.0.0.0", port=5001)
