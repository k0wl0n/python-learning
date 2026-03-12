flowchart TD
    A["🌐 GET /mahasiswa"] --> B["Ambil parameter dari URL"]
    B --> B1["Baca parameter:<br>• sort (kolom pengurutan)<br>• order (asc / desc)<br>• grade (filter nilai huruf)"]

    B1 --> C{"Kolom sort<br>valid?"}
    C -- "Tidak valid" --> C1["❌ Kembalikan pesan error:<br>kolom sort tidak dikenali"]

    C -- "Valid / kosong" --> D["Siapkan query dasar:<br>ambil semua data mahasiswa"]

    D --> E{"Ada filter<br>grade?"}
    E -- "Ya" --> E1["Tambahkan kondisi:<br>hanya ambil grade tertentu"]
    E1 --> F
    E -- "Tidak" --> F{"Ada<br>pengurutan?"}

    F -- "Ya" --> F1{"Urutan<br>menurun?"}
    F1 -- "Ya" --> F2["Urutkan dari besar ke kecil"]
    F1 -- "Tidak" --> F3["Urutkan dari kecil ke besar"]
    F2 --> F4["Tambahkan pengurutan ke query"]
    F3 --> F4

    F -- "Tidak" --> G
    F4 --> G["Buka koneksi database"]

    G --> H["Jalankan query ke MySQL"]
    H --> I["Ambil semua baris hasil<br>dan ubah ke format daftar"]
    I --> J["Tutup koneksi database"]
    J --> K["✅ Kirim respons:<br>data mahasiswa + jumlah ditemukan"]

    style A fill:#4A90D9,color:#fff
    style C1 fill:#E74C3C,color:#fff
    style K fill:#27AE60,color:#fff
    style C fill:#F39C12,color:#fff
    style E fill:#F39C12,color:#fff
    style F fill:#F39C12,color:#fff
    style F1 fill:#F39C12,color:#fff
