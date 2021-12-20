

ulangi = True
while(ulangi):
    pin = int(input("Pin "))
    saldo = 15000000
    if(pin == 123456):
        print("[1] - Pembayaran")
        print("[2] - Setor Tunai")
        print("[3] - Tarik Tunai ")
        pilihan = int(input("Pilihan Anda : "))
        if(pilihan == 1):
            bill = int(input("Pembayaran Anda : "))
            saldo1 = saldo - bill
            print("Selamat Pembayaran Berhasil")
            print("Saldo Anda Sekarang : ",saldo1) 
            print("apakah mau transaksi lainnya?")
            jawab = input("jawab(y/t)>")
            ulangi = True if jawab == 'y' else False
            print("silahkan masukkan pin anda untuk transaksi lainnya")
        elif(pilihan == 2):
            setor = int(input("Setoran Anda : "))
            saldo1 = saldo + setor
            print("Setoran Anda Berhasil")
            print("Saldo Anda Sekarang : ",saldo1)
            print("apakah mau transaksi lainnya?")
            jawab = input("jawab(y/t)>")
            ulangi = True if jawab == 'y' else False
            print("silahkan masukkan pin anda untuk transaksi lainnya") 
        elif(pilihan == 3):
            tarik = int(input("Nominal Yang Anda Tarik : "))
            saldo1 = saldo - tarik
            print("Penarikan Anda Berhasil")
            print("Saldo Anda Sekarang : ",saldo1) 
            print("apakah mau transaksi lainnya?")
            jawab = input("jawab(y/t)>")
            ulangi = True if jawab == 'y' else False
            print("silahkan masukkan pin anda untuk transaksi lainnya")
    else:
        print("Password Salah")
        print("apakah mau input lagi?")
        jawab = input("jawab(y/t)>")
        ulangi = True if jawab == 'y' else False

    print("Silahkan Ambil Kartu Anda")