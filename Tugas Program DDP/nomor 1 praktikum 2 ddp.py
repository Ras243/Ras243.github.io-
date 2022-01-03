##No.1
# MEMBUAT PROGRAM PENAMBAHAN LIST

# ibu membeli 6 buah
buah = ["nanas","semangka","melon","jeruk","pisang","langsat"]
print("Sebelum ditambah:")
print(buah)

# ibu menambah apel dan durian
buah.append("apel")
buah.append("durian")
print("\nSetelah ditambah:")
print(buah)

# ibu mengganti buah pertama dengan manggis
buah[0]=("manggis")
print("\nSetelah diganti:")
print(buah)

# ibu menghapus elemen list
buah.remove("melon")
buah.remove("jeruk")
print("\nSetelah dihapus:")
print(buah)

#nama list dengan perulangan
print("\nnama list:")
x = 0
for i in buah:
    x = x+1
    print("buah ke",x,":",i)

# menampilkan panjang elemen list
pjg = len(buah)
print("panjang list:",pjg)
