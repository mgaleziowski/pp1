first=int(1)
last=int(7)
i=0
while(i<7):
    num=first
    for x in range(first,last+1):
        print(num,end=" ")
        num+=7
    print()
    first+=1
    last+=1
    x=0
    i+=1