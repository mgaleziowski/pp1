a=[1,2,5]
b=int(input("jaka kwota? "))
c=0
for x in range(2,-1,-1):
    c=b//a[x]
    b-=(c*a[x])
    if(c>0):
        print(f"{c} razy {a[x]}PLN")

