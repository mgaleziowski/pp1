def computepay(a,b):
    c=1
    if(a>40):
        c=1.5
    return a*b*c
a=int(input("podaj godziny "))
b=int(input("podaj stawke za godzine "))
print("wyplata wynosi:",computepay(a,b))
