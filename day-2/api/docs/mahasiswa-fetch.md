[1 tool called]

Berikut penjelasan dengan data nyata:

---

### Data dari MySQL (raw)

MySQL mengembalikan data sebagai **tuple** (tanpa nama kolom):

```python
cursor.description = [
    ("id",),
    ("nama",),
    ("nim",),
    ("nilai_tugas",),
    ("nilai_uts",),
    ("nilai_uas",),
    ("nilai_akhir",),
    ("grade",),
    ("status",),
    ("created_at",),
    ("updated_at",),
]

rows = [
    (1, "Andi Pratama",   "2024001", Decimal('80.00'), Decimal('75.00'), Decimal('85.00'), Decimal('80.50'), "B", "LULUS",       datetime(2025, 3, 12, 10, 0), datetime(2025, 3, 12, 10, 0)),
    (2, "Siti Rahma",     "2024002", Decimal('90.00'), Decimal('88.00'), Decimal('92.00'), Decimal('90.20'), "A", "LULUS",       datetime(2025, 3, 12, 10, 0), datetime(2025, 3, 12, 10, 0)),
    (3, "Budi Santoso",   "2024003", Decimal('60.00'), Decimal('55.00'), Decimal('65.00'), Decimal('60.50'), "C", "LULUS",       datetime(2025, 3, 12, 10, 0), datetime(2025, 3, 12, 10, 0)),
    (4, "Fani Anggraini", "2024006", Decimal('30.00'), Decimal('35.00'), Decimal('25.00'), Decimal('29.50'), "E", "TIDAK LULUS", datetime(2025, 3, 12, 10, 0), datetime(2025, 3, 12, 10, 0)),
]
```

### Proses `row_to_dict` (1 baris)

Ambil baris pertama sebagai contoh:

```
cursor.description → ["id", "nama", "nim", "nilai_tugas", ...]
row                → (1,    "Andi Pratama", "2024001", Decimal('80.00'), ...)
```

`zip` pasangkan satu-satu:

```
("id",          1)                          → result["id"] = 1
("nama",        "Andi Pratama")             → result["nama"] = "Andi Pratama"
("nim",         "2024001")                  → result["nim"] = "2024001"
("nilai_tugas", Decimal('80.00'))           → result["nilai_tugas"] = 80.0        ← Decimal → float
("nilai_uts",   Decimal('75.00'))           → result["nilai_uts"] = 75.0          ← Decimal → float
("nilai_uas",   Decimal('85.00'))           → result["nilai_uas"] = 85.0          ← Decimal → float
("nilai_akhir", Decimal('80.50'))           → result["nilai_akhir"] = 80.5        ← Decimal → float
("grade",       "B")                        → result["grade"] = "B"
("status",      "LULUS")                    → result["status"] = "LULUS"
("created_at",  datetime(2025,3,12,10,0))   → result["created_at"] = "2025-03-12T10:00:00"  ← datetime → string
("updated_at",  datetime(2025,3,12,10,0))   → result["updated_at"] = "2025-03-12T10:00:00"  ← datetime → string
```

Hasil: **1 dict**

```python
{
    "id": 1,
    "nama": "Andi Pratama",
    "nim": "2024001",
    "nilai_tugas": 80.0,
    "nilai_uts": 75.0,
    "nilai_uas": 85.0,
    "nilai_akhir": 80.5,
    "grade": "B",
    "status": "LULUS",
    "created_at": "2025-03-12T10:00:00",
    "updated_at": "2025-03-12T10:00:00"
}
```

### Proses `rows_to_list` (semua baris)

List comprehension menjalankan `row_to_dict` untuk **setiap row**:

```python
[row_to_dict(cursor, row) for row in rows]
#    ↑ baris 1                  ↑ loop 4 baris
#    ↑ baris 2
#    ↑ baris 3
#    ↑ baris 4
```

Hasil akhir: **list of dict** — siap jadi JSON response:

```json
[
    {"id": 1, "nama": "Andi Pratama",   "nilai_akhir": 80.5, "grade": "B", "status": "LULUS",       ...},
    {"id": 2, "nama": "Siti Rahma",     "nilai_akhir": 90.2, "grade": "A", "status": "LULUS",       ...},
    {"id": 3, "nama": "Budi Santoso",   "nilai_akhir": 60.5, "grade": "C", "status": "LULUS",       ...},
    {"id": 4, "nama": "Fani Anggraini", "nilai_akhir": 29.5, "grade": "E", "status": "TIDAK LULUS", ...}
]
```

---

### Kenapa perlu konversi?

| Tipe MySQL | Tipe Python | Masalah | Solusi |
|---|---|---|---|
| `DECIMAL(5,2)` | `Decimal('80.50')` | `jsonify()` tidak bisa serialize Decimal | `float(val)` → `80.5` |
| `TIMESTAMP` | `datetime(2025,3,12)` | `jsonify()` tidak bisa serialize datetime | `val.isoformat()` → `"2025-03-12T10:00:00"` |
| `INT`, `VARCHAR` | `int`, `str` | Sudah JSON-safe | Langsung pakai |