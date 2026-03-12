-- ============================================================
-- INIT.SQL - Database Nilai Mahasiswa
-- Auto-run oleh MySQL saat container pertama kali dibuat
-- ============================================================

CREATE DATABASE IF NOT EXISTS nilai_mahasiswa;
USE nilai_mahasiswa;

-- ============================================================
-- TABEL MAHASISWA
-- ============================================================
CREATE TABLE IF NOT EXISTS mahasiswa (
    id          INT             AUTO_INCREMENT PRIMARY KEY,
    nama        VARCHAR(100)    NOT NULL,
    nim         VARCHAR(20)     NOT NULL UNIQUE,
    nilai_tugas DECIMAL(5,2)    NOT NULL CHECK (nilai_tugas BETWEEN 0 AND 100),
    nilai_uts   DECIMAL(5,2)    NOT NULL CHECK (nilai_uts   BETWEEN 0 AND 100),
    nilai_uas   DECIMAL(5,2)    NOT NULL CHECK (nilai_uas   BETWEEN 0 AND 100),
    nilai_akhir DECIMAL(5,2)    GENERATED ALWAYS AS (
                    ROUND((nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4), 2)
                ) STORED,
    grade       CHAR(1)         GENERATED ALWAYS AS (
                    CASE
                        WHEN ROUND((nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4), 2) >= 85 THEN 'A'
                        WHEN ROUND((nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4), 2) >= 70 THEN 'B'
                        WHEN ROUND((nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4), 2) >= 55 THEN 'C'
                        WHEN ROUND((nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4), 2) >= 40 THEN 'D'
                        ELSE 'E'
                    END
                ) STORED,
    status      VARCHAR(12)     GENERATED ALWAYS AS (
                    CASE
                        WHEN ROUND((nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4), 2) >= 40 THEN 'LULUS'
                        ELSE 'TIDAK LULUS'
                    END
                ) STORED,
    created_at  TIMESTAMP       DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP       DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ============================================================
-- SEED DATA (sama dengan seed_data() di step_04_backend_api.py)
-- nilai_akhir, grade, status dihitung otomatis oleh DB
-- ============================================================
INSERT INTO mahasiswa (nama, nim, nilai_tugas, nilai_uts, nilai_uas) VALUES
    ('Andi Pratama',   '2024001', 80, 75, 85),  -- nilai_akhir=81.5,  grade=B, LULUS
    ('Siti Rahma',     '2024002', 90, 88, 92),  -- nilai_akhir=90.2,  grade=A, LULUS
    ('Budi Santoso',   '2024003', 60, 55, 65),  -- nilai_akhir=60.5,  grade=C, LULUS
    ('Diana Putri',    '2024004', 45, 40, 50),  -- nilai_akhir=45.5,  grade=D, LULUS
    ('Eko Wijaya',     '2024005', 95, 90, 95),  -- nilai_akhir=93.5,  grade=A, LULUS
    ('Fani Anggraini', '2024006', 30, 35, 25);  -- nilai_akhir=29.5,  grade=E, TIDAK LULUS

-- ============================================================
-- VERIFIKASI (tampil saat init)
-- ============================================================
SELECT
    id,
    nama,
    nim,
    nilai_tugas,
    nilai_uts,
    nilai_uas,
    nilai_akhir,
    grade,
    status
FROM mahasiswa
ORDER BY nilai_akhir DESC;
