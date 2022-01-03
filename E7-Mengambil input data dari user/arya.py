gaji = int(input("masukkan gaji : "))
pekerjaan = input("masukkan pekerjaan : ")

if pekerjaan == "pns":
    pajak = 5/100 * gaji
    gaji_bersih = gaji - pajak
else:
    pajak = 2/100 * gaji
    gaji_bersih = gaji - pajak
print("gaji bersih : ",gaji_bersih)