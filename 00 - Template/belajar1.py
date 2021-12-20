#agar hasil yg dikeluarkan mulai dari yg belakang

def reverse_string(text):
    kaco,cicci=len(text),''
    for i in range(0,kaco):
        cicci += text[kaco-i-1]
    return cicci

print(reverse_string("abcde"))