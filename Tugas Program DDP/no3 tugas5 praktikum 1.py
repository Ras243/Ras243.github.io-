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
#x = int(input("nilai x : "))
#y = int(input("nilai y : "))
#z = int(input("nilai z : "))
#hasil_pertukaran = y,z,x
#print("triple bilangan bulat asli",x,y,z)
#print("triple bilangan bulat menjadi",hasil_pertukaran)