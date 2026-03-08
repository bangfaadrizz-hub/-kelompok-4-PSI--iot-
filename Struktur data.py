
jumlah_peserta = int(input("Masukkan jumlah peserta: "))

for i in range(1, jumlah_peserta + 1):
    print(f"\nPeserta ke-{i}")
    
    total_nilai = 0
    ada_nilai_kurang_60 = False
    
    for j in range(1, 6):
        nilai = int(input(f"Masukkan nilai sesi {j}: "))
        total_nilai += nilai
        
        if nilai < 60:
            ada_nilai_kurang_60 = True
    
    rata_rata = total_nilai / 5

    if rata_rata >= 75 and not ada_nilai_kurang_60:
        status = "Lulus"
    elif rata_rata >= 75 and ada_nilai_kurang_60:
        status = "Remedial"
    else:
        status = "Tidak Lulus"
    
    print(f"Rata-rata nilai: {rata_rata}")
    print(f"Status: {status}")