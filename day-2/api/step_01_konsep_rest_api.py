"""
╔══════════════════════════════════════════════════════════════╗
║   STEP 1: KONSEP REST API                                    ║
║   Pahami dulu konsep dasar sebelum coding                    ║
╚══════════════════════════════════════════════════════════════╝

=== APA ITU API? ===

API = Application Programming Interface
      Jembatan komunikasi antara aplikasi.

     ┌──────────────┐    HTTP Request     ┌──────────────┐
     │   Frontend   │ ──────────────────► │   Backend    │
     │  (Browser/   │                     │    (Flask)   │
     │   Mobile)    │ ◄────────────────── │              │
     └──────────────┘    JSON Response    └──────────────┘

=== APA ITU REST? ===

REST = REpresentational State Transfer
       Aturan standar untuk membuat API yang konsisten.

Prinsip utama REST:
    1. Gunakan URL untuk menunjuk RESOURCE (data)
    2. Gunakan HTTP METHOD untuk menunjuk AKSI
    3. Response dalam format JSON

=== HTTP METHODS ===

    ┌─────────┬──────────────────────────────────────────────────┐
    │ METHOD  │ KEGUNAAN                                         │
    ├─────────┼──────────────────────────────────────────────────┤
    │ GET     │ Mengambil/membaca data                            │
    │ POST    │ Membuat/menambah data baru                        │
    │ PUT     │ Mengubah/update data (seluruhnya)                 │
    │ PATCH   │ Mengubah sebagian data saja                       │
    │ DELETE  │ Menghapus data                                    │
    └─────────┴──────────────────────────────────────────────────┘

=== URL PATTERN (Endpoint) ===

    Nama resource sebaiknya JAMAK (plural) dan lowercase:

    GET    /mahasiswa          → ambil semua mahasiswa
    GET    /mahasiswa/5        → ambil mahasiswa dengan ID=5
    POST   /mahasiswa          → tambah mahasiswa baru
    PUT    /mahasiswa/5        → update mahasiswa ID=5
    DELETE /mahasiswa/5        → hapus mahasiswa ID=5

=== HTTP STATUS CODE ===

    2xx = Sukses
        200 OK          → Request berhasil
        201 Created     → Data berhasil dibuat
        204 No Content  → Berhasil, tanpa response body

    4xx = Error dari Client
        400 Bad Request     → Data yang dikirim salah/kurang
        404 Not Found       → Data tidak ditemukan
        409 Conflict        → Konflik, misal NIM sudah ada

    5xx = Error dari Server
        500 Internal Server Error → Bug di server

=== FORMAT JSON RESPONSE (Standar yang kita pakai) ===

Sukses:
    {
        "success": true,
        "message": "Mahasiswa berhasil ditambahkan",
        "data": { ... }
    }

Gagal:
    {
        "success": false,
        "message": "NIM sudah terdaftar",
        "data": null
    }

=== TOOLS UNTUK TEST API ===

    1. cURL (terminal)
       curl http://localhost:5000/mahasiswa

    2. Postman (GUI, download di postman.com)

    3. VS Code REST Client extension
       Buat file .http, tulis request langsung di VS Code

    4. Python requests library (kita pakai di test_api.py)
       import requests
       r = requests.get("http://localhost:5000/mahasiswa")

=== ALUR PROJECT KITA ===

    step_01_konsep_rest_api.py  ← KAMU DI SINI
    step_02_flask_dasar.py      → Belajar Flask dasar
    step_03_data_model.py       → Desain data & helper functions -> mysql
    step_04_backend_api.py      → Aplikasi lengkap
    test_api.py                 → Test semua endpoint
"""

print("=" * 60)
print("  STEP 1: KONSEP REST API")
print("=" * 60)
print()
print("  REST API adalah cara standar membuat backend server.")
print()
print("  HTTP Methods:")
print("    GET    → Baca data")
print("    POST   → Buat data baru")
print("    PUT    → Update data")
print("    DELETE → Hapus data")
print()
print("  URL pattern:")
print("    GET  /mahasiswa      → semua mahasiswa")
print("    GET  /mahasiswa/1    → mahasiswa id=1")
print("    POST /mahasiswa      → tambah mahasiswa")
print("    PUT  /mahasiswa/1    → update id=1")
print("    DEL  /mahasiswa/1    → hapus id=1")
print()
print("  ✅ Konsep sudah dipahami? Lanjut ke step_02_flask_dasar.py")
print("=" * 60)
