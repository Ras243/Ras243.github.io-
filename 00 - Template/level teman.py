
import random

x = random.randrange(1,31)
print("Tanggal ulang tahun teman : ",x)
m = int(input("Tanggal mengucapkan selamat ulang tahun : "))
n = int(input("Jam mengucapkan selamat ulang tahun : "))

if m == x and n >= 0 and n<= 2:
    status = "sangat bro!"
elif m == x:
    status = "bro!"
else:
    status = "kurang bro!"

print(status)