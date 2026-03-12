flowchart TD
    A["🌐 GET /mahasiswa\n?sort=&order=&grade="] --> B["Extract Query Parameters"]
    B --> B1["sort_by = request.args.get('sort')\norder = request.args.get('order', 'asc')\nfilter_grade = request.args.get('grade')"]

    B1 --> C{"sort_by ada\nDAN\nsort_by ∉ whitelist?"}
    C -- "Ya (invalid)" --> C1["❌ response_err()\n'sort harus salah satu dari:\nnilai_akhir, nama, nim, id'"]

    C -- "Tidak" --> D["sql = 'SELECT * FROM mahasiswa'\nparams = [ ]"]

    D --> E{"filter_grade\nada?"}
    E -- "Ya" --> E1["sql += ' WHERE grade = %s'\nparams.append(grade.upper())"]
    E1 --> F
    E -- "Tidak" --> F{"sort_by\nada?"}

    F -- "Ya" --> F1{"order == 'desc'?"}
    F1 -- "Ya" --> F2["direction = 'DESC'"]
    F1 -- "Tidak" --> F3["direction = 'ASC'"]
    F2 --> F4["sql += ' ORDER BY {sort_by} {direction}'"]
    F3 --> F4

    F -- "Tidak" --> G
    F4 --> G["conn = get_db()\ncursor = conn.cursor()"]

    G --> H["cursor.execute(sql, params)"]
    H --> I["rows = cursor.fetchall()\nhasil = rows_to_list(cursor, rows)"]
    I --> J["cursor.close()\nconn.close()"]
    J --> K["✅ response_ok()\ndata=hasil\nmessage='N mahasiswa ditemukan'"]

    style A fill:#4A90D9,color:#fff
    style C1 fill:#E74C3C,color:#fff
    style K fill:#27AE60,color:#fff
    style C fill:#F39C12,color:#fff
    style E fill:#F39C12,color:#fff
    style F fill:#F39C12,color:#fff
    style F1 fill:#F39C12,color:#fff