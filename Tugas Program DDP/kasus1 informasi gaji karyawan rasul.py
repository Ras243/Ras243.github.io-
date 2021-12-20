'''
#contoh kasus:
#NIM D0221399
#Gaji Pokok = Rp.1.000.000
#Gaji lembur/jam = Rp. 5000
#Lama lembur = Sesuai 2 angka terakhir nim
#Gaji lembur = (gaji lembur/jam)*lama lembur
#pajak = Sesuai 2 angka terakhir nim
'''

nama = "Nurrasuli (D0221399)"
gaji_pokok = 1000000
Lama_lembur = 99            
GajiLembur = 5000
Jumlah_lembur = GajiLembur * Lama_lembur
Gaji_kotor = gaji_pokok + Jumlah_lembur
pajak = 99 / 100
potongan = int(pajak * gaji_pokok)
Gaji_bersih = int(Gaji_kotor-potongan)

print("Informasi Gaji Karyawan")
print("Nama           :",nama)
print("Gaji Pokok     : Rp",gaji_pokok)
print("Gaji Lembur    : Rp",Jumlah_lembur)
print("Gaji Kotor     : Rp",Gaji_kotor)
print("Pajak          : Rp",pajak)
print("Potongan       : Rp",potongan)
print("Gaji Bersih    : Rp",Gaji_bersih)