Berikut contoh data real untuk endpoint `PUT /mahasiswa/<id>`:

---

### Request

```
PUT /mahasiswa/3
Content-Type: application/json
```
```json
{
    "nama": "Budi Santoso Wijaya",
    "nilai_tugas": 85,
    "nilai_uas": 90
}
```

Catatan: `nilai_uts` **tidak dikirim** — ini partial update, hanya field yang dikirim yang berubah.

---

### Step-by-step dengan data real

**Baris 449–451: Ambil body**
```python
body = {"nama": "Budi Santoso Wijaya", "nilai_tugas": 85, "nilai_uas": 90}
# body ada isi → lanjut (tidak return error)
```

**Baris 457–459: Cek ID ada di database**
```sql
SELECT id FROM mahasiswa WHERE id = 3
-- Hasil: (3,) → ada → lanjut
```

**Baris 462–463: Siapkan wadah kosong**
```python
set_parts = []
params    = []
```

**Baris 465–470: Proses field "nama"**
```python
# "nama" in body? → Ya
nama_baru = "Budi Santoso Wijaya".strip()  # → "Budi Santoso Wijaya"
# nama kosong? → Tidak → lanjut

set_parts = ["nama = %s"]
params    = ["Budi Santoso Wijaya"]
```

**Baris 473–479: Loop 3 field nilai**
```
Iterasi 1: field = "nilai_tugas"
  → ada di body? Ya (85)
  → validasi: 0 ≤ 85 ≤ 100 → OK
  → set_parts = ["nama = %s", "nilai_tugas = %s"]
  → params    = ["Budi Santoso Wijaya", 85.0]

Iterasi 2: field = "nilai_uts"
  → ada di body? Tidak → skip

Iterasi 3: field = "nilai_uas"
  → ada di body? Ya (90)
  → validasi: 0 ≤ 90 ≤ 100 → OK
  → set_parts = ["nama = %s", "nilai_tugas = %s", "nilai_uas = %s"]
  → params    = ["Budi Santoso Wijaya", 85.0, 90.0]
```

**Baris 481–482: Ada yang diupdate?**
```python
set_parts = ["nama = %s", "nilai_tugas = %s", "nilai_uas = %s"]
# len = 3 → ada isi → lanjut (tidak return error)
```

**Baris 484–489: Bangun & eksekusi query**
```python
params.append(3)  # tambah id di akhir untuk WHERE
# params = ["Budi Santoso Wijaya", 85.0, 90.0, 3]

# ', '.join(set_parts) → "nama = %s, nilai_tugas = %s, nilai_uas = %s"
```
Query final yang dikirim ke MySQL:
```sql
UPDATE mahasiswa SET nama = %s, nilai_tugas = %s, nilai_uas = %s WHERE id = %s
-- params: ["Budi Santoso Wijaya", 85.0, 90.0, 3]

-- MySQL eksekusi menjadi:
UPDATE mahasiswa SET nama = 'Budi Santoso Wijaya', nilai_tugas = 85.0, nilai_uas = 90.0 WHERE id = 3
```
```python
conn.commit()  # simpan perubahan ke disk
```

**Baris 492–493: Ambil data terbaru**
```sql
SELECT * FROM mahasiswa WHERE id = 3
```
MySQL otomatis hitung ulang **generated columns**:
```
nilai_uts masih lama = 55 (tidak diubah)
nilai_akhir = (85 × 0.3) + (55 × 0.3) + (90 × 0.4) = 25.5 + 16.5 + 36.0 = 78.0
grade       = 78.0 ≥ 70 → "B"
status      = "LULUS"
```

**Baris 502–505: Response**
```json
{
    "success": true,
    "message": "Mahasiswa ID 3 berhasil diupdate",
    "data": {
        "id": 3,
        "nama": "Budi Santoso Wijaya",
        "nim": "2024003",
        "nilai_tugas": 85.0,
        "nilai_uts": 55.0,
        "nilai_uas": 90.0,
        "nilai_akhir": 78.0,
        "grade": "B",
        "status": "LULUS",
        "created_at": "2025-03-12T10:00:00",
        "updated_at": "2025-03-12T14:30:00"
    }
}
```

---

### Perbandingan sebelum vs sesudah

| Field | Sebelum | Sesudah | Keterangan |
|---|---|---|---|
| nama | Budi Santoso | Budi Santoso Wijaya | diubah |
| nilai_tugas | 60.0 | **85.0** | diubah |
| nilai_uts | 55.0 | 55.0 | tidak dikirim → tetap |
| nilai_uas | 65.0 | **90.0** | diubah |
| nilai_akhir | 60.5 | **78.0** | auto hitung MySQL |
| grade | C | **B** | auto hitung MySQL |
| status | LULUS | LULUS | auto hitung MySQL |

---

### Contoh error case

**Body kosong:**
```json
PUT /mahasiswa/3   body: {}
→ 400: "Tidak ada field yang diupdate"
```

**ID tidak ada:**
```json
PUT /mahasiswa/999  body: {"nama": "Test"}
→ 404: "Mahasiswa ID 999 tidak ditemukan"
```

**Nilai di luar range:**
```json
PUT /mahasiswa/3   body: {"nilai_tugas": 150}
→ 400: "nilai_tugas harus antara 0 dan 100"
```