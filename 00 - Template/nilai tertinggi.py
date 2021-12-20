
def nilaitertinggi():
    list = []
    input1 = int(input("masukkan nilai pertama: "))
    list.append(input1)
    input2 = int(input("masukkan nilai kedua: "))
    list.append(input2)
    input3 = int(input("masukkan nilai ketiga: "))
    list.append(input3)
    nilai = max(list)

    print('nilai tertinggi adalah =>',str(nilai))

nilaitertinggi()