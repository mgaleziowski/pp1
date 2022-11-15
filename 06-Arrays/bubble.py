def bubblesort(a):
    for x in range(len(a)):
        for i in range(len(a)-1):
            if(a[i]>a[i+1]):
                help=a[i+1]
                a[i+1]=a[i]
                a[i]=help
    return a

def dechex(a):
    b=[]
    c=["A","B","C","D","E","F"]
    x=[]
    y=[]
    for r in range(10):
        b.append(r)
    b+=c
    while(a>0):
        x.append(b[a%16])
        a//=16
    for i in range(len(x)-1,-1,-1):
        y.append(str(x[i]))
    return "".join(y)

def bindec(a):
    a=list(str((a)))
    b=[]
    sum=0
    for i in range(len(a)-1,-1,-1):
        b.append(int(a[i]))
    for x in range(len(b)):
        sum+=b[x]*(2**x)
    return sum

