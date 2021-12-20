#contoh kasus:
#NIM D0217011 
#Gaji Pokok = Rp.1.000.000
#Gaji lembur/jam = Rp. 5000
#Lama lembur = Sesuai 2 angka terakhir nim 11
#Gaji lembur = (gaji lembur/jam)*lama lembur
#pajak = 10%

nama = "Nurrasuli (D0217011)"
gaji_pokok = 1000000
Lama_lembur = 11
GajiLembur = 5000
Jumlah_lembur = 5000*11
Gaji_kotor = gaji_pokok + Jumlah_lembur
pajak = 10  / 100
potongan = int(pajak * gaji_pokok)
Gaji_bersih = int(Gaji_kotor-potongan)

print("Nama           :",nama)
print("Gaji Pokok     : Rp",gaji_pokok)
print("Gaji Lembur    : Rp",Jumlah_lembur)
print("Gaji Kotor     : Rp",Gaji_kotor)
print("Pajak          : Rp",pajak)
print("Potongan       : Rp",potongan)
print("Gaji Bersih    : Rp",Gaji_bersih)

# Fungsi Penggunaan Round untuk membulatkan bilangan
print("\nContoh Fungsi Penggunaan Round")
print(round(5))
5
print(round(5.4))
5
print(round(5.5))
6
print(round(1.523, 2))
1.52
print(round(1.527, 2))
1.53

