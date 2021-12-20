print("## PROGRAM WARNET ##")
ulangi = True
pendapatan = 0

while(ulangi):
    user = input("Nama user: ")
    print("Pilih Paket: ")
    print("a. PC Plus (6000)")
    print("b. PC Plus (10.000)")
    paket = input("input paket (a/b)> ")

    print("berapa jam main?")
    jam = int(input("jawab> "))

    if(paket == "a"):
        pendapatan += 6000 * jam
    elif(paket == "b"):
        pendapatan += 10000 * jam
    else:
        print("salah pilih paket!")
    
    print(f"Total pendapatan saat ini: {pendapatan}")
    print("apakah mau input lagi?")
    jawab = input("jawab(y/t)>")
    ulangi = True if jawab == 'y' else False

print(f"Total Pendapatan hari ini: {pendapatan}")