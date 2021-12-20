
player1 = {"name":"rasul", "power":100}
player2 = {"name":"reynd", "power":250}

def train(player):
    player['power'] = player['power'] + 100

def attack(attacker, defender):
    if(attacker['power'] > defender['power']):
        print('serangan berhasil! selamat untuk ', attacker['name'])
    else:
        print('serangan gagal! kamu lemah ',attacker['name'])

train(player1)
train(player1)
attack(player1, player2)