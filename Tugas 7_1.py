def pengitungan_gaji():
    golongan = input("Masukkan Golongan Karyawan = ")
    jumlahLembur = int(input("Masukkan jumlah = "))

    if golongan == "A":
        gaji_pokok = 2500000
        tunjangan = gaji_pokok * 0.10
        gaji_lembur = 15000
    
    elif golongan == "B":
        gaji_pokok = 3500000
        tunjangan = gaji_pokok * 0.15
        gaji_lembur = 25000
    
    else:
        print ("Tidak Valid")
        return
    
    totalLembur = jumlahLembur * gaji_lembur
    totalGaji = tunjangan + gaji_pokok + gaji_lembur
    pajak = totalGaji * 0.05
    gaji_bersih = totalGaji - pajak

    print ("="*56)
    print ("Penghasilan yang Akan Diterima Karyawan Sesuai Golongan")
    print ("")
    print ("Golongan Karyawan Adalah : ", golongan)
    print ("Total Jam Lembur yang Diambil Karyawan : ", jumlahLembur)
    print (f"Gaji Pokok Karyawan Sejumlah : Rp{gaji_pokok:,.2f};")
    print (f"Tunjangan Karyawan Sejumlah : Rp{tunjangan:,.2f};")
    print (f"Total Gaji Lembur Karyawan Sejumlah : Rp{totalLembur:,.2f};")
    print (f"Total Gaji yang Diterima Sebelum Pajak : Rp{totalGaji:,.2f};")
    print (f"Pajak yang Dikenakana pada Gaji Karyawan : Rp{pajak:,.2f};")
    print (f"Total Gaji yang Diterima Setelah Pajak : Rp{gaji_bersih:,.2f};")
    print ("")
    print ("="*56)

pengitungan_gaji()