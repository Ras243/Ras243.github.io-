#b05

print ("Jumlah Hari")
y = "s"
while y == "s" :
    x =str( input("Masukan Bulan dalam bentuk angka:"))
    if x == "1":
        jan = "Januari"
        jm1 = 31
        print("Bulan       :",jan)
        print("Jumlah hari :",jm1,"hari")
    elif x == "2":
        feb = "Februari"
        jm2 = "28 / 29"
        print("Bulan       :",feb)
        print("Jumlah hari :",jm2,"hari")
    elif x == "3":
        mar = "Maret"
        jm3 = 31
        print("Bulan       :",mar)
        print("Jumlah hari :",jm3,"hari")
    elif x == "4":
        apr = "April"
        jm4 = 30
        print("Bulan       :",apr)
        print("Jumlah hari :",jm4,"hari")
    elif x == "5":
        mei = "Mei"
        jm5 = 31
        print("Bulan       :",mei)
        print("Jumlah hari :",jm5,"hari")
    elif x == "6":
        jun = "Juni"
        jm6 =30
        print("Bulan       :",jun)
        print("Jumlah hari :",jm6,"hari")
    elif x == "7":
        jul = "Juli"
        jm7=31
        print("Bulan       :",jul)
        print("Jumlah hari :",jm7,"hari")
    elif x == "8":
        agus = "Agustus"
        jm8=31
        print("Bulan       :",agus)
        print("Jumlah hari :",jm8,"hari")
    elif x == "9":
        sep = "September"
        jm9 = 30
        print("Bulan       :",sep)
        print("Jumlah hari :",jm9,"hari")
    elif x == "10":
        okt = "Oktober"
        jm10 =31
        print("Bulan       :",okt)
        print("Jumlah hari :",jm10,"hari")
    elif x == "11":
        jun = "Novomber"
        jm11=30
        print("Bulan       :",jun)
        print("Jumlah hari :",jm11,"hari")
    elif x == "12":
        des = "Desember"
        jm12= 31
        print("Bulan       :",des)
        print("Jumlah hari :",jm12,"hari")
    else :
        print(f"Mohon maaf bulan {x} belum ditemukan")
        y = "s"