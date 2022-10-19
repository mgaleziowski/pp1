first=int(1)
last=int(7)
for y in range(7):
    num=first
    for x in range(first,last+1):
        print(num,end=" ")
        num+=7
    print()
    first+=1
    last+=1
    x=0