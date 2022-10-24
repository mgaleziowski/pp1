def countletter(x,y):
    count=0
    for i in range(len(x)):
        if(x[i]==y):
            count+=1
    return count

a=str(input("podaj slowo "))
b=input("podaj szukana litere ")
print(f"litera [{b}] wystepuje {countletter(a,b)} razy")
