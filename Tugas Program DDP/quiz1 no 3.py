keluarga = ["Baharuddin","Dalmia","adhink","Artati","Desi","Jufri","Dewi","Hasbi","Linda","Nurrasuli","Alma"]
print(keluarga)
print(keluarga[9])
keluarga.append("rudi")
print(keluarga)
keluarga.remove("rudi")
print("\nsetelah dihapus")
print(keluarga)
keluarga[1] = ("ibu")
print(keluarga)
print("\nnama list:")
x = 0
for i in keluarga:
    x = x+1
    print("keluarga ke",x,":",i) 