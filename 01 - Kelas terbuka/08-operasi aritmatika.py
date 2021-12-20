

print('MEMBUAT PROGRAM OPERATOR ARITMATIKA')
d = int(input('MASUKKAN ANGKA 1 : '))
e = int(input('MASUKKAN ANGKA 2 : '))

# aritmatika operator penjumlahan
hasil = d + e
print("hasil operasi + = ",hasil)

# aritmatika operator pengurangan
hasil = d - e
print("hasil operasi - = ",hasil)

# aritmatika operator perkalian
hasil = d * e
print("hasil operasi * = ",hasil)

# aritmatika operator pembagian
hasil = d / e
print("hasil operasi / = ",hasil)

# aritmatika operator eksponen(pangkat)
hasil = d ** e
print("hasil operasi ** = ",hasil)

# aritmatika operator modulus
hasil = d % e
print("hasil operasi % = ",hasil)

# aritmatika operator floor division
hasil = d // e
print("hasil operasi // = ",hasil)

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)
