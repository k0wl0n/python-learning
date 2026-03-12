[6 tools called]

Berikut penjelasan di mana `index.html` ditempatkan dalam arsitektur template:

---

### Struktur file

```
day-2/api/
├── step_05_frontend.py          ← Flask frontend server
├── templates/                   ← folder khusus Jinja2
│   ├── layout.html              ← template INDUK (base)
│   ├── index.html               ← halaman daftar mahasiswa
│   ├── form_mahasiswa.html      ← halaman tambah/edit
│   └── statistik.html           ← halaman statistik
```

### Bagaimana `index.html` masuk ke `layout.html`

`layout.html` adalah **kerangka** halaman — berisi navbar, footer, CSS, dan JS yang sama di semua halaman. Di dalamnya ada lubang kosong:

```108:108:day-2/api/templates/layout.html
    {% block content %}{% endblock %}
```

`index.html` **mengisi lubang itu** dengan `{% extends %}` dan `{% block content %}`:

```14:18:day-2/api/templates/index.html
{% extends "layout.html" %}

{% block title %}Daftar Mahasiswa{% endblock %}

{% block content %}
```

### Hasil akhir yang dikirim ke browser

Jinja2 menggabungkan keduanya menjadi satu HTML utuh:

```
┌─────────────────────────────────────────────┐
│  layout.html                                │
│  ┌───────────────────────────────────────┐  │
│  │ <head>                                │  │
│  │   <title>Daftar Mahasiswa</title>  ◄──── block title dari index.html
│  │   Bootstrap CSS                       │  │
│  │ </head>                               │  │
│  ├───────────────────────────────────────┤  │
│  │ NAVBAR  (dari layout.html)            │  │
│  ├───────────────────────────────────────┤  │
│  │ Flash Messages (dari layout.html)     │  │
│  ├───────────────────────────────────────┤  │
│  │                                       │  │
│  │  ┌─────────────────────────────────┐  │  │
│  │  │  block content                  │  │  │
│  │  │  ╔═══════════════════════════╗  │  │  │
│  │  │  ║ index.html                ║  │  │  │
│  │  │  ║ • Search bar              ║  │  │  │
│  │  │  ║ • Filter grade & sort     ║  │  │  │
│  │  │  ║ • Tabel mahasiswa         ║  │  │  │
│  │  │  ║ • Tombol edit & hapus     ║  │  │  │
│  │  │  ╚═══════════════════════════╝  │  │  │
│  │  └─────────────────────────────────┘  │  │
│  │                                       │  │
│  ├───────────────────────────────────────┤  │
│  │ FOOTER  (dari layout.html)            │  │
│  │ Bootstrap JS                          │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Alur data lengkap

```
Browser buka http://localhost:8001/
        │
        ▼
step_05_frontend.py → def index()          ← route "/"
        │
        ├─ Ambil query params (sort, grade, search)
        ├─ Panggil API backend: GET http://localhost:5001/mahasiswa
        ├─ Terima data = [{...}, {...}, ...]
        │
        ▼
render_template("index.html",             ← cari di folder templates/
    mahasiswa = data,                         variabel dikirim ke template
    sort_by   = sort_by,
    grade     = grade,
    search    = search,
    order     = order,
)
        │
        ▼
Jinja2 proses:
  1. index.html bilang {% extends "layout.html" %}
  2. Buka layout.html sebagai kerangka
  3. Isi {% block title %} → "Daftar Mahasiswa"
  4. Isi {% block content %} → isi index.html (tabel, search, dll)
  5. Loop {% for mhs in mahasiswa %} → render tiap baris tabel
        │
        ▼
HTML utuh dikirim ke browser
```

Jadi `index.html` bukan halaman mandiri — ia adalah **potongan konten** yang disisipkan ke dalam `layout.html` oleh Jinja2 sebelum dikirim ke browser.