angka = [1.2,3.14,33.1,6.3,8.6,7.7,5.2,1.1,2.3,4.9,5.3]
print(angka)
print(angka[1],angka[2],angka[5],angka[7],angka[10])
print(angka[4])
print(angka[4:6],angka[1:4],angka[4:8])
print(angka[0:2],angka[4:6],angka[9:11])
print(sum(angka))
t=0
angka[3] = t
angka[5] = angka[3]
t = angka[3]
print(angka)
angka[3] = 6.3
angka[5] = 7.7
angka[3],angka[5] = angka[5],angka[3]
print(angka)
