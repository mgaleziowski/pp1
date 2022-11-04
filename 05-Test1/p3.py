def f(amount_to_pay):
    am=0
    coin=[5,2,1]
    for i in range(3):
        am+=amount_to_pay//coin[i]
        amount_to_pay%=coin[i]
    return am
b=int(input("podaj ilosc "))
print(f(b))