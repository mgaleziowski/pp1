def fact(x):
    if(x==0 or x==1):
        return 1
    else:
        return fact(x-1)*x
    
a=int(input("podaj liczbe "))
print(f"silnia z {a} to {fact(a)}")