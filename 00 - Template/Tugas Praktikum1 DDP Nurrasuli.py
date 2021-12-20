#PRAKTIKUM DDP
#NURRASULI
#INFORMATIKA D

#no.1
nama = "Nurrasuli"          #tipe data string
nim = "D0221399"            #tipe data string
jenis_kelamin = "Laki-laki" #tipe data string
tempat_lahir = "Dusun Hikma"#tipe data string
tgl_lahir = "02 april 2003" #tipe data string
hobi = "Main futsal"        #tipe data string
usia = 18                   #tipe data integer 
print("Nama          :",nama,"\nNim           :",nim,"\nJenis kelamin :",jenis_kelamin,"\nTempat lahir  :",tempat_lahir,"\nTgl lahir     :",tgl_lahir,"\nhobi          :",hobi)

#no.2
##Algorutma
##Operator penambahan
   
"ALGORITMA MENGGUNAKAN OPERATOR PENAMBAHAN"
"1.Mulai"
"2.Masukkan bilangan pertama (d)"
"3.Masukkan bilangan kedua (e)"
"4.Hitung hasil d+e"
"5.Tampilkan hasil"
"6.Selesai"

print('MEMBUAT PROGRAM OPERATOR ARITMATIKA')
d = int(input('MASUKKAN ANGKA 1 : '))
e = int(input('MASUKKAN ANGKA 2 : '))

# aritmatika operator penjumlahan
penjumlahan = d + e
print("hasil operasi + = ",penjumlahan)

# aritmatika operator pengurangan
pengurangan = d - e
print("hasil operasi - = ",pengurangan)

# aritmatika operator perkalian
perkalian = d * e
print("hasil operasi * = ",perkalian)

# aritmatika operator pembagian
pembagian = d / e
print("hasil operasi / = ",pembagian)

# aritmatika operator modulus
nilai_modulus = d % e
print("hasil operasi % = ",nilai_modulus)

#NO.3
# Menukar Triple(x,y,z) menjadi(y,z,x)
x = 20
y = 15
z = 10
print("sebelum di tukar")
print(x)
print(y)
print(z)

temp = x
x = y
y = z
z = temp

print("setelah di tukar")
print(x)
print(y)
print(z)

#atau ini
#Menukar Triple(x,y,z) menjadi(y,z,x)
x = int(input("nilai x : "))
y = int(input("nilai y : "))
z = int(input("nilai z : "))
hasil_pertukaran = y,z,x
print("triple bilangan bulat asli",x,y,z)
print("triple bilangan bulat menjadi",hasil_pertukaran)

