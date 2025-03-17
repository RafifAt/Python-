def penjualan (jumlah_barang, harga_satuan):
 total_harga = jumlah_barang * harga_satuan
 pajak = total_harga * 0.05
 total_bayar = total_harga + pajak
 return total_bayar
 
jumlah_barang = int(input("Barang yang Ingin Dibeli = "))
harga_satuan = int(input("Harga Satuan Barang = "))
total_bayar = penjualan(harga_satuan, jumlah_barang)
print("\n\nStruk")
print("================================")
print("Jumlah Barang yang Dibeli = "+str(jumlah_barang))
print("Harga Satuan Barang = "+str(harga_satuan))
print(f"Total Harga Yang Harus Dibayar = {total_bayar:,.2f};")