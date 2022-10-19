def pow(x,y):
    if(y==0):
        return 1
    else:
        return pow(x,y-1)*x
    
a=int(input("podaj podstawe "))
b=int(input("podaj wykladnik "))
print(f"wynik wynosi {pow(a,b)}")