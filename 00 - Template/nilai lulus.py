nilai = int(input("masukkan nilai: "))

if(nilai >= 90 and nilai <= 100):
    print("Nilai A")
elif(nilai >= 101):
    print("Nilai Tidak ditemukan")
elif(nilai <= 89 and nilai >=80):
    print("Nilai B")
else:
    print("Kamu Tidak Tuntas")