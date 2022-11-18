def primearray(n):
    a=[]
    if(n<2):
        return False
    for r in range(2,n+1):
        a.append(r)
    for i in range(len(a)):
        if(a[i]>0):
            j=2
            while(a[i]*j<=n):
                a[(a[i]*j)-2]=0
                j+=1
    for x in range(a.count(0)):
        a.remove(0)
    return a

n=int(eval(input(">")))
pri=primearray(n)
a=[]
i=0
while(n>1):
    while(n%pri[i]==0):
        a.append(pri[i])
        n//=pri[i]
    i+=1
print(a)
        


                