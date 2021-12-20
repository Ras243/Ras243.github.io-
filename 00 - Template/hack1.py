number = 0
while number < 101:
    a = input("masukkan kata kunci :")
    if a == "hack":
        for i in range(0,101,1):
            print("hacking is running....",i,"%")
            if i == 100:
                print("hacked!..","%")
                break
