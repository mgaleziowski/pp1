def f(card_number):
    nr=list(str(card_number))
    for i in range(2,12):
        nr[i]="*"
    return "".join(nr)

a=int(input("podaj numer karty "))
print(f(a))