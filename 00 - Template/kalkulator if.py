
ang1 = float(input("masukkan angka pertama: "))
op = input('''masukkan operator> + , - , * , / , ** , % , // : ''')
ang2 = float(input("masukkan angka kedua: "))

if(op == '+'):
    print(ang1 + ang2)
elif(op == '-'):
    print(ang1 - ang2)
elif(op == '*'):
    print(ang1 * ang2)
elif(op == '/'):
    print(ang1 / ang2)
elif(op == '**'):
    print(ang1 ** ang2)
elif(op == '%'):
    print(ang1 % ang2)
elif(op == '//'):
    print(ang1 // ang2)
else:
    print('Operator tidak Valid')
 