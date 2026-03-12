[1 tool called]

Berikut contoh bagaimana query builder bekerja berdasarkan kombinasi parameter yang dikirim user:

---

**Cara kerja:** SQL dibangun bertahap — mulai dari base query, lalu ditambah `WHERE` dan `ORDER BY` tergantung parameter yang ada.

### Skenario 1: Tanpa parameter apapun
```
GET /mahasiswa
```
```sql
SELECT * FROM mahasiswa
-- params: []
```

### Skenario 2: Filter grade saja
```
GET /mahasiswa?grade=A
```
```sql
SELECT * FROM mahasiswa WHERE grade = %s
-- params: ['A']
```

### Skenario 3: Sort saja
```
GET /mahasiswa?sort=nilai_akhir&order=desc
```
```sql
SELECT * FROM mahasiswa ORDER BY nilai_akhir DESC
-- params: []
```

### Skenario 4: Sort ascending (default)
```
GET /mahasiswa?sort=nama
```
```sql
SELECT * FROM mahasiswa ORDER BY nama ASC
-- params: []
```

### Skenario 5: Filter + Sort (lengkap)
```
GET /mahasiswa?grade=B&sort=nilai_akhir&order=desc
```
```sql
SELECT * FROM mahasiswa WHERE grade = %s ORDER BY nilai_akhir DESC
-- params: ['B']
```

### Skenario 6: Sort kolom tidak valid
```
GET /mahasiswa?sort=password
```
```
❌ 400 Bad Request
"sort harus salah satu dari: nilai_akhir, nama, nim, id"
```

---

Secara visual, prosesnya seperti ini:

```
sql = "SELECT * FROM mahasiswa"          ← base selalu sama
               │
               ▼
       ada grade? ──Ya──→ + " WHERE grade = %s"
               │                    params = ['A']
               ▼
       ada sort_by? ──Ya──→ + " ORDER BY nama ASC"
               │
               ▼
       Query final siap dieksekusi
```

Poin penting di pattern ini:
- **`WHERE` pakai `%s`** (parameterized) — aman dari SQL injection, MySQL yang escape nilainya
- **`ORDER BY` pakai f-string** — tidak bisa pakai `%s` untuk nama kolom, makanya dilindungi oleh **whitelist** validation di awal (`valid_sort`)