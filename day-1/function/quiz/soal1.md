Berikut contoh **soal latihan Python** untuk membuat **function menghitung nilai mahasiswa**.

---

# Soal: Menghitung Nilai Mahasiswa

Buatlah sebuah **function Python** bernama `hitung_nilai_mahasiswa()` yang digunakan untuk menghitung nilai akhir seorang mahasiswa.

## Ketentuan

Seorang mahasiswa memiliki 3 komponen nilai:

* **Tugas** (30%)
* **UTS** (30%)
* **UAS** (40%)

Nilai akhir dihitung dengan rumus berikut:

Nilai\ Akhir = (0.3 \times Tugas) + (0.3 \times UTS) + (0.4 \times UAS)

---

## Kriteria Nilai Huruf

| Nilai Akhir | Grade |
| ----------- | ----- |
| ≥ 85        | A     |
| ≥ 70        | B     |
| ≥ 60        | C     |
| ≥ 50        | D     |
| < 50        | E     |

---

## Tugas yang Harus Dibuat

1. Buat function:

```
hitung_nilai_mahasiswa(nama, tugas, uts, uas)
```

2. Function harus:

* menghitung **nilai akhir**
* menentukan **grade**
* menampilkan hasil dalam format berikut

---

## Contoh Output

Jika input:

```
Nama  : Andi
Tugas : 80
UTS   : 75
UAS   : 90
```

Output:

```
Nama Mahasiswa : Andi
Nilai Akhir    : 83.5
Grade          : B
```

---

## Bonus Challenge

Tambahkan fitur:

1. Jika nilai **di bawah 60**, tampilkan:

```
Status : Tidak Lulus
```

2. Jika nilai **≥ 60**:

```
Status : Lulus
```

---

Jika kamu mau, saya juga bisa buatkan:

* **versi soal yang lebih sulit (pakai list mahasiswa + loop)**
* **versi interview question style**
* **versi mini project sistem nilai mahasiswa (ranking + rata-rata kelas)**.
