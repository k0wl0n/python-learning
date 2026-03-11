def hitung_nilai_mahasiswa(nama, tugas, uts, uas):
    nilai_akhir = tugas*0.3 + uts*0.3 + uas *0.4
    if nilai_akhir >= 85:
        Grade = "A"
    elif nilai_akhir >= 70:
        Grade = "B"
    elif nilai_akhir >= 60:
        Grade = "C"
    elif nilai_akhir >= 50:
        Grade = "D"
    elif nilai_akhir < 50:
        Grade = "E"
    print(f"Nama Mahasiswa: {nama}, Nilai Akhir: {nilai_akhir}, Grade: {Grade}")

hitung_nilai_mahasiswa("Andi", 80, 75, 90)
