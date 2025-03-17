def gaji (gaji_pokok):
    tunjangan = gaji_pokok * 0.25
    gaji_sebelum_pajak = tunjangan + gaji_pokok
    pajak = gaji_pokok * 0.05
    print("\nSlip Gaji")
    print("\n=============================")
    print(f"\nGaji sebelum pajak = Rp {gaji_sebelum_pajak:,.2f}")
    print(f"Tunjangan yang didapat = Rp {tunjangan:,.2f}")
    print(f"Pajak Dari Gaji = Rp {pajak:,.2f}")
    return gaji_sebelum_pajak - pajak
gaji_pokok = int(input("masukkan gaji awal = "))
total_penghasilan = gaji(gaji_pokok)
print(f"Total Akhir Gaji = Rp{total_penghasilan:,.2f};")