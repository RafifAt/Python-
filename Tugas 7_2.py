def hitung_biaya_bengkel():
     Layanan = input("Pilih Layanan Bengkel = ")

     if Layanan == "Turun Mesin":
          biaya = 160000
     elif Layanan == "Ganti V-belt":
          biaya = 50000
     elif Layanan == "Ganti Aki":
          biaya = 50000
     elif Layanan == "Servis Ringan":
          biaya = 80000
     else:
          print("Layanan Tidak Tersedia")
          return
     
     servisRingan = 80000
     if Layanan != "Servis Ringan":
           total_biaya = biaya + servisRingan
     else:
           total_biaya = biaya

     print("="*40)
     print("Layanan Servis yang Dipilih Pelanggan")
     print("")
     print("Pilihan Layanan Servis : ", Layanan)
     print("")
     print(f"Total Biaya yang Dibayar Pelanggan : Rp{total_biaya:,.2f};")
     print("")
     print("="*40)

hitung_biaya_bengkel()