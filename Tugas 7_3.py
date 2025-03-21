def penjualan_tiket():
    Hari = input("Masukkan Hari yang Dipilih : ")
    Tiket = int(input("Masukkan Jumlah Tiket yang Dibeli : "))

    if Hari  == "Senin":
        harga_tiket = 35000
    elif Hari  == "Selasa":
        harga_tiket = 35000
    elif Hari  == "Rabu":
        harga_tiket = 35000
    elif Hari  == "Kamis":  
        harga_tiket = 35000
    elif Hari  == "Jumat":
        harga_tiket = 45000
    elif Hari  == "Sabtu":
        harga_tiket = 45000
    elif Hari  == "Minggu":
        harga_tiket = 45000
    else:
        print("Hari tidak Valid")
        return
    
    jumlah_harga = Tiket * harga_tiket
    pajak = jumlah_harga * 0.05
    total_harga = jumlah_harga + pajak
        

        

    print("="*50)
    print("=== Tiket yang Dibeli oleh Pelanggan ===")
    print("Hari yang Dipilih oleh Pelangan", Hari)
    print("Jumlah Tiket yang Dibeli : ",Tiket)
    print(f"Jumlah Harga Sebelum Pajak : Rp{jumlah_harga:,.2f};")
    print(f"Pajak yang Diberikan pada Pembeli : Rp{pajak:,.2f};")
    print(f"Harga Total yang Diberikan Kepada Pelanggan : Rp{total_harga:,.2f};")
    
penjualan_tiket()