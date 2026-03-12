"""
╔══════════════════════════════════════════════════════════════╗
║   STEP 2: FLASK DASAR                                        ║
║   Memahami cara kerja Flask sebelum ke app lengkap           ║
╚══════════════════════════════════════════════════════════════╝

INSTALASI:
    pip install flask

JALANKAN FILE INI:
    python3 step_02_flask_dasar.py

TEST DI BROWSER ATAU CURL:
    curl http://localhost:5000/
    curl http://localhost:5000/sapa/Budi
    curl http://localhost:5000/hitung/10/3
"""

from flask import Flask, request, jsonify

# ============================================================
# MEMBUAT APLIKASI FLASK
# ============================================================

# Flask(__name__) → membuat instance aplikasi Flask
# __name__ → nama module saat ini, dipakai Flask untuk
#             menentukan root folder aplikasi
app = Flask(__name__)


# ============================================================
# ROUTE / ENDPOINT DASAR
# ============================================================

# @app.route("/path") → decorator yang menghubungkan URL ke function
# Function yang didekorasi disebut "view function"

@app.route("/")
def home():
    """
    GET /
    Route paling dasar, hanya return pesan sambutan.
    """
    # jsonify() → mengubah dict Python menjadi JSON response
    return jsonify({
        "success": True,
        "message": "Selamat datang di API Belajar Flask!",
        "version": "1.0.0"
    })


# ============================================================
# ROUTE DENGAN URL PARAMETER
# ============================================================

@app.route("/sapa/<nama>")
def sapa(nama):
    """
    GET /sapa/<nama>
    <nama> adalah URL parameter → ditangkap sebagai argument function.
    Contoh: GET /sapa/Budi → nama = "Budi"
    """
    # f-string untuk format pesan
    pesan = f"Halo, {nama.title()}! Selamat belajar Flask."

    return jsonify({
        "success": True,
        "message": pesan,
        "nama": nama.title()
    })


@app.route("/mahasiswa/<int:id>")
def get_mahasiswa_by_id(id):
    """
    GET /mahasiswa/<id>
    <int:id> → konversi URL parameter ke integer otomatis (type casting).
    Jika bukan integer, Flask otomatis return 404.
    """
    # Simulasi data (nanti pakai list of dict yang sesungguhnya)
    data_dummy = {1: "Alice", 2: "Bob", 3: "Charlie"}

    # Conditional: cek apakah ID ada
    if id not in data_dummy:
        # jsonify() + tuple (response, status_code)
        return jsonify({
            "success": False,
            "message": f"Mahasiswa dengan ID {id} tidak ditemukan"
        }), 404

    return jsonify({
        "success": True,
        "data": {"id": id, "nama": data_dummy[id]}
    })


# ============================================================
# ROUTE DENGAN BEBERAPA HTTP METHOD
# ============================================================

@app.route("/hitung/<float:a>/<float:b>", methods=["GET"])
def hitung(a, b):
    """
    GET /hitung/<a>/<b>
    Menghitung berbagai operasi aritmatika.
    <float:a> → konversi ke float.
    """
    # Dictionary untuk menyimpan hasil (tipe data dict)
    hasil = {
        "tambah": a + b,
        "kurang": a - b,
        "kali": a * b,
        # Ternary operator untuk validasi bagi nol
        "bagi": (a / b) if b != 0 else "Error: bagi dengan nol",
        "modulus": (a % b) if b != 0 else "Error: bagi dengan nol",
    }

    return jsonify({
        "success": True,
        "input": {"a": a, "b": b},
        "hasil": hasil
    })


# ============================================================
# QUERY PARAMETERS (?key=value di URL)
# ============================================================

@app.route("/cari")
def cari():
    """
    GET /cari?kata=python&limit=5
    Query parameter diambil dengan request.args.get()
    Contoh: GET /cari?kata=budi&limit=3
    """
    # request.args adalah ImmutableDict dari query string
    # .get("key", default) → aman, tidak error jika key tidak ada
    kata = request.args.get("kata", "")
    limit = request.args.get("limit", 10)

    # Type casting: limit dari query string selalu string
    try:
        limit = int(limit)
    except ValueError:
        return jsonify({
            "success": False,
            "message": "Parameter 'limit' harus berupa angka"
        }), 400

    # String methods: lower() dan in operator
    data = ["Alice", "Bob", "Charlie", "Diana", "Eddie", "Fiona"]
    hasil = [n for n in data if kata.lower() in n.lower()][:limit]

    return jsonify({
        "success": True,
        "keyword": kata,
        "limit": limit,
        "count": len(hasil),
        "data": hasil
    })


# ============================================================
# MENERIMA JSON BODY (POST/PUT)
# ============================================================

@app.route("/echo", methods=["POST"])
def echo():
    """
    POST /echo
    Body: JSON { "pesan": "..." }
    Mengembalikan kembali data yang dikirim (echo).

    Test dengan curl:
        curl -X POST http://localhost:5000/echo \\
             -H "Content-Type: application/json" \\
             -d '{"pesan": "Halo dunia"}'
    """
    # request.get_json() → parse JSON body dari request
    body = request.get_json()

    # Validasi: body tidak boleh None atau kosong
    # Logical operator: or
    if not body:
        return jsonify({
            "success": False,
            "message": "Request body harus berupa JSON"
        }), 400

    # Mengambil field dari dict dengan .get() (aman, tidak error)
    pesan = body.get("pesan", "").strip()  # string method: strip()

    # Conditional
    if not pesan:
        return jsonify({
            "success": False,
            "message": "Field 'pesan' wajib diisi"
        }), 400

    return jsonify({
        "success": True,
        "message": "Echo berhasil",
        "data": {
            "pesan_asli": pesan,
            "pesan_upper": pesan.upper(),       # string method
            "pesan_balik": pesan[::-1],          # string slicing
            "jumlah_karakter": len(pesan),       # built-in len()
            "jumlah_kata": len(pesan.split()),   # string method split()
        }
    })


# ============================================================
# ERROR HANDLER
# ============================================================

@app.errorhandler(404)
def not_found(e):
    """Tangani semua request ke URL yang tidak terdaftar."""
    return jsonify({
        "success": False,
        "message": f"Endpoint tidak ditemukan: {request.path}"
    }), 404


@app.errorhandler(405)
def method_not_allowed(e):
    """Tangani HTTP method yang tidak diizinkan."""
    return jsonify({
        "success": False,
        "message": f"Method {request.method} tidak diizinkan di endpoint ini"
    }), 405


# ============================================================
# MENJALANKAN SERVER
# ============================================================

if __name__ == "__main__":
    print("=" * 55)
    print("  Flask Server - STEP 2: Dasar Flask")
    print("=" * 55)
    print("  Endpoint tersedia:")
    print("  GET  http://localhost:5000/")
    print("  GET  http://localhost:5000/sapa/NamaMu")
    print("  GET  http://localhost:5000/mahasiswa/1")
    print("  GET  http://localhost:5000/hitung/10/3")
    print("  GET  http://localhost:5000/cari?kata=ali")
    print("  POST http://localhost:5000/echo")
    print("=" * 55)
    print("  Tekan CTRL+C untuk stop server")
    print()

    # debug=True → auto-reload saat file berubah, tampilkan error detail
    app.run(debug=True, port=5000)
