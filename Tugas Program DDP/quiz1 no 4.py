#membuat program yg menggambarkan lampu lalu lintas

import time
import os
dayatahan = int(input("daya tahan lampu : "))
for i in range(0,dayatahan):
    os.system("clear")
    print("MERAH")
    time.sleep(60)
    os.system("clear")
    print("KUNING")
    time.sleep(2)
    os.system("clear")
    print("HIJAU")
    time.sleep(60)
    os.system("clear")
