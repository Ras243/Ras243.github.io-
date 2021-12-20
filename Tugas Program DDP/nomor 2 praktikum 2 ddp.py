#No.2 
#if statement

is_game_over = False
p1_pos = 5
e1_pos = 6
if p1_pos == e1_pos:
    is_game_over = True
    print("permainan Berakhir")
else:
    is_game_over = False
    print("permainan lanjut")

e2_pos = 7
if p1_pos == e1_pos:
    is_game_over = True
    print("permainan berakhir")
elif p1_pos == e2_pos:
    is_game_over = True
    print("permainan berakhir")
else:
    is_game_over = False
    print("permainan berlanjut")

p1_pos = 7
if p1_pos ==e1_pos:
    is_game_over =  True
    print("permainan berakhir")
elif p1_pos == e2_pos:
    is_game_over = True
    print("permainan berakhir")
else:
    is_game_over = False
    print("permainan berlanjut")

if p1_pos == e1_pos and p1_pos == e2_pos:
    is_game_over = True
    print("permainan berakhir")
else:
    is_game_over = False
    print("permainan lanjut")
    
