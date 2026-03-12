"""
╔══════════════════════════════════════════════════════════════╗
║   STEP 5: FRONTEND - FLASK + BOOTSTRAP + REQUESTS            ║
║   Server-side rendering yang consume REST API                ║
╚══════════════════════════════════════════════════════════════╝

Di file ini kita belajar:
    1. Flask sebagai "frontend server" (render HTML)
    2. Jinja2 template → HTML dinamis dari Python
    3. requests library → panggil REST API dari Python
    4. Bootstrap 5 → tampilan modern tanpa CSS manual
    5. Flash messages → notifikasi sukses/error

Arsitektur:
    Browser → Frontend (port 8001) → API Backend (port 5001) → MySQL

Cara menjalankan:
    1. Pastikan API backend jalan: python step_04_backend_api.py  (port 5001)
    2. Jalankan frontend ini:    python step_05_frontend.py  (port 8001)
    3. Buka browser: http://localhost:8001

Install dependency tambahan:
    pip install requests
"""

import os

import requests                         # library HTTP client → panggil API
from flask import (
    Flask, render_template, request,    # core Flask
    redirect, url_for, flash            # navigasi & notifikasi
)

app = Flask(__name__)

# secret_key wajib ada untuk menggunakan flash() (session)
# Di production: gunakan nilai random yang panjang dan disimpan di env var
app.secret_key = os.getenv("SECRET_KEY", "belajar-python-tpcc-2024")

# ============================================================
# KONFIGURASI: URL API Backend
# ============================================================
# Semua request ke API akan menggunakan base URL ini.
# os.getenv() → baca dari environment variable, fallback ke default.
# Di Docker: API_BASE=http://backend:5001 (nama service docker-compose)
# Di lokal:  default http://localhost:5001
API_BASE = os.getenv("API_BASE", "http://localhost:5001")


# ============================================================
# HELPER: Panggil API
# ============================================================

def api_get(endpoint: str, params: dict = None) -> tuple:
    """
    GET request ke API.
    Return (data, error_message).

    requests.get() → kirim HTTP GET
    response.json() → parse JSON response → dict Python
    """
    try:
        response = requests.get(f"{API_BASE}{endpoint}", params=params, timeout=5)
        hasil    = response.json()   # JSON string → dict Python

        if hasil.get("success"):
            return hasil.get("data"), None
        return None, hasil.get("message", "Terjadi kesalahan")

    except requests.exceptions.ConnectionError:
        return None, f"Tidak bisa terhubung ke API ({API_BASE}). Pastikan step_04_backend_api.py sudah jalan!"
    except requests.exceptions.Timeout:
        return None, "API timeout (tidak merespons dalam 5 detik)"
    except Exception as e:
        return None, f"Error: {str(e)}"


def api_post(endpoint: str, data: dict) -> tuple:
    """
    POST request ke API dengan JSON body.
    Return (data, error_message).

    requests.post(..., json=data) → otomatis set Content-Type: application/json
    """
    try:
        response = requests.post(f"{API_BASE}{endpoint}", json=data, timeout=5)
        hasil    = response.json()

        if hasil.get("success"):
            return hasil.get("data"), None
        return None, hasil.get("message", "Terjadi kesalahan")

    except requests.exceptions.ConnectionError:
        return None, "Tidak bisa terhubung ke API. Pastikan step_04_backend_api.py sudah jalan!"
    except Exception as e:
        return None, f"Error: {str(e)}"


def api_put(endpoint: str, data: dict) -> tuple:
    """PUT request ke API (update data)."""
    try:
        response = requests.put(f"{API_BASE}{endpoint}", json=data, timeout=5)
        hasil    = response.json()

        if hasil.get("success"):
            return hasil.get("data"), None
        return None, hasil.get("message", "Terjadi kesalahan")

    except requests.exceptions.ConnectionError:
        return None, "Tidak bisa terhubung ke API. Pastikan step_04_backend_api.py sudah jalan!"
    except Exception as e:
        return None, f"Error: {str(e)}"


def api_delete(endpoint: str) -> tuple:
    """DELETE request ke API."""
    try:
        response = requests.delete(f"{API_BASE}{endpoint}", timeout=5)
        hasil    = response.json()

        if hasil.get("success"):
            return hasil.get("data"), None
        return None, hasil.get("message", "Terjadi kesalahan")

    except requests.exceptions.ConnectionError:
        return None, "Tidak bisa terhubung ke API. Pastikan step_04_backend_api.py sudah jalan!"
    except Exception as e:
        return None, f"Error: {str(e)}"


# ============================================================
# ROUTES: Halaman Frontend
# ============================================================

@app.route("/")
def index():
    """
    GET /
    Halaman utama: tampilkan semua mahasiswa dalam tabel.

    Query params (opsional):
        ?sort=nilai_akhir&order=desc&grade=A&search=andi

    Konsep:
        - request.args.get() → ambil query parameter dari URL
        - render_template() → render file HTML dengan variabel
        - Jinja2 template → {{ variabel }} di HTML
    """
    # Ambil query params dari URL browser (diteruskan ke API)
    sort_by = request.args.get("sort", None)
    order   = request.args.get("order", "asc")
    grade   = request.args.get("grade", None)
    search  = request.args.get("search", "").strip()

    # Tentukan endpoint yang akan dipanggil
    if search:
        # Gunakan endpoint search jika ada keyword
        data, err = api_get("/mahasiswa/search", params={"nama": search})
    else:
        # Gunakan endpoint utama dengan filter & sort
        params = {}
        if sort_by: params["sort"]  = sort_by
        if order:   params["order"] = order
        if grade:   params["grade"] = grade
        data, err = api_get("/mahasiswa", params=params)

    if err:
        flash(err, "danger")   # flash() → kirim pesan ke template (sekali tampil)
        data = []

    # render_template() → cari file di folder templates/
    # variabel yang dikirim bisa dipakai di HTML dengan {{ nama_var }}
    return render_template("index.html",
        mahasiswa = data or [],
        sort_by   = sort_by,
        order     = order,
        grade     = grade,
        search    = search,
    )


@app.route("/tambah", methods=["GET", "POST"])
def tambah():
    """
    GET  /tambah → tampilkan form kosong
    POST /tambah → kirim data form ke API

    Konsep:
        - methods=["GET", "POST"] → satu route handle 2 method
        - request.method → cek method yang digunakan
        - request.form   → ambil data dari form HTML (POST)
        - redirect()     → redirect ke halaman lain setelah sukses
        - url_for()      → generate URL dari nama fungsi
    """
    if request.method == "POST":
        # request.form → dict-like objek berisi data dari <form> HTML
        # .get() dengan default "" → aman jika field tidak ada
        payload = {
            "nama":        request.form.get("nama", "").strip(),
            "nim":         request.form.get("nim", "").strip(),
            "nilai_tugas": request.form.get("nilai_tugas"),
            "nilai_uts":   request.form.get("nilai_uts"),
            "nilai_uas":   request.form.get("nilai_uas"),
        }

        # Konversi string dari form ke float (type casting)
        try:
            payload["nilai_tugas"] = float(payload["nilai_tugas"])
            payload["nilai_uts"]   = float(payload["nilai_uts"])
            payload["nilai_uas"]   = float(payload["nilai_uas"])
        except (TypeError, ValueError):
            flash("Nilai harus berupa angka!", "danger")
            return render_template("form_mahasiswa.html", mode="tambah", form=payload)

        # Panggil API POST /mahasiswa
        data, err = api_post("/mahasiswa", payload)

        if err:
            flash(err, "danger")
            # Kembalikan form dengan data yang sudah diisi (tidak hilang)
            return render_template("form_mahasiswa.html", mode="tambah", form=payload)

        # Sukses: flash pesan + redirect ke halaman utama
        flash(f"Mahasiswa '{data['nama']}' berhasil ditambahkan! Grade: {data['grade']}", "success")
        return redirect(url_for("index"))

    # GET request → tampilkan form kosong
    return render_template("form_mahasiswa.html", mode="tambah", form={})


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    """
    GET  /edit/<id> → tampilkan form berisi data yang mau diedit
    POST /edit/<id> → kirim data update ke API

    Konsep:
        - <int:id> → URL parameter, Flask konversi ke integer
        - Pre-filled form → ambil data dari API lalu isi ke form
    """
    if request.method == "POST":
        # Ambil hanya field yang diisi (partial update)
        payload = {}

        nama = request.form.get("nama", "").strip()
        if nama:
            payload["nama"] = nama

        for field in ("nilai_tugas", "nilai_uts", "nilai_uas"):
            val = request.form.get(field, "").strip()
            if val:
                try:
                    payload[field] = float(val)
                except ValueError:
                    flash(f"{field} harus berupa angka!", "danger")
                    data, _ = api_get(f"/mahasiswa/{id}")
                    return render_template("form_mahasiswa.html",
                                           mode="edit", form=data, id=id)

        data, err = api_put(f"/mahasiswa/{id}", payload)

        if err:
            flash(err, "danger")
            data, _ = api_get(f"/mahasiswa/{id}")
            return render_template("form_mahasiswa.html",
                                   mode="edit", form=data or {}, id=id)

        flash(f"Data '{data['nama']}' berhasil diupdate! Grade: {data['grade']}", "success")
        return redirect(url_for("index"))

    # GET → ambil data dari API untuk pre-fill form
    data, err = api_get(f"/mahasiswa/{id}")
    if err:
        flash(err, "danger")
        return redirect(url_for("index"))

    return render_template("form_mahasiswa.html", mode="edit", form=data, id=id)


@app.route("/hapus/<int:id>", methods=["POST"])
def hapus(id):
    """
    POST /hapus/<id> → hapus mahasiswa via API lalu redirect

    Kenapa POST bukan GET?
    → Operasi yang mengubah data (hapus, tambah, update) harus POST/PUT/DELETE,
      bukan GET. Ini standar HTTP. Jika GET, browser bisa cache atau
      orang bisa trigger delete hanya dengan share link.
    """
    data, err = api_delete(f"/mahasiswa/{id}")

    if err:
        flash(err, "danger")
    else:
        flash(f"Mahasiswa '{data['nama']}' berhasil dihapus!", "warning")

    # Setelah hapus, kembali ke halaman sebelumnya atau index
    # request.referrer → URL halaman sebelumnya (dari browser header)
    return redirect(request.referrer or url_for("index"))


@app.route("/statistik")
def statistik():
    """
    GET /statistik
    Halaman statistik: tampilkan data agregat mahasiswa.
    """
    data, err = api_get("/mahasiswa/statistik")

    if err:
        flash(err, "danger")
        data = {}

    return render_template("statistik.html", stats=data or {})


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║       FRONTEND - Flask + Bootstrap                   ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║  Frontend : http://localhost:8001                    ║")
    print("║  API      : http://localhost:5001  (harus jalan!)    ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║  HALAMAN:                                            ║")
    print("║  /              → daftar semua mahasiswa             ║")
    print("║  /tambah        → form tambah mahasiswa              ║")
    print("║  /edit/<id>     → form edit mahasiswa                ║")
    print("║  /hapus/<id>    → hapus mahasiswa                    ║")
    print("║  /statistik     → statistik nilai                    ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()

    debug = os.getenv("FLASK_DEBUG", "true").lower() in ("true", "1", "yes")
    app.run(debug=debug, host="0.0.0.0", port=8001)
