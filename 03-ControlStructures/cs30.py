def ifprime(x):
    if(x==2):
        return True
    for y in range(2,x):
        if(x%y==0):
            return False
    return True

n=int(input("podaj ilosc liczb "))
i=0
a=2
while(i<n):
    if(ifprime(a)):
        print(a,end=" ")
        i+=1
    a+=1
