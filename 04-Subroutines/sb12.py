def sum(x):
    if(x==1):
        return 1
    else:
        return sum(x-1)+x

n=int(input("podaj zakres liczb [1;n] "))
print(f"suma wynosi {sum(n)}")