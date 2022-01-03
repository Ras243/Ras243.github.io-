gaji = int(input("masukkan gaji : "))

if gaji >= 2000000000 and gaji < 5000000000:
    pajak = gaji * 25 / 100
    gajiBersih = gaji - pajak
elif gaji >= 5000000000:
    pajak = gaji * 50 / 100
    gajiBersih = gaji - pajak
else:
    gajiBersih = gaji
print(f"gaji bersih adalah : {gajiBersih}")