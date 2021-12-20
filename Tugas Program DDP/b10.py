#b10

import datetime
tgl1 = datetime.date(1900,10,10)
tgl2 = datetime.date.today()
selisih = tgl2-tgl1
print(selisih.days)