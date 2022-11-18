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

def flip(a):
    b=[]
    for i in range(len(a)-1,-1,-1):
        b.append(a[i])
    return b

def search(a,b):
    a=list(str(a))
    b=str(b)
    pos=[]
    for i in range(len(a)):
        if(a[i]==b):
            pos.append(i)
    return pos

def factorial(a):
    if(a<0):
        return False
    if(a==0 or a==1):
        return 1
    else:
        return factorial(a-1)*a
    
def arytsum(a,b):
    if(a>b):
        return False
    if(a==b):
        return a
    else:
        return arytsum(a,b-1)+b
    
def avg(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum/len(a)

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