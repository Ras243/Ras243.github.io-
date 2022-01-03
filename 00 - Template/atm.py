pin = int(input("Pin "))
saldo = int(10000000)
if(pin == 123456):
    print("[1] - pembayaran")
    print("[2] - setor tunai")
    print("[3] - tarik tunai")
    pilihan = int(input("Pilihan anda: "))
    if(pilihan == 1):
        bill = int(input("Pembayaran anda : "))
        saldo = saldo - bill
        print("Selamat Pembayaran Berhasil")
        print("Saldo Anda Sekarang : ",saldo)
    elif(pilihan == 2):
        setor = int(input("Setoran Anda : "))
        saldo = saldo + setor
        print("Setoran Anda Berhas")
        print("Saldo Anda Sekarang : ",saldo)
    elif(pilihan == 3):
        tarik = int(input("Nominal Yang Anda Tarik : "))
        saldo = saldo - tarik
        print("Penarikan Anda Berhasil")
        print("Saldo Anda Sekarang : ",saldo)
else:
    print("Password Salah")