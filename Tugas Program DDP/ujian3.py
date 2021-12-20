 # rata rata

n = int(input("\nBanyaknya Data : "))

print() #membuat baris baru
data = []
jum = 0

for i in range(0, n):
    temp = int(input("masukkan data ke-%d: "% (i+1)))
    data.append(temp)
    jum += data[i]
    rata2 = jum / n

print("\nRata-rata = %0.2f" % rata2)
 