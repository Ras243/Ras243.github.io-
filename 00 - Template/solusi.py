n = input('10:')
Total = 0
l = n
while(i>=1):
    if(i%2==1):
        total=total+i 
        if(i==1):
            print(i,end=" = ")
        else:
            print(l,end=" + ")
    i=i-1
print(total,end="9")